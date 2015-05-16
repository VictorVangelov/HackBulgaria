 
public class DatabaseCorruptedException extends Exception {

	private static String userMSG = "Ooops , there is a probleam about processing data from the DB!!!";


	public DatabaseCorruptedException(String msg, Throwable causedBy){
		super(msg ,causedBy.getCause());
	}
	
	public DatabaseCorruptedException(Throwable causedBy){
		super(userMSG,causedBy);
	}
	public DatabaseCorruptedException(){
		super(userMSG);
		System.out.println(userMSG);
	}

}
