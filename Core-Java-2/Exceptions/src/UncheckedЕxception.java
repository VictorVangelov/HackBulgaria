import java.util.ArrayList;
import java.util.Collection;

public class UncheckedЕxception {

	public static void main(String[] args) {
		Person p1 = new Person("", 21);
		Person p2 = new Person("123");
		Person p3 = new Person("as!#");
		Person p4 = new Person("asd");
		Person p5 = new Person(null, 1);
		ArrayList<Person> listOfPersons = new ArrayList<Person>();
		/*listOfPersons.add(p1);
		listOfPersons.add(p2);
		listOfPersons.add(p3);
		listOfPersons.add(p4);
		listOfPersons.add(p5);
		*/
		try {
			checkUsername(listOfPersons);
		} catch (DatabaseCorruptedException e) {
			e.printStackTrace();
		}
		

	}

	public static void checkUsername(Collection<Person> listOfPersons)
			throws DatabaseCorruptedException {
		try {
			for (Person person : listOfPersons) {
				isInvalidName(person);
			}
		} catch (InvalidUsernameException e) {
			throw new DatabaseCorruptedException(e);
		}
	}

	private static void isInvalidName(Person currPerson)
			throws InvalidUsernameException {
		try {
			isEmpty(currPerson.name);
			hasSpecialSymbols(currPerson.name);
			hasNumbers(currPerson.name);

		} catch (SpecialSymbolsInUsernameException | NumbersInUsernameException
				| NameIsEmptyException e) {
			throw new InvalidUsernameException(e);
		}

	}

	public static boolean hasSpecialSymbols(String name)
			throws SpecialSymbolsInUsernameException {
		String[] sb = name.split("[^!@$#%^&*()_-]+");
		if (sb.length != 0 |sb.toString()=="") {
			throw new SpecialSymbolsInUsernameException();
		}
		return false;
	}

	public static boolean isEmpty(String name) throws NameIsEmptyException {
		if (name.equals(null) | name.length() == 0) {
			throw new NameIsEmptyException();
		} else
			return false;
	}

	public static boolean hasNumbers(String name)
			throws NumbersInUsernameException {
		String[] sb = name.split("[^0-9 \\W]+");
		if (sb.length != 0) {
			throw new NumbersInUsernameException();
		}
		return false;
	}

}