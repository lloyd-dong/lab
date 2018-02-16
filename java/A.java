import java.util.List;
import java.util.Arrays;
import com.google.protobuf.ByteString;
//import java.util.Iterator;
import java.util.ArrayList;

public class A{
	public static void main(String[] args){
		// List<String> features = Arrays.asList("Lambdas", "Default Method", "Stream API", "Date and Time API");
		// features.forEach(n -> System.out.println(n));
		ByteString bs =  ByteString.copyFromUtf8("new string");
		// bs.forEach(b -> System.out.println(b));
		if (bs instanceof Iterable){
			System.out.println("instanceof of Iterator");
		}
		if (Iterable.class.isAssignableFrom(ByteString.class))
			System.out.println("an Iterable");
		 ArrayList<String> obj = new ArrayList<String>();
		 obj.add("Albert");
		 obj.add("Betty");
		 obj.forEach(item -> System.out.println(item));
		 if (obj instanceof Iterable)
		 	System.out.println("ArrayList is Iterable");
	}	
}
