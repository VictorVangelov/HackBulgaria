package com.hackbulgaria.corejava.firstTask;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Iterator;

public class Time {

	int hour, min, sec, day, mounth, year;
	static Calendar now = Calendar.getInstance();
	private static int maxPeriodOverCurrEayer = 2000;;

	Time(int hour, int min, int sec, int day, int mounth, int year) {
		try {
			this.hour = hour;
			this.min = min;
			this.sec = sec;
			this.day = day;
			this.mounth = mounth;
			this.year = fixYear(year);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

	Time(int hour, int min, int day, int mounth, int year) {
		try {

			this.min = min;
			this.sec = now.get(Calendar.SECOND);
			this.hour = hour;
			this.day = day;
			this.mounth = mounth;
			this.year = fixYear(year);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

	Time(int hour, int day, int mounth, int year) {
		try {

			this.sec = now.get(Calendar.SECOND);
			this.min = now.get(Calendar.MINUTE);
			this.hour = hour;
			this.day = day;
			this.mounth = mounth;
			this.year = fixYear(year);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

	Time(int day, int mounth, int year) {
		try {
			this.hour = now.get(Calendar.HOUR);
			this.min = now.get(Calendar.MINUTE);
			this.sec = now.get(Calendar.SECOND);
			this.day = day;
			this.mounth = mounth;
			this.year = fixYear(year);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

	Time(int mounth, int year) {
		try {
			this.hour = now.get(Calendar.HOUR);
			this.min = now.get(Calendar.MINUTE);
			this.sec = now.get(Calendar.SECOND);
			this.day = now.get(Calendar.DAY_OF_MONTH);
			this.mounth = mounth;
			this.year = fixYear(year);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

	Time(int year) {
		try {
			this.hour = now.get(Calendar.HOUR);
			;
			this.min = now.get(Calendar.MINUTE);
			this.sec = now.get(Calendar.SECOND);
			this.day = now.get(Calendar.DAY_OF_MONTH);
			this.mounth = now.get(Calendar.MONTH);
			this.year = fixYear(year);
;

		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

	Time() {
		try {
			this.hour = now.get(Calendar.HOUR);
			this.min = now.get(Calendar.MINUTE);
			this.sec = now.get(Calendar.SECOND);
			this.day = now.get(Calendar.DAY_OF_MONTH);
			this.mounth = now.get(Calendar.MONTH);
			this.year = fixYear(now.get(Calendar.YEAR));

		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

	@Override
	public String toString() {
		return String.format("%02d:%02d:%02d %02d.%02d.%04d", this.hour,
				this.min, this.sec, this.day, this.mounth, this.year);
	}

	static private int fixYear(int year) {
		int currentBalance = now.get(Calendar.YEAR) - Time.maxPeriodOverCurrEayer;
		System.out.println(year+" < = "+currentBalance);
		if (year<= currentBalance) {
			return Integer.sum(year, maxPeriodOverCurrEayer);
		}else if(currentBalance<year & year <=99){
			return Integer.sum(year, 1900);	
		}else if(year >99 & year<999) {
		return Integer.sum(year, 1000);
		}else if (year >1000 & year<= now.get(Calendar.YEAR)){
			return year;
		}else {return now.get(Calendar.YEAR);}
		}

	public static void main(String[] args) {
		Time time1 = new Time(15);
		Time time2 = new Time(12, 16);
		Time time3 = new Time(14, 13, 899);
		Time time4 = new Time(1, 2, 3, 98);
		Time time5 = new Time(1, 2, 3, 4, 5);
		Time time6 = new Time(1, 2, 3, 4, 5, 99);
		Time time7 = new Time();
		ArrayList<Time> timesArray = new ArrayList<Time>(Arrays.asList(time1,time2, time3, time4, time5, time6, time7));
		Iterator<Time> timesIterator = timesArray.iterator();
		while (timesIterator.hasNext()) {
			System.out.println(timesIterator.next());

		}

	}
}
