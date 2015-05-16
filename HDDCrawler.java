package com.hackbulgaria.fileruler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.apache.commons.io.FilenameUtils;

public class HDDCrawler {
    private final static String videoFormats = "mkv,flv,mng,wmv,mp4,mpeg,3gp,avi";
    private final static String imageFormats = "hdr,jpeg,tiff,rif,gif,bmp,png,exif,ppm,pgm,pbm,pnm";

    private final static List<String> videoFormatsList = Arrays.asList(videoFormats.split(","));
    private final static List<String> imageFormatsList = Arrays.asList(imageFormats.split(","));

    public static ArrayList<String> listOfMovies = new ArrayList<String>();
    public static ArrayList<String> listOfImages = new ArrayList<String>();

    public ArrayList<String> getListOfMovies() {
        return listOfMovies;
    }

    public ArrayList<String> getListOfImages() {
        return listOfImages;
    }

    private static boolean isVideoFormat(String ext) {
        if (videoFormatsList.contains(ext.toLowerCase())) {
            return true;
        }
        return false;
    }

    private static boolean isImageFormat(String ext) {
        if (imageFormatsList.contains(ext.toLowerCase())) {
            return true;
        }
        return false;
    }

    public static String getExtension(String filePathAndName) {
        return FilenameUtils.getExtension(filePathAndName);
    }

    public static void fillTheCollection(String filePathAndName) {
        String ext = getExtension(filePathAndName);
        if (isImageFormat(ext)) {
            listOfImages.add(filePathAndName);
        } else if (isVideoFormat(ext)) {
            listOfMovies.add(filePathAndName);
        }
    }
}