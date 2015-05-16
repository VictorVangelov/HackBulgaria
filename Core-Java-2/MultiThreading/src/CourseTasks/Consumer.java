package CourseTasks;

public class Consumer implements Runnable {

	@Override
	public void run() {
		for(int i =0; i< 1_000;i++){
			synchronized (BlockingQueue.myQueue) {
				while(BlockingQueue.myQueue.isEmpty()){
					try {
						BlockingQueue.myQueue.wait();
					} catch (InterruptedException e) {}
				}
				BlockingQueue.myQueue.poll();
				System.out.println(BlockingQueue.myQueue.size());
				BlockingQueue.myQueue.notify();
			}
			
		}
		
	}

}
