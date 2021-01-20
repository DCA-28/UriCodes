import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int globalCase = 1;
		
		while(true) {
			String toFind = br.readLine();
			if(toFind == null) break;
			if(globalCase > 1) System.out.println();
			
			String[] shoes = br.readLine().split(" ");
			
			boolean flag = false;
			int totalOcurrences = 0;
			int malePair = 0;
			int femalePair = 0;
			
			for(String information : shoes) {
				
				if(information.equals(toFind)) {
					totalOcurrences += 1;
					flag = true;
					
				}
				
				else {
					
					if(flag) {
						
						if(information.equals("M")) {
							malePair += 1 ;
						}
						else if(information.equals("F")) {
							femalePair += 1;
						}
						flag = false;
						
					}
					
				}
			}
			
			System.out.printf("Caso %d:%n", globalCase);
			System.out.printf("Pares Iguais: %d%n", totalOcurrences);
			System.out.printf("F: %d%n",femalePair);
			System.out.printf("M: %d%n", malePair);
			
			globalCase += 1;
			
		}
			

	}

}
