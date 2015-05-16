
public class NameIsEmptyException extends Exception {

	
	private static String userMsg = "Error : Username is empty or null";

	public NameIsEmptyException(Exception exc) {
		super(userMsg,exc);

	}
	
	
	
	public NameIsEmptyException(String msg,Exception exc) {
		super(msg,exc.getCause());
	}

	public NameIsEmptyException(){
		super(userMsg);
		System.out.println(userMsg);
	}


}
