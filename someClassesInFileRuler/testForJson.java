package com.hackbulgaria.fileruler;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.net.URL;

import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.HttpStatus;
import org.apache.commons.httpclient.methods.GetMethod;
import org.apache.http.HttpException;
import org.apache.http.HttpResponse;
import org.json.JSONException;

import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.http.exceptions.UnirestException;

public class testForJson {
	public static void main(String[] args) throws JSONException, IOException, UnirestException {
		HttpResponse<String> response = Unirest.get("http://api.imagga.com/v1/tagging?url=http%3A%2F%2Fplayground.imagga.com%2Fstatic%2Fimg%2Fexample_photo.jpg")
				  .header("accept", "application/json")
				  .header("authorization", "Basic YWNjX2YzYTVkYTc4N2ZmZTZmMDo0MmIwNWZhMTcwNjlhOGMzMDgwMjkyNDBkNjkwODU0Mw==")
				  .asString();
		System.out.println(response);
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

}
