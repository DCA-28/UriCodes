import java.io.BufferedReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while(true) {
			String[] entry = br.readLine().split(" ");
			
			if(Integer.valueOf(entry[0]) + Integer.valueOf(entry[1]) == 0) break;
			
			String[] secondEntry = br.readLine().split(" ");
			
			Set<Integer> remainingNumbers = new HashSet<Integer>();
			
			for(String element : secondEntry) {
				remainingNumbers.add(Integer.parseInt(element));
				
			}
			
			// Starting the analyses
			
			if(Integer.valueOf(entry[1]) > Integer.valueOf(entry[0])) {
				System.out.println('Y');
				continue;
			}
			
			else if(remainingNumbers.contains(Integer.valueOf(entry[0])) == false || 
					remainingNumbers.contains(0) == false) {
				System.out.println('N');
				continue;				
				
			}
			
			else {
				Set<Integer> numbersSequence = new HashSet<Integer>();
				
				for(int i = 0; i < Integer.valueOf(entry[0]) + 1; i++) {
					numbersSequence.add(i);
				}
				
				Set<Integer> calculated = new HashSet<Integer>() {{
					add(0);
				}};
				
				Set<Integer> used = new HashSet<Integer>();
				
				for(Integer number : remainingNumbers) {
					used.add(number);
					Set<Integer> subtract = new HashSet<Integer>(remainingNumbers);
					subtract.removeAll(used);
					
					for(Integer element : subtract) {
						calculated.add(Math.abs(number - element));
						
					}
				}
				
				if(calculated.equals(numbersSequence)) {
					System.out.println('Y');
					continue;
				}
				
				else {
					System.out.println('N');
					
				}
				
			}
			
		}

	}
}
