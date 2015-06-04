package interviewTasks2;

import interviewTasks.firstTasks;

import java.util.ArrayList;

public class QSort {

	public static <T extends Comparable<T>> void sort(T[] inputArr) {
		if (inputArr == null || inputArr.length == 0) {
			return;
		}
		quickSort(inputArr, 0, inputArr.length - 1);
	}

	private static <T> void swap(T[] inputArr, int firstElement,
			int secoundElement) {
		T temp = inputArr[firstElement];
		inputArr[firstElement] = inputArr[secoundElement];
		inputArr[secoundElement] = temp;
	}

	private static <T extends Comparable<T>> void quickSort(T[] inputArr,
			int lower, int higher) {
		if (lower < higher) {
			int i = lower;
			int j = higher;
			T x = inputArr[(i + j) / 2];
			do {
				while (x.compareTo(inputArr[j]) < 0) {
					j--;
				}
				while (inputArr[i].compareTo(x) < 0) {
					i++;
				}
				if (i <= j) {
					swap(inputArr, i, j);
				}
			} while (i <= j);
			if (lower < j){
				quickSort(inputArr, lower, j);
			}if(i<higher){
				quickSort(inputArr, i, higher);
			}
		}
	}
}
