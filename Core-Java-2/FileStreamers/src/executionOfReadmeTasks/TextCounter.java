package executionOfReadmeTasks;

public class TextCounter {

	public int getWordCount(String fileContent) {
		int numberOfWords = fileContent.split("\\s+").length;
		return numberOfWords;
	}

	public static void main(String[] args) {

	}
}