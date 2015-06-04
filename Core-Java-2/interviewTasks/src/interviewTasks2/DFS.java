package interviewTasks2;

import java.util.ArrayList;
import java.util.Stack;

public class DFS {
	void dfs(ArrayList<ArrayList<Integer>> graphRep, int start) {
		Stack<Integer> myStack = new Stack<Integer>();
		myStack.push(start);
		boolean[] visited = new boolean[graphRep.size()];
		while (!myStack.isEmpty()) {
			int popedElement = myStack.pop();
			if (!visited[popedElement]) {
				visited[popedElement] = true;
				Stack<Integer> exStack = new Stack<Integer>();
				for (int chield : graphRep.get(popedElement)) {
					if(!visited[chield]){
						exStack.push(chield);
					}
				}
			while(!exStack.isEmpty()){
				myStack.push(exStack.pop());
			}
				}
		}

	}
}
