package com.hackbulgaria.fileruler;

import java.util.ArrayList;

public class MoviesCollecion {
    public static ArrayList<Movie> movieCollection = new ArrayList<Movie>();

    public void add(Movie movie) {
        movieCollection.add(movie);
    }

    public ArrayList<Movie> getMovies() {
        return movieCollection;
    }
}
