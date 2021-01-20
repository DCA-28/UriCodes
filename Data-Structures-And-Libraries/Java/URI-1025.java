import java.io.IOException;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        
        Scanner sc2 = new Scanner(System.in);
		int global = 1;
 
		while(true) {
 
			int q = sc2.nextInt();
			int n = sc2.nextInt();
 
			if(q + n == 0) {
				break;
 
			}
 
			sc2.nextLine();
 
			int[] stones = new int[q];
 
			for(int i = 0; i < stones.length; i++) {
				stones[i] = sc2.nextInt();
				sc2.nextLine();
 
			}
 
			Arrays.sort(stones);
			HashMap<Integer, Integer> dictionary= new HashMap<Integer, Integer>();
 
			for (int i = 0; i < stones.length; i++) { 			
				int key = stones[i];
				if(dictionary.get(key) == null) { 
					dictionary.put(key, i + 1); 
				}						  
			 }	
			/* System.out.println(dictionary.entrySet()); */
			System.out.printf("CASE# %d:%n", global);
 
			for (int i = 0; i < n; i++) {
 
				int value = sc2.nextInt(); 
				String ans = find(dictionary,value);
				System.out.println(ans);
				sc2.nextLine();
 
			  }
 
			global += 1;
 
		}		
		sc2.close();
	}
 
	static String find(HashMap<Integer, Integer> dictionary, int value) {
		if(dictionary.get(value) != null) {
			return String.format("%d found at %d", value, dictionary.get(value));
 
		}
 
		else {
			return String.format("%d not found", value);
 
		}
        
    }
 
}
