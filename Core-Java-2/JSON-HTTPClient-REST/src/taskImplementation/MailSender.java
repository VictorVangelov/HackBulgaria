package taskImplementation;

import java.io.BufferedReader;
import java.io.Console;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

import org.apache.commons.mail.DefaultAuthenticator;
import org.apache.commons.mail.EmailAttachment;
import org.apache.commons.mail.EmailException;
import org.apache.commons.mail.MultiPartEmail;

public class MailSender {
	static MultiPartEmail email;
	static Scanner scanner;
	static Console console;

	private static String getPassword(String usernameAndPassword) {
	String	password[] = usernameAndPassword.split("-");
		return password[1];
	}

	private static String getUsername(String usernameAndPassword) {
		String	username[] = usernameAndPassword.split("-");
		return username[0];
	}

	private static String getRecipient() {
		/*
		 * scanner = new Scanner(System.in);
		 * System.out.print("Enter recipient email: "); String recipient =
		 * scanner.nextLine(); return recipient.trim();
		 */
		return "never_afraid@abv.bg";
	}

	public static EmailAttachment getDefaultAttachment() throws EmailException {
		EmailAttachment attachment = new EmailAttachment();
		attachment.setPath("HorseBite.gif");
		attachment.setDisposition(EmailAttachment.ATTACHMENT);
		attachment.setDescription("Picture of John and his horse");
		attachment.setName("John and his horse.gif");
		return attachment;
	}

	private static void sendMail(String username, String password,
			String recipient) {

		email = new MultiPartEmail();
		try {
			email.setHostName("smtp.googlemail.com");
			email.setSmtpPort(465);
			email.setAuthenticator(new DefaultAuthenticator(username, password));
			email.setSSLOnConnect(true);
			// email.setDebug(true);

			email.setSubject("TestMail from my program");
			email.setFrom(username);
			email.setMsg("This is a test mail ... :-)");
			email.addTo(recipient);
			email.attach(getDefaultAttachment());
			email.send();
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

	public static void main(String[] args) {
		Path pathToUsernameAndPass = Paths.get("SendMailAccAndPass.txt");
		String usernameAndPass = null;
		String username = "";
		String password = "";
		try {
			usernameAndPass = readFrom(pathToUsernameAndPass);
			username = getUsername(usernameAndPass);
			password = getPassword(usernameAndPass);

		} catch (IOException e) {
			e.printStackTrace();
		}
		String recipient = MailSender.getRecipient();
		sendMail(username, password, recipient);
	}

	public static String readFrom(File inputFile) throws IOException {
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new FileReader(inputFile));
		String currentLineOfFile;
		while ((currentLineOfFile = br.readLine()) != null) {
			sb.append(currentLineOfFile);
		}
		br.close();
		return sb.toString();
	}

	public static String readFrom(Path pathToFile) throws IOException {
		File inputFile = pathToFile.toFile();
		return MailSender.readFrom(inputFile);

	}

	public static File getFile(Path filePath) {
		return filePath.toFile();
	}

}
