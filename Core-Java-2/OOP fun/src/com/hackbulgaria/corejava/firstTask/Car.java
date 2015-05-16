package com.hackbulgaria.corejava.firstTask;

import java.sql.Date;

public abstract class Car  {
	String brandName;
	long mileage;
	Date dateOfBirth;
	
	public String getBrandName()
	{
		return this.brandName;
	}
	Car(String brandName)
	{
		this.brandName = brandName;
	}
	public long getMileage()
	{
		return this.mileage;		
	}
	
	

}
