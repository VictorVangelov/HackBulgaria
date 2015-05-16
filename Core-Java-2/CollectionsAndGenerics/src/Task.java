
public class Task implements Comparable{
float priority =1;
float timeToExecute = 0;
	@Override
	public int compareTo(Object o) {
		Task compTask = (Task) o;
		if (this.priority == compTask.priority)
		{
			if(this.timeToExecute< compTask.timeToExecute){
				return -1;
			}else {return 1;}
		
		}
		if(this.priority > compTask.priority){
			return -1;
			
		}else return 1;
	}

}
