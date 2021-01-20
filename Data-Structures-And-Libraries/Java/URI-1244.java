import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);		
		Comp comparator = new Comp();
		
		ArrayList<String> strings = new ArrayList<>();
		
		int cases = sc.nextInt();
		sc.nextLine();
		
		for(int i = 0; i < cases; i++) {
			String[] stringVector = sc.nextLine().split(" ");
			int spaceControl = stringVector.length;
			
			strings.addAll(Arrays.asList(stringVector));
			Collections.sort(strings, comparator.reversed());
			
			int counter = 0;
			for(String word : strings) {
				if(counter != spaceControl - 1) {
					System.out.print(word + " ");
				}
				else {
					System.out.print(word);
				}
				
				++counter;
			}
			strings.clear();
			System.out.println();
		}
		
	 }
	
	  static class Comp implements Comparator<String>{
		public int compare(String s1, String s2) {
			return Integer.compare(s1.length(), s2.length());
		}
		
   }

}
