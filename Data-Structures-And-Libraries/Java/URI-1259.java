import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		List<Integer> odd = new ArrayList<Integer>();
		List<Integer> even = new ArrayList<Integer>();
		int number = 0;
		
		int cases = sc.nextInt();
		sc.nextLine();
			
		for(int i = 0; i < cases; i++) {
			number = sc.nextInt();
			sc.nextLine();
			
			if(number % 2 == 0) even.add(number);
			
			else odd.add(number);
			
		}
		
		Collections.sort(even);
		Collections.sort(odd, Collections.reverseOrder());
		
		for(Integer value : even) {
			System.out.println(value);
		}
		
		for(Integer value : odd) {
			System.out.println(value);
		}

	}

}
