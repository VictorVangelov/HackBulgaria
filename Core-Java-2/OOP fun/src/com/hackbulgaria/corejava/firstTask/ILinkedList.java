package com.hackbulgaria.corejava.firstTask;


public interface ILinkedList<T> {

	void addFirst(T obj);
	void addLast(T obj);
	T getFirst();
	T getLast();
	T popFirst();
	T popLast();
	void removeFirst();
	void removeLast();
	int getSize();
	T getAt(int elementIndex);
	boolean isEmpty();
	void swapWithFirst(T obj);
	void swapWithLast(T obj);
	
	
	

}
