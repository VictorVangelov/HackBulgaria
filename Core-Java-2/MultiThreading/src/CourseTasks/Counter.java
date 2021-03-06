package CourseTasks;

import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Counter {

	AtomicInteger value = new AtomicInteger(0);
	int intValue = 0;
	boolean isLocked = false;
	final static Lock lock = new ReentrantLock();

	protected synchronized void intrementMe() {
		intValue++;
	}

	protected void increment() {
		value.incrementAndGet();
	}

	protected int getValue() {
		return value.get();
	}
}
