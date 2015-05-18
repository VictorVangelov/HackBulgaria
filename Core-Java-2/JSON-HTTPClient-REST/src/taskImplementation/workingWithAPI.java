package taskImplementation;

import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.io.Writer;
import java.util.Iterator;

import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class workingWithAPI {

	private static void workWithApi(String url) throws IOException {
		String jsonContent = getContent(url);

		JSONArray allStudents;
		try {
			allStudents = new JSONArray(jsonContent);
		} catch (JSONException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	private void saveContentInFile(String filename, String jsonContent) throws FileNotFoundException {
		try (Writer writer = new BufferedWriter(new OutputStreamWriter(
				new FileOutputStream(filename), "utf-8"))) {
			writer.write(jsonContent);
			writer.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
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

	public static void main(String[] args) {
		String fileName = "allstudents.json";
		String url = "https://hackbulgaria.com/api/students/";
		workWithApi(url);
	}
}
