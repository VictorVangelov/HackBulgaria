package com.hackbulgaria.corejava.firstTask;


import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;

public class StackImpl<T> implements IStack<T>, Iterable<T> {

	private ArrayList<T> stackArray;
	public StackImpl() {
		 stackArray = new ArrayList<T>();
	}
	@Override
	public void push(Object element) {
		if (!stackArray.contains(element)) {
			stackArray.add((T) element);
		}
	}

	@Override
	public T pop() {
		try {
			T popedElement = peek();
			stackArray.remove(stackArray.size()-1);
			return popedElement;
		} catch (NullPointerException npe) {
			return null;
		}
	}

	@Override
	public int length() {
		return stackArray.size();
	}

	@Override
	public void clear() {
		stackArray.clear();
	}

	@Override
	public boolean isEmpty() {
		return stackArray.isEmpty();
	}

	@Override
	public T peek() {
		try {
			return stackArray.get(stackArray.size() - 1);
		} catch (NullPointerException npe) {
			return null;
		}
		
	}
	@Override
	public Iterator<T> iterator() {
		Collections.reverse(stackArray);
		return stackArray.iterator();
	}

}
