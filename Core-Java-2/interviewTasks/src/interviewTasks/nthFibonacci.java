package interviewTasks;

public class nthFibonacci {
	private static int fib(int n) {
		int first = 0;
		int secound = 1;
		int temp;
		for (int i = 2; i <= n; i++) {
			temp = first;
			first += secound;
			System.out.println(first);
			secound = temp;
		}
		return first;
	}
	public static void main(String[] args) {
		System.out.println("The nth Fibbonaci number is :"+fib(10));
	}

}
