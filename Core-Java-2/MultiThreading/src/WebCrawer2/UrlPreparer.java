package WebCrawer2;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class UrlPreparer {
	private static String homeUrl;

	private static URL prepareLink(String link) throws MalformedURLException {
		return new URL(homeUrl + link.substring(1, link.length()));
	}

	private static void setHomeUrl(String newHomeUrl) {
		homeUrl = newHomeUrl;
	}

	private static boolean isOutgoing(String currentUrlBaseHost) {
		return homeUrl != getURLHost(currentUrlBaseHost);
	}

	private static boolean containHashTag(String url) {
		return url.contains("#");
	}

	static void fulfillNotVisited(String content) {
		for (String url : getAllLinks(content)) {
			if (!isOutgoing(url)) {
				if (!containHashTag(url)) {
					if (!WebCrawler2.visitedUrls.contains(url)) {
						URL preparedUrl;
						try {
							preparedUrl = prepareLink(url);
							WebCrawler2.stillNotVisited.add(preparedUrl);
						} catch (MalformedURLException e) {
							System.out.println(url + " is malformedUrl");
						}
					}
				}
			}
		}
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

	private static String getURLHost(String currentUrl) {
		try {
			URL aURL = new URL(currentUrl);
			return aURL.getHost();
		} catch (MalformedURLException e) {
			return homeUrl;
		}
	}

}