package WebCrawer;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.http.HttpEntity;
import org.apache.http.client.fluent.Content;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

public class WebCrawler {


	public static CopyOnWriteArrayList<URL> failedUrls ;
	public static CopyOnWriteArrayList<URL> visitedUrls;
	public static CopyOnWriteArrayList<String> contentContainer;
	public static CopyOnWriteArrayList<String> stillNotVisited;
	private static HashMap<String, String> urlAndTitels = new HashMap<String, String>();
	public static ConcurrentLinkedQueue<String> hrefContainer;

	
	
	
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



	



	public static void crowler(String url, String needle) {
/*		visitedUrls.add(url);
		String content = getContent(url);
		checkForMatch(content, needle, url);
		UrlPreparer.fulfillNotVisited(content);*/

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
/*		String homeUrl = "http://www.mileycyrus.com/";
		setHomeUrl(homeUrl);
		// String formatedUrl = getURLHost(homeUrl);
		String url = "";
		String needle = "Bangerz";
		stillNotVisited.add(homeUrl);
		while (stillNotVisited.size() != 0) {
			url = stillNotVisited.get(0);
			stillNotVisited.remove(0);
			crowler(url, needle);*/
		}

	}


