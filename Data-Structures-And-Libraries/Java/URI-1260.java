import java.io.IOException;
import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Locale;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		int cases = sc.nextInt();
		sc.nextLine(); /*consuming the next empty line */
		sc.nextLine();
		
		HashMap<String, Integer> treesMap = new HashMap<String, Integer>();
		int totalTrees = 0;
		
		while(sc.hasNextLine()) {
			String specie = sc.nextLine();
			
			if(specie.length() == 0) {
				getSpecies(treesMap, totalTrees, "loop");
				totalTrees = 0;
				treesMap.clear();
				
			}
			
			else {
				
				if(treesMap.get(specie) != null) {
					treesMap.replace(specie, treesMap.get(specie) + 1);
				}
				else {
					treesMap.put(specie, 1);	
			}
				totalTrees += 1;
		  }		
		}	
		getSpecies(treesMap, totalTrees, "end");
		sc.close();
 
    }
    
    static void getSpecies(HashMap<String, Integer> dictionary,int totalTrees, String flag) {
		ArrayList<String> species = new ArrayList<String>();
		for(String specie : dictionary.keySet()) {
			species.add(specie);		
		}
		Collections.sort(species);
		
		for(String specie: species) {
			System.out.printf("%s %.4f%n", specie, (float) dictionary.get(specie) / totalTrees * 100);		
		}
		dictionary.clear();
		totalTrees = 0;
		
		if(flag == "loop") {
			System.out.println();			
		}
	}
 
}
