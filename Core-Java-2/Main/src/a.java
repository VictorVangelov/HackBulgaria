

import java.util.Collections;
import java.util.Iterator;
import java.util.List;

public class StackWithLinkedList<T> extends LinkedListImpl<T> implements Iterable<T> {
	private MyLink<T> first;
	private int size = 0;
	
	
	public   StackWithLinkedList<T> createLinkedStack(){
		
		IStack<T> linkedStack = new IStack<T>() {
			StackWithLinkedList<T> temp = new StackWithLinkedList<T>();
			@Override
			public void push(T element) {
				temp.addFirst(element);
				size++;
				
			}
			@Override
			public T pop() {
				size -= 1;
				return temp.popFirst();
			}
			
			@Override
			public int length() {
				return temp.getSize();
			}
			
			@Override
			public void clear() {
				temp = new StackWithLinkedList<T>();
				
			}
			
			@Override
			public boolean isEmpty() {
				return temp.getSize() == 0;
			}
			
			@Override
			public T peek() {
				return temp.getFirst();
			}
			@Override
			public Iterator<T> iterator() {
				return null;
			}
		};
		return  (StackWithLinkedList<T>)linkedStack;
	}


	@Override
	public Iterator<T> iterator() {
		Collections.reverse((List<T>) createLinkedStack());
		return null;
	}



	






}
