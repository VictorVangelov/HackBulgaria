package executionOfReadmeTasks;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class PropartiesFileParser {
	private HashMap<String, String> properties;
	private BufferedReader brInputFile;

	private static String getKey(String line) {
		String key = line.substring(0, line.indexOf("="));
		return key.trim();
	}

	private static String getValue(String line) {
		return line.substring(line.indexOf("=") + 1, line.length());
	}

	private static boolean isComment(String line) {
		if (line.charAt(0) == '#') {
			return true;
		} else {
			return false;
		}
	}

	public Map<String, String> parseProperties(File inputFile) throws IOException {
		brInputFile = new BufferedReader(new FileReader(inputFile));
		String currentLineOfFile;
		String key, value;
		while ((currentLineOfFile = brInputFile.readLine()) != null) {
			if (isComment(currentLineOfFile)) {
				key = getKey(currentLineOfFile);
				value = getValue(currentLineOfFile);
				properties.put(key, value);
			}
		}
		return properties;

	}

	public static void main(String[] args) {

	}

}
