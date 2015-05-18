package com.hackbulgaria.corejava.firstTask;

import java.sql.Date;

public class BMW extends Car  {
	int numberOfDoors;


	BMW(String brandName, long mileage, Date dateOfBirth, int numberOfDoors ) {
		super(brandName);
		this.numberOfDoors = numberOfDoors;
		this.dateOfBirth = dateOfBirth;
		this.mileage = mileage;
		}




}
