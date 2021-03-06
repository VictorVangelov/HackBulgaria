package CourseTasks;

import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

import javax.management.monitor.MonitorSettingException;

public class RaceCondition implements Runnable {
	public static Counter myCounter = new Counter();

	private synchronized void notifyMe() {
		try {
			myCounter.isLocked = false;
			myCounter.notifyAll();
			myCounter.wait();

		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
			
	}

	public void run() {
		synchronized (myCounter) {
			while (myCounter.isLocked) {
				try {
					myCounter.wait();
				} catch (InterruptedException e) {}
			}
			myCounter.isLocked = true;
			for (int i = 0; i < 200; i++) {
				 System.out.println(Thread.currentThread().getName());
				myCounter.intrementMe();
				//System.out.println(myCounter.intValue);
	
				notifyMe();
				
			}
			 System.out.printf("im out bitch %s    %s %n",Thread.currentThread().getName(),myCounter.intValue);
		}
	}

	/*
	 * private void notifyMe() { isLocked = lock.tryLock(); notifyAll();
	 * 
	 * 
	 * 
	 * }
	 * 
	 * public void run() { synchronized (this) { while (isLocked) { try {
	 * wait(); } catch (InterruptedException e) {
	 * System.out.println("i wasnt ready"); } } for (int i = 0; i < 2_000_000;
	 * i++) { // System.out.println(Thread.currentThread().getName());
	 * myCounter.increment(); notifyMe(); } } }
	 */

	public static void main(String[] args) {
		Thread a = new Thread(new RaceCondition());
		Thread b = new Thread(new RaceCondition());
		Thread c = new Thread(new RaceCondition());
		long startTime = System.currentTimeMillis();
		try {
			a.start();
			b.start();
			c.start();
			
			try {
				b.join();
				c.join();
				a.join();
			} catch (InterruptedException e) {
				System.out.println("i wasnt ready - b");
				e.printStackTrace();
			}

		} finally {
			long endTime = System.currentTimeMillis() - startTime;
			System.out.printf("my counter`s value : %d%n", myCounter.intValue);
			System.out.println("sums took: " + endTime);

		}
	}
}
