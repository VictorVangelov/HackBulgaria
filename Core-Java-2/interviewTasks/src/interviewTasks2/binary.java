package interviewTasks2;

public class binary {
	int binarySearch(int[] arr, int key) {
		int end = arr.length;
		int start = 0;
		int mid = (start + end) / 2;
		while (start <= end) {
			mid = (start + end) / 2;
			if (key == arr[mid]) {
				return mid;
			}
			if (key < arr[mid]) {
				end = mid - 1;
			}
			if (key > arr[mid]) {
				start = mid + 1;
			}
		}
		return -1;
	}

}
