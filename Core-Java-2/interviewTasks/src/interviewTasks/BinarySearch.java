package interviewTasks;

import java.util.Arrays;

public class BinarySearch {
	public static void main(String[] args) {
		int[] sortedArr = { 1, 3, 4, 5, 11, 15, 24, 26, 29 };
		System.out.println(binarySearch(sortedArr, 2));

	}

	static int binarySearch(int[] arr, int wantedKey) {
		int start = 0;
		int end = arr.length;
		while (start <= end) {
			int middle = (start + end) / 2;
			if (wantedKey == arr[middle]) {
				return middle;
			} else if (wantedKey < arr[middle]) {
				end = middle - 1;
			} else {
				start = middle + 1;
			}
		}
		return -1;
	}
}
