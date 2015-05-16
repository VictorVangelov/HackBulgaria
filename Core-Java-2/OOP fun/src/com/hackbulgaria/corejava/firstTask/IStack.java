package com.hackbulgaria.corejava.firstTask;

import java.util.Iterator;

public interface IStack<T> {
	
	void push(T element);
	T pop();
	int length();
	void clear();
	boolean isEmpty();
	T peek();
	//Iterator<? extends Object> iterator();
	Iterator<T> iterator();
	

}
