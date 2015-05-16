package CourseTasks;

public class Producer implements  Runnable {
	@Override
	public void run() {
		for(int i =0; i< 1_000;i++){
			synchronized (BlockingQueue.myQueue) {
				while(BlockingQueue.myQueue.size() == BlockingQueue.MAX_CAPACITY){
					try {
						BlockingQueue.myQueue.wait();
					} catch (InterruptedException e) {}
				}
				System.out.println(BlockingQueue.myQueue.size());
				BlockingQueue.myQueue.add("asd");
				BlockingQueue.myQueue.notify();
			}
			
		}
		
	}


}
