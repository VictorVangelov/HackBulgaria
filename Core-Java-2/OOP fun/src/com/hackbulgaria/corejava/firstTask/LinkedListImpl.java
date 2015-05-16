package com.hackbulgaria.corejava.firstTask;


public class LinkedListImpl<T> implements ILinkedList<T> {

	private MyLink<T> first;
	private MyLink<T> last;
	private int size = 0;

	public MyLink<T>[] getNeighbors(int index, boolean fromBeginning) {
		MyLink<T> temp1 = null;
		MyLink<T> temp2 = null;
		final MyLink<T>[] twoNeighbors;
		temp1 = this.last;
		if (!fromBeginning) {
			for (int i = 0; i < index; i++) {
				temp1 = temp1.getPreviousLink();
			}
			temp2 = temp1.getPreviousLink();
			twoNeighbors = new MyLink[] { temp2, temp1 };
		} else {
			for (int i = 0; i < index; i++) {
				temp1 = temp1.getNextLink();
			}
			temp2 = temp1.getNextLink();
			twoNeighbors = new MyLink[] { temp1, temp2 };
		}
		return twoNeighbors;
	}

	public void set(T obj, int index) {
		MyLink<T> newLink = null;
		MyLink<T> temp1 = null;
		MyLink<T> temp2 = null;
		if (index <= 0) {
			addFirst(obj);
		} else if (index >= this.size - 1) {
			addLast(obj);
		} else {
			if (isNearTheEnd(index)) {
				temp1 = getNeighbors(index, false)[0];
				temp2 = getNeighbors(index, false)[1];
			} else {
				temp2 = getNeighbors(index, false)[0];
				temp1 = getNeighbors(index, false)[1];
			}
			newLink = new MyLink<T>(obj, temp1, temp2);
			temp1.setNextLink( newLink);
			temp2.setPreviousLink(newLink);
		}
		this.size++;

	}

	public boolean isNearTheEnd(int index) {
		if (this.size / 2 < index) {
			return false;
		}
		return true;
	}

	@Override
	public void addFirst(T element) {
		MyLink<T> newLink = null;
		MyLink<T> temp = null;
		if (first== null) {
			newLink = new MyLink<T>(element, null, null);
			first = newLink;
			last = newLink;
		} else {
			temp = this.first;
			newLink = new MyLink<T>(element, null, temp);
			temp.setPreviousLink(newLink);
			this.first = newLink;
		}
		this.size++;

	}

	@Override
	public void addLast(T obj) {
		MyLink<T> newLink = null;
		MyLink<T> temp = null;
		if (newLink.equals(last)) {
			newLink = new MyLink<T>(obj, null, null);
			first = newLink;
			last = newLink;
		} else {
			temp = this.last;
			newLink = new MyLink<T>(obj, temp, null);
			temp.setNextLink(newLink);
			this.last = newLink;
		}
		this.size++;
	}

	@Override
	public T getFirst() {
		return (T) first.data;
	}

	@Override
	public T getLast() {
		return (T) last.data;
	}

	@Override
	public T popFirst() {
		MyLink<T> temp = first;
		addFirst((T)temp.getNextLink().data);

		return  temp.data;
	}

	@Override
	public T popLast() {
		MyLink<T> temp = last;
		addLast((T)temp.getPreviousLink().data);
		return (T) temp.data;
	}

	@Override
	public void removeFirst() {
		MyLink<T> temp = first.getNextLink();
		temp.setPreviousLink(null);
		first = temp;
		size--;

	}

	@Override
	public void removeLast() {
		if (this.size != 0) {
			MyLink<T> temp = last.getPreviousLink();
			temp.setNextLink(null);
			last = temp;
			size--;
		}
	}

	@Override
	public int getSize() {
		return size;
	}

	@Override
	public T getAt(int elementIndex) {
		MyLink<T> temp = null;
		if (0 <= elementIndex & elementIndex < size) {
			if (isNearTheEnd(elementIndex)) {
				temp = last;
				for (int i = 0; i < elementIndex; i++) {
					temp = temp.previousLink;
				}
			} else {
				temp = first;
				for (int i = 0; i < elementIndex; i++) {
					temp = temp.previousLink;
				}
			}
			return (T) temp.data;

		}
		return null;
	}

	@Override
	public boolean isEmpty() {

		return size == 0;
	}

	@Override
	public void swapWithFirst(T obj) {
		T dataFromFirstElement = first.data;
		this.first.data = obj;
		obj = dataFromFirstElement;
		
		

	}

	@Override
	public void swapWithLast(T obj) {
		T dataFromLastElement =  last.data;
		this.last.data = obj;
		obj = dataFromLastElement;

	}


}
