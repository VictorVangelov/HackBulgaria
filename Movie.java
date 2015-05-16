package com.hackbulgaria.fileruler;

import java.nio.file.Path;

public class Movie {

	int id;
	final String name;
	final String yearOfRelease;
	final String actors;
	final String scenarist;
	final String director;
	final String runtime;
	final String ganre;
	Path filePath;


    public Movie(String name, String yearOfRelease, String actors, String scenarist, String director, String runtime,
            String ganre, Path filePath) {
        this.name = name;
        this.yearOfRelease = yearOfRelease;
        this.actors = actors;
        this.scenarist = scenarist;
        this.director = director;
        this.runtime = runtime;
        this.ganre = ganre;
        this.filePath = filePath;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public String getYearOfRelease() {
        return yearOfRelease;
    }

    public String getActors() {
        return actors;
    }

    public String getScenarist() {
        return scenarist;
    }

    public String getDirector() {
        return director;
    }

    public String getRuntime() {
        return runtime;
    }

    public String getGanre() {
        return ganre;
    }

    public Path getFilePath() {
        return filePath;
    }

    public String toString() {
        return String.format("%s %s %s %s %s %s %s", /* getId(), */getName(), getYearOfRelease(), getActors(),
                getScenarist(), getDirector(), getRuntime(), getGanre());
    }
}
