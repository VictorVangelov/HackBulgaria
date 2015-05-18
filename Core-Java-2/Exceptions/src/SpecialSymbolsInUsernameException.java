
public class SpecialSymbolsInUsernameException extends Exception{
	
	private static String userMsg = "Error : Username contains Special Symbols like !@#$%^&*()";
	
	public SpecialSymbolsInUsernameException(){
		super(userMsg);
		System.out.println(userMsg);
	}
	public SpecialSymbolsInUsernameException(Throwable exc){
		super(userMsg, exc);
	}
	
	public SpecialSymbolsInUsernameException(String msg, Throwable exc){
		super(msg,exc);
	}

}
