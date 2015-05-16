package com.hackbulgaria.fileruler;

import java.nio.file.Path;
import java.nio.file.attribute.FileTime;
import java.util.HashMap;

public class Image {

	final String name;
	public final Path path;
	final int width;
	final int height;
	final FileTime createdDate;
	final HashMap<String, Long> imaggaTags;
	HashMap<String, Long> fileRulerTags;

	public HashMap<String, Long> getImaggaTags() {
		return imaggaTags;
	}
	public void addTagInFileRuler(String tag, Long conf){
		this.fileRulerTags.put(tag, conf);
	}

	public Image(Path path, String name, int width, int height,
			FileTime createdDate, HashMap<String, Long> imaggaTags) {
		this.path = path;
		this.name = name;
		this.width = width;
		this.height = height;
		this.createdDate = createdDate;
		this.imaggaTags = imaggaTags;
		this.fileRulerTags = new HashMap<String, Long>();
	}
}
