package WebCrawer2;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.commons.io.IOUtils;
import org.apache.http.HttpEntity;
import org.apache.http.client.fluent.Content;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.omg.CORBA.portable.InputStream;

public class WebCrawler2 {

	public static CopyOnWriteArrayList<URL> failedUrls = new CopyOnWriteArrayList<URL>();
	public static CopyOnWriteArrayList<URL> visitedUrls = new CopyOnWriteArrayList<URL>();

	public static ConcurrentLinkedQueue<URL> stillNotVisited = new ConcurrentLinkedQueue<URL>();;
	public static HashMap<URL, ArrayList<String>> urlAndTitels = new HashMap<URL, ArrayList<String>>();
	public static ConcurrentLinkedQueue<String> hrefContainer = new ConcurrentLinkedQueue<String>();;;

	private static Matcher getMatchedTitles(String content) {
		String formatedContent = content.replaceAll("\\s+", " ");
		Pattern p = Pattern.compile("<title>(.*?)</title>");
		Matcher match = p.matcher(formatedContent);
		return match;
	}

	private static ArrayList<String> prepareMatchResult(Matcher matcher) {
		ArrayList<String> listOfTitels = new ArrayList<String>();
		while (matcher.find() == true) {
			listOfTitels.add(matcher.group(0));
		}
		return listOfTitels;
	}

	public static void crowler(URL url, String needle)
			throws MalformedURLException, IOException {
		visitedUrls.add(url);
		String content = getContent(url);
		checkForMatch(needle);
		UrlPreparer.fulfillNotVisited(content);
	}

	private static void checkForMatch(String needle) {
		for (URL currUrl : urlAndTitels.keySet()) {
			for (String title : urlAndTitels.get(currUrl)) {
				if (title.contains(needle)) {
					System.out.println("\nWebsite : " + currUrl + "\n Title : "
							+ title);
				}
			}
		}
	}

	private void checkForMatch(String needle, URL url) {
		for (String title : urlAndTitels.get(url)) {
			if (title.contains(needle)) {
				System.out
						.println("\nWebsite : " + url + "\n Title : " + title);
			}
		}
	}

	protected static ArrayList<String> getTitels(String content) {
		Matcher titles = getMatchedTitles(content);
		return prepareMatchResult(titles);
	}

	public static void main(String[] args) throws MalformedURLException,
			IOException {
		WebCrawler2.stillNotVisited.add(new URL());
		
		new Thread(new RequestMaker()).start();
		
		
		/*
		 * String homeUrl = "http://www.mileycyrus.com/"; //
		 * setHomeUrl(homeUrl); // String formatedUrl = getURLHost(homeUrl);
		 * String url = ""; String needle = "Bangerz";
		 * stillNotVisited.add(homeUrl); while (stillNotVisited.size() != 0) {
		 * url = stillNotVisited.get(0); stillNotVisited.remove(0); crowler(url,
		 * needle); }
		 */
		// System.out.println(downloadContents(new
		// URL("http://www.nurkiewicz.com/2013/02/javautilconcurrentfuture-basics.html")));

	}

	public static String getContent(URL url) throws IOException {
		try (java.io.InputStream input = url.openStream()) {
			return IOUtils.toString(input, StandardCharsets.UTF_8);
		}
	}
}
