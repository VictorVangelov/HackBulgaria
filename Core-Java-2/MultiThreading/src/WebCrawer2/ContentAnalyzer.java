package WebCrawer2;

import java.util.concurrent.ConcurrentLinkedQueue;

public class ContentAnalyzer implements Runnable {
	//public static ConcurrentLinkedQueue<String> contentContainer = new ConcurrentLinkedQueue<String>();
	public static ConcurrentLinkedQueue<String> contentContainer = new ConcurrentLinkedQueue<String>();

	@Override
	public void run() {
		String currContent  = contentContainer.poll();
		WebCrawler2.urlAndTitels.put(currentUrl, WebCrawler2.getTitels(currContent));
		UrlPreparer.fulfillNotVisited(currContent);
		
		
	}
	
	
	
	
	

}
