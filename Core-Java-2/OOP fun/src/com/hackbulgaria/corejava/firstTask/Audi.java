package com.hackbulgaria.corejava.firstTask;

import java.sql.Date;

public class Audi extends Car {
	

	Audi(String name, long mileage, Date dateOfBirth) {
		super(name);
		this.mileage = mileage;
		this.dateOfBirth = dateOfBirth;
	}
	public Audi(String name) {
		super(name);
	}
	@Override
	public String toString(){
		return this.brandName;
	}

}
