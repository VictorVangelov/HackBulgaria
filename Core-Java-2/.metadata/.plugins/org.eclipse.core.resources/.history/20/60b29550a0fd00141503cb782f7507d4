package junitframework;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class TestClass {

	@Before(priority = Priority.MEDIUM)
	public void beforeFunction1() {
		System.out.println("Before 1");
	}

	@Before(priority = Priority.HIGH)
	public void beforeFunction2() {
		System.out.println("Before 2");
	}

	@Execute()
	public void executeFunction1() {
		System.out.println("Execution failed");
	}

	@Execute(done = true)
	public void executeFunction2() {
		System.out.println("Execution passed");
	}

	@After(priority = Priority.LOW)
	public void afterFunction1() {
		System.out.println("After 1");
	}

	@After(priority = Priority.MEDIUM)
	public void afterFunction2() {
		System.out.println("After 2");
	}

	static Comparator<Method> AfterComparator = new Comparator<Method>() {

		@Override
		public int compare(Method o1, Method o2) {
			if (o1.getAnnotation(Before.class) != null) {
				Before left = (Before) o1.getAnnotation(Before.class);
				Before right = (Before) o2.getAnnotation(Before.class);
				return right.priority().compareTo(left.priority());
			
			}
			return 0;
		}
	};
	
	static Comparator<Method> BeforeComparator = new Comparator<Method>() {
		@Override
		public int compare(Method o1, Method o2) {	
		if (o1.getAnnotation(After.class) != null) {
				After left = (After) o1.getAnnotation(After.class);
				After right = (After) o2.getAnnotation(After.class);
				return right.priority().compareTo(left.priority());
			}
			return 0;
		}
	};

	public static List<Method> getBefores() {
		List<Method> befores = new ArrayList<Method>();
		Class<TestClass> test = TestClass.class;
		for (Method method : test.getDeclaredMethods()) {
			if (method.isAnnotationPresent(Before.class)) {
				befores.add(method);
			}
		}
		befores.sort(BeforeComparator);
		return befores;
	}

	public static List<Method> getAfters() {
		List<Method> afters = new ArrayList<Method>();
		Class<TestClass> test = TestClass.class;
		for (Method method : test.getDeclaredMethods()) {
			if (method.isAnnotationPresent(After.class)) {
				afters.add(method);
			}
		}
		afters.sort(AfterComparator);
		return afters;
	}

	public static void executeMethods(List<Method> executables, TestClass test)
			throws IllegalAccessException, IllegalArgumentException,
			InvocationTargetException {
		for (Method method : executables) {
			method.invoke(test);
		}
	}

	public static void main(String[] args) throws IllegalAccessException,
			IllegalArgumentException, InvocationTargetException,
			InstantiationException {
		TestClass test = new TestClass();

		Method[] methods = test.getClass().getDeclaredMethods();

		List<Method> befores = getBefores();
		List<Method> executables = new ArrayList<Method>();
		List<Method> afters = getAfters();

		for (Method method : methods) {
			if (method.isAnnotationPresent(Execute.class)) {
				System.out.println("Testing " + method.getName() + "... ");
				executables.addAll(befores);
				executables.add(method);
				executables.addAll(afters);
				executeMethods(executables, test);
				System.out.println("--------------------------");
			}
			executables.clear();
		}

	}

}
