package com.hackbulgaria.corejava.firstTask;

import java.util.Iterator;

public class StackWithLinkedList<T> implements IStack<T>{

	private LinkedListImpl<T> LinkedStack ;
	private int size = 0;



	private StackWithLinkedList() {
		LinkedStack = new LinkedListImpl<T>();
		size = 0;
	}

	public static <T> StackWithLinkedList<T> factory() {
		StackWithLinkedList<T> firstLinkedStack = new StackWithLinkedList<T>();

		return firstLinkedStack;
	}


	@Override
	public void push(T element) {
		this.LinkedStack.addFirst(element);
		// StackLinked.size++;

	}

	@Override
	public T pop() {
		this.size -= 1;
		return this.LinkedStack.popFirst();
	}

	@Override
	public int length() {
		return this.LinkedStack.getSize();
	}

	@Override
	public void clear() {
		this.LinkedStack = new StackWithLinkedList<T>().LinkedStack;

	}

	@Override
	public boolean isEmpty() {
		return this.LinkedStack.getSize() == 0;
	}

	@Override
	public T peek() {
		return this.LinkedStack.getFirst();
	}

	@Override
	public Iterator<T> iterator() {
		return null;
	}

	public static void main(String[] args) {
		Audi a3 = new Audi("a3");
		StackWithLinkedList<Audi> audiLinkedStack =  factory();
		audiLinkedStack.push(a3);
		System.out.println(audiLinkedStack.peek());
		System.out.println(audiLinkedStack.size);
		
	}
}

