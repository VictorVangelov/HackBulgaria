package customAnnotations;

import java.lang.annotation.Annotation;

@classInfo (author = "Victor", revision = 3, checked = false, related = classInfo.class)

public class ClassInfo {
	public static void main(String[] args) {
		Class<ClassInfo> instance = ClassInfo.class;
		System.out.println(instance.getAnnotations());
		instance.getAnnotation(classInfo.class);
		System.out.println(instance.getAnnotation(classInfo.class));
		
		for (Annotation ann : instance.getAnnotations()) {
			classInfo annotation = (classInfo) ann; 
			System.out.println(annotation.author());
			System.out.println(annotation.checked());
			System.out.println(annotation.revision());
			System.out.println(annotation.related().toString());
		}
	}
}
