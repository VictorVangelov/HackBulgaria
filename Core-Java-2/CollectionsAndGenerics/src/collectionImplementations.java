import java.util.Collection;
import java.util.Iterator;
import java.util.Stack;


public class collectionImplementations {
	
	
	public static void main(String[] args) {
		
	}
	
	public static boolean exBrackets(String bracketsEx){
		Stack<Character> tempStack = new Stack<Character>();
		char ch ;
		for (int i = 0; i < bracketsEx.length(); i++) {
			ch = bracketsEx.charAt(i);
			
			if (ch == '(') {
				tempStack.add(bracketsEx.charAt(i));				
			}else if (ch == ')'){
				if(tempStack.size() == 0){
					return false;
				}else {tempStack.pop();}
			}
		}
		if (tempStack.size() != 0) {
			return false;
		}
		else {return true;}
	}

	public static void reversIt(Collection<Integer> someCollection){
		int collectionSize = someCollection.size();
		Iterator<Integer> myIter = new Iterator<Integer>() {

			@Override
			public boolean hasNext() {
				// TODO Auto-generated method stub
				return false;
			}

			@Override
			public Integer next() {
				// TODO Auto-generated method stub
				return null;
			}
		};
		
		
	}
}
