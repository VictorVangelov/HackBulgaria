package com.hackbulgaria.corejava.firstTask;

public class MyLink<T> {
	 MyLink<T>  nextLink=null;
	 MyLink<T> previousLink=null;
	 
	 T data;
	private int index;
	
	protected MyLink(T data, MyLink<T>  previousLink, MyLink<T>  nextLink){
		this.data = data;
		this.previousLink = previousLink;
		this.nextLink = nextLink;
	}
	
 	int getIndex() {
		return index;
	}
	void setIndex(int index) {
		this.index = index;
	}
	MyLink<T>  getNextLink() {
		return nextLink;
	}
	void setNextLink(MyLink<T> nextLink) {
		this.nextLink = nextLink;
	}
	MyLink<T> getPreviousLink() {
		return previousLink;
	}
	void setPreviousLink(MyLink<T> previousLink) {
		this.previousLink = previousLink;
	}
	T getData() {
		return data;
	}
	void setData(T data) {
		this.data = data;
	}

	public boolean hasPriveus() {
		if(this.previousLink.equals(null)){
			return false;
		}
		return true;
	}
	public boolean hasNext() {
		if(this.nextLink == null){
			return false;
		}
		return true;
	}
	
	
	
	
	
	

}
