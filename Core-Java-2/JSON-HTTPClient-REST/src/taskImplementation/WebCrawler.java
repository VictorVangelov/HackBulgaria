package taskImplementation;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

public class WebCrawler {

	private static String homeUrl;
	private static CopyOnWriteArrayList<String> visited = new CopyOnWriteArrayList<String>();
	private static CopyOnWriteArrayList<String> stillNotVisited = new CopyOnWriteArrayList<String>();
	private static HashMap<String, String> urlAndTitels = new HashMap<String, String>();

	private static String prepareLink(String link) {
		return homeUrl + link.substring(1, link.length());
	}

	private static void setHomeUrl(String newHomeUrl) {
		homeUrl = newHomeUrl;
	}

	private static boolean isOutgoing(String currentUrlBaseHost) {
		if (homeUrl != getURLHost(currentUrlBaseHost)) {
			return true;
		}
		return false;
	}

	private static String getURLHost(String currentUrl) {
		try {
			URL aURL = new URL(currentUrl);
			return aURL.getHost();
		} catch (MalformedURLException e) {
			return homeUrl;
		}
	}

	private static Matcher getMatchedTitles(String content) {
		String formatedContent = content.replaceAll("\\s+", " ");
		Pattern p = Pattern.compile("<title>(.*?)</title>");
		Matcher match = p.matcher(formatedContent);
		return match;
	}

	private static ArrayList<String> prepareMatchResult(Matcher matcher) {
		ArrayList<String> listOfTitels = new ArrayList<String>();
		while (matcher.find() == true) {
			listOfTitels.add(matcher.group(1));
		}
		return listOfTitels;
	}

	private static String getContent(String url) {

		CloseableHttpClient httpClient = HttpClients.createDefault();
		HttpGet getMethod = new HttpGet(url);
		CloseableHttpResponse response = null;
		String responseString = "";
		try {
			response = httpClient.execute(getMethod);
			HttpEntity entity = response.getEntity();
			if (entity != null) {
				responseString = EntityUtils.toString(entity, "UTF-8");
			}
		} catch (UnsupportedOperationException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		} catch (IOException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		} finally {
			if (response != null) {
				try {
					response.close();
				} catch (IOException e) {
					System.out.println(e.getMessage());
					e.printStackTrace();
				}
			}
		}
		return responseString;

	}

	private static List<String> getAllLinks(String content) {
		ArrayList<String> resultList = new ArrayList<>();
		String regex = "<a.*?href=\"((?!javascript).*?)\".*?>";
		Pattern pattern = Pattern.compile(regex);
		Matcher matcher = pattern.matcher(content);
		while (matcher.find() == true) {
			resultList.add(matcher.group(1));
		}
		return resultList;
	}

	private static boolean containHashTag(String url) {
		if (url.contains("#")) {
			return true;
		} else
			return false;
	}

	public static void crowler(String url, String needle) {
		visited.add(url);
		String content = getContent(url);
		checkForMatch(content, needle, url);
		fulfillNotVisited(content);

	}

	private static void fulfillNotVisited(String content) {
		for (String url : getAllLinks(content)) {
			if (!isOutgoing(url)) {
				if (!containHashTag(url)) {
					if (!visited.contains(url)) {
						String preparedLink = prepareLink(url);
						stillNotVisited.add(preparedLink);
					}
				}
			}
		}
	}

	private static void checkForMatch(String content, String needle, String url) {
		for (String title : getTitels(content)) {
			if (title.contains(needle)) {
				urlAndTitels.put(url, title);
				System.out
						.println("\nWebsite : " + url + "\n Title : " + title);
				// System.exit(0);
			}
		}
	}

	private static ArrayList<String> getTitels(String content) {
		Matcher titles = getMatchedTitles(content);
		return prepareMatchResult(titles);
	}

	public static void main(String[] args) {
		String homeUrl = "http://www.mileycyrus.com/";
		setHomeUrl(homeUrl);
		// String formatedUrl = getURLHost(homeUrl);
		String url = "";
		String needle = "Bangerz";
		stillNotVisited.add(homeUrl);
		while (stillNotVisited.size() != 0) {
			url = stillNotVisited.get(0);
			stillNotVisited.remove(0);
			crowler(url, needle);
		}

	}

}
