

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;

import org.apache.http.HttpEntity;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.*;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;

import java.lang.AutoCloseable;

@Author(name="Shosho", date="05.05.2015")
public class FileDownloader {

	public static void downloader(String hddUrl, String myUrl)
			throws ClientProtocolException, IOException {
		CloseableHttpClient httpclient = HttpClients.createDefault();
		HttpGet httpGet = new HttpGet(myUrl);
		CloseableHttpResponse response = httpclient.execute(httpGet);
		HttpEntity entity = response.getEntity();
		if (entity != null) {
			InputStream inStream = entity.getContent();
			try (BufferedInputStream bis = new BufferedInputStream(inStream);
					BufferedOutputStream bos = new BufferedOutputStream(
							new FileOutputStream(new File(hddUrl)));) {
				int inputByte;
				while ((inputByte = bis.read()) != -1) {
					bos.write(inputByte);
				}
				bis.close();
				bos.close();
			} catch (IOException ioe) {
				System.out.println(ioe.getMessage());
			} catch (RuntimeException rte) {
				httpGet.abort();
				System.out.println(rte.getMessage());
			} finally {
				inStream.close();
			}
			httpclient.close();
		}

	}

	public static void main(String[] args) throws ClientProtocolException,
			IOException {
		String filePath = "/home/shosho/Downloads/";
		String fileName = "TestableImage.jpg";
		String wantedUrl = "http://d3dsacqprgcsqh.cloudfront.net/photo/aozrdx0_700b.jpg";
		;
		downloader(filePath + fileName, wantedUrl);
		/*
		 * String fileName = args[0]; String newFileUrl = args[1];
		 * downloader(fileName,newFileUrl);
		 */
	}
}
