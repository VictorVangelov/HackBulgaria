package CourseTasks;

import java.util.LinkedList;
import java.util.Queue;

public class BlockingQueue {

	static Queue<String> myQueue = new LinkedList<String>();
	static boolean isEmpty = true;
	static final int  MAX_CAPACITY = 5;
	static String polledString;

	public static void main(String[] args) throws InterruptedException {
		Thread producer1 = new Thread(new Producer());
		Thread producer2 = new Thread(new Producer());
		Thread producer3 = new Thread(new Producer());
		
		Thread consumer1 = new Thread(new Consumer());
		Thread consumer2 = new Thread(new Consumer());
		Thread consumer3 = new Thread(new Consumer());
		long startTime = System.currentTimeMillis();
		try {
			producer1.start();
			producer2.start();
			producer3.start();
			consumer1.start();

			
			try {
				producer1.join();
				producer2.join();
				producer3.join();
				consumer1.join();

			} catch (InterruptedException e) {
				System.out.println("i wasnt ready - b");
				e.printStackTrace();
			}

		} finally {
			long endTime = System.currentTimeMillis() - startTime;

			System.out.println("sums took: " + endTime);
		}
		
	}
	void beforeBonusMain() throws InterruptedException{
		Thread adder = new Thread() {
			public void run() {
				for (int i = 0; i < 2_0; i++){
					synchronized (myQueue) {
						while (!isEmpty) {
							try {
								myQueue.wait();
							} catch (InterruptedException e) {
							}
						}
						isEmpty = false;
						myQueue.add("Text by Adder");
						System.out.println("i fullfiled the Queue");
						myQueue.notify();
					}
				}
			}
		};
		Thread poller = new Thread() {
			public void run() {
				for (int i = 0; i < 2_0; i++) {
					synchronized (myQueue) {
						while (isEmpty) {
							try {
								
								myQueue.wait();
							} catch (InterruptedException e) {
							}
						}
						
						isEmpty = true;
						polledString= myQueue.poll();
						System.out.println("I polled from the queue, and now its empty");
						myQueue.notify();
					}
				}
			}
		};

		adder.start();
		poller.start();
		adder.join();
		System.out.println("adder has finished");
		poller.join();
		System.out.println("poller hasFinished");
		
	}
}
