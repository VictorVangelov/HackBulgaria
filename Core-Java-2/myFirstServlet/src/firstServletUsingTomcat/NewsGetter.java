package firstServletUsingTomcat;

import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import sun.awt.image.ByteArrayImageSource;

import com.sun.syndication.feed.synd.SyndEntry;
import com.sun.syndication.feed.synd.SyndFeed;
import com.sun.syndication.io.SyndFeedInput;
import com.sun.syndication.io.XmlReader;

public class NewsGetter {

	public static String getNews() {
		StringBuilder outputContent = new StringBuilder();
		ArrayList<SyndEntry> syndEntrys = getSyndEntrys();
		String template = " <item>  <br><a href=%s>%s</a>  <br><br>"
				+ "  <description>%s</description></item><br><br><br><br>";

		String title;
		String link, description, tempContent;

		for (SyndEntry entry : syndEntrys) {
			/*
			 * title = entry.getTitle().getBytes("UTF-8").toString(); link =
			 * entry.getLink().getBytes("UTF-8").toString(); author
			 * =entry.getAuthor().getBytes("UTF-8").toString();
			 */
			title = entry.getTitle();
			link = entry.getLink();
			description = entry.getDescription().getValue();
			tempContent = String.format(template, link, title, description);
			outputContent.append(tempContent);
		}
		return outputContent.toString();

	}

	public static ArrayList<SyndEntry> getSyndEntrys() {
		ArrayList<SyndEntry> listOfSyndEntrys = new ArrayList<SyndEntry>();
		try {
			URL url = new URL("http://www.dnevnik.bg/rssc/?rubrid=1657");
			HttpURLConnection httpcon = (HttpURLConnection) url
					.openConnection();
			// Reading the feed
			SyndFeedInput input = new SyndFeedInput();
			SyndFeed feed = input.build(new XmlReader(httpcon));
			List<SyndEntry> entries = feed.getEntries();
			Iterator<SyndEntry> itEntries = entries.iterator();
			SyndEntry entry;
			StringBuilder siteContent = new StringBuilder();
			while (itEntries.hasNext()) {
				entry = itEntries.next();

				listOfSyndEntrys.add(entry);
			}
			return listOfSyndEntrys;
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return listOfSyndEntrys;

	}
}