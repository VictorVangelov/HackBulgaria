package com.hackbulgaria.fileruler;

import java.awt.image.BufferedImage;
import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributes;
import java.nio.file.attribute.FileTime;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;

import javax.imageio.ImageIO;

import org.apache.commons.httpclient.methods.PostMethod;
import org.apache.commons.httpclient.methods.multipart.Part;
import org.apache.commons.io.IOUtils;
import org.apache.http.HttpException;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.entity.mime.MultipartEntity;
import org.apache.http.entity.mime.content.InputStreamBody;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.params.CoreProtocolPNames;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.google.gson.JsonObject;

public class ImageFactory extends Thread {
	


	String name;
	Path path;
	int width;
	int height;
	FileTime createdDate;
	HashMap<String, Long> imaggaTags;
	ArrayList<String> fileRulerTags;
	JsonObject imaggaJSON;
	BufferedImage bimg;
	BasicFileAttributes attr;

	public ImageFactory(String filePathAndName) {
		super(filePathAndName);
	}

	public static String readFrom(File inputFile) throws IOException {
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new FileReader(inputFile));
		String currentLineOfFile;
		while ((currentLineOfFile = br.readLine()) != null) {
			sb.append(currentLineOfFile);
		}
		br.close();
		return sb.toString();
	}

	public static void main(String[] args) throws URISyntaxException {
		ArrayList<String> asd = new ArrayList<String>();
		asd.add("/home/shosho/ProgrammingShits/HackBulgaria/FileRuler/FileRuler/FileRuler/11.jpg");
		asd.add("/home/shosho/ProgrammingShits/HackBulgaria/FileRuler/FileRuler/FileRuler/12.jpg");
		System.out.println(getTagsFromImmaga(asd));

	}

	@SuppressWarnings("deprecation")
	public static String getTagsFromImmaga(Collection<String> coll) {

		String uploadImageURL = "http://api.imagga.com/v1/content";
		String tagsURL = "http://api.imagga.com/v1/tagging";
		CloseableHttpClient httpclient = null;
		HttpPost httpPost = null;
		String result = "";

		String imageID = "";
		byte[] data;
		InputStream inResponse;
		HttpResponse httpResponse;
		for (String strPath : coll) {

			try {
				// Input stream for image
				BufferedInputStream in = new BufferedInputStream(
						new FileInputStream(strPath));
				try {
					data = IOUtils.toByteArray(in);
					// Output stream for image
					httpclient = HttpClients.createDefault();
					httpclient.getParams().setParameter(
							CoreProtocolPNames.USER_AGENT,
							System.getProperty("http.agent"));
					httpPost = new HttpPost(uploadImageURL);
					InputStreamBody inputStreamBody = new InputStreamBody(
							new ByteArrayInputStream(data), strPath);
					MultipartEntity multipartEntity = new MultipartEntity();
					multipartEntity.addPart("file", inputStreamBody);
					httpPost.setEntity(multipartEntity);
					httpResponse = httpclient.execute(httpPost);
					// Handle response back from script.
					if (httpResponse != null) {
						inResponse = httpResponse.getEntity().getContent();
						imageID = "" + inResponse.read();

					} else { // Error, no response.
						new IOException("Error: When upload image, "
								+ httpResponse + " is null.");
					}


					// httpclient = HttpClients.createDefault();
					httpclient.getParams().setParameter(
							CoreProtocolPNames.USER_AGENT,
							System.getProperty("http.agent"));
					try {
						URIBuilder builder = new URIBuilder(tagsURL)
								.addParameter("content", imageID);

						HttpGet method = new HttpGet(builder.build());
						httpResponse = httpclient.execute(method);

						if (httpResponse != null) {
							InputStream inResponse1 = httpResponse.getEntity()
									.getContent();
							result = "" + inResponse1.read();

						} else { // Error, no response.
							new IOException("Error: When upload image, "
									+ httpResponse + " is null.");
						}
					} catch (URISyntaxException e) {
						e.printStackTrace();
					}

				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} finally {
					in.close();
				}
			} catch (ClientProtocolException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			}

		} // end for()
		return result;
	}

	@Override
	public void run() {

		name = new File(getName()).getName();
		name = name.substring(0, name.lastIndexOf('.'));

		try {
			path = Paths.get(new URI(getName()));

			// jsonContent = list ot tagove - response ot immaga

			String jsonContent = readFrom(new File("exampleJson.json"));
			JSONObject obj = new JSONObject(jsonContent);
			JSONArray arr = obj.getJSONArray("results");
			JSONObject imaggaInformation = arr.getJSONObject(0);
			JSONArray tagsAndConfidence = (JSONArray) imaggaInformation
					.get("tags");
			for (int i = 0; i < tagsAndConfidence.length(); i++) {
				String tag = tagsAndConfidence.getJSONObject(i)
						.getString("tag");
				long confidence = tagsAndConfidence.getJSONObject(i).getLong(
						"confidence");
				imaggaTags.put(tag, confidence);
			}
			name = getName().substring(
					name.lastIndexOf(File.pathSeparator) + 1,
					name.lastIndexOf('.'));
			path = Paths.get(new URI(getName()));
			bimg = ImageIO.read(new File(getName()));
			width = bimg.getWidth();
			height = bimg.getHeight();
			attr = Files.readAttributes(path, BasicFileAttributes.class);
			FileTime createdDate = attr.creationTime();
			ImagesCollection.imagesCollection.add(new Image(path, name, width,
					height, createdDate, imaggaTags));

		} catch (JSONException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		} catch (IOException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		} catch (URISyntaxException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}
	}

	void generateAllMovies() {
		for (String pathToFile : HDDCrawler.listOfMovies) {
			new ImageFactory(pathToFile).start();

		}
	}

}
