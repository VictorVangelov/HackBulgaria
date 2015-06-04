package WebCrawer2;

import java.net.MalformedURLException;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.Callable;
import java.util.concurrent.Executors;

import org.apache.commons.io.IOUtils;

import com.google.common.util.concurrent.Futures;
import com.google.common.util.concurrent.ListenableFuture;
import com.google.common.util.concurrent.ListeningExecutorService;
import com.google.common.util.concurrent.MoreExecutors;

public class asd {
	static ListeningExecutorService pool = MoreExecutors
			.listeningDecorator(Executors.newCachedThreadPool());

	public static void main(String[] args) throws MalformedURLException {
		WebCrawler2.stillNotVisited.add(new URL("http://www.nurkiewicz.com/2013/02/listenablefuture-in-guava.html"));
		WebCrawler2.stillNotVisited.add(new URL("http://www.nurkiewicz.com/2013/02/javautilconcurrentfuture-basics.html"));
		URL currentUrl = WebCrawler2.stillNotVisited.poll();
		while(!WebCrawler2.stillNotVisited.isEmpty()) {
		}
		final ListenableFuture<String> future = pool
				.submit(new Callable<String>() {
					@Override
					public String call() throws Exception {
						return IOUtils.toString(currentUrl,
								StandardCharsets.UTF_8);
					}
				});
		Futures.addCallback(future,
				new com.google.common.util.concurrent.FutureCallback<String>() {
					@Override
					public void onFailure(Throwable error) {
						System.out.println("failere\n" + error.getCause());
					}

					@Override
					public void onSuccess(String content) {
						// Is that a correct way to do that Shit
						System.out.println(currentUrl);
						//System.out.println(content);
						WebCrawler2.urlAndTitels.put(currentUrl,	WebCrawler2.getTitels(content));
						UrlPreparer.fulfillNotVisited(content);
					}
				});

	/*	try {
			WebCrawler.stillNotVisited.wait();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}*/
	}
}
