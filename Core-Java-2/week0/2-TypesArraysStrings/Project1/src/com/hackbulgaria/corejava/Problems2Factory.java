package com.hackbulgaria.corejava;

public class Problems2Factory {
    String OATH_TOKEN = "THIS IS MY DEAR PASSWORD";

    public static Problems2 createProblems2Instance() {
        return new Problems2Impl();
    }

    public static void main(String[] args) {
    	createProblems2Instance().convertToGrayscale("");
    }

    public static void meh(Integer k) {
    }
}
