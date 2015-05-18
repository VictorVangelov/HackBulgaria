
public class InvalidUsernameException extends Exception{
		
	private static String userMsg = "Wrong or not good defined username";
	
	public InvalidUsernameException(){
		super(userMsg);
		System.out.println(userMsg);
	}
	
	public InvalidUsernameException(Throwable exc){
		super(userMsg, exc);
	}
	public InvalidUsernameException(String msg, Throwable exc){
		super(msg,exc.getCause());
	}

}
