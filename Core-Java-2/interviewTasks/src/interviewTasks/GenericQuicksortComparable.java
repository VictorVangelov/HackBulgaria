package interviewTasks;

import java.util.Arrays;

public class GenericQuicksortComparable {

	public static <T extends Comparable<T>> void sort(T[] arr) {
		int length = arr.length;
		if (length == 0 || arr == null) {
			return;
		}
		qsort(arr, 0, length - 1);
	}

	private static <T> void swap(T[] arr, int i, int j) {
		T temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	private static <T extends Comparable<T>> void qsort(T[] arr, int lower,
			int higher) {
		if (lower < higher) {
			int i = lower, j = higher;
			T x = arr[(i + j) / 2];

			do {
				while (arr[i].compareTo(x) < 0)
					i++;
				while (x.compareTo(arr[j]) < 0)
					j--;

				if (i <= j) {
					swap(arr, i, j);
					i++;
					j--;
				}

			} while (i <= j);
			if (lower < j) {

				qsort(arr, lower, j);
			}
			if (i < higher) {
				qsort(arr, i, higher);
			}
		}
	}

	public static void main(String[] args) {
		Double[] ia = { 30.1d, 20d, 10d, 5d, 6.1d, 9.9d, 99d };
		GenericQuicksortComparable.<Double> sort(ia);
		System.out.println(Arrays.toString(ia));

	}
}