
public class NumbersInUsernameException extends Exception{
	

	public NumbersInUsernameException(Exception causedBy) {
		super(userMsg,causedBy);
	}
	public NumbersInUsernameException(){
		super(userMsg);
		System.out.println(userMsg);
	}
	
	public NumbersInUsernameException(String msg, Exception causedBy){
		super(userMsg, causedBy.getCause());
	}
	private static String userMsg = "Error: Username contains numbers";
	
	


}
