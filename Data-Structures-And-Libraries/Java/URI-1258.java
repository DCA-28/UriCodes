import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
 
public class Main {
 
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
 
		/*Maps for solving the problems */
 
		Map<Integer, ArrayList<String>> owners = new HashMap<Integer, ArrayList<String>>(){{
			put(1, new ArrayList<String>());
			put(2, new ArrayList<String>());
			put(3, new ArrayList<String>());
			put(4, new ArrayList<String>());
			put(5, new ArrayList<String>());
			put(6, new ArrayList<String>());		
		}};
 
		Map<String, Integer> colorSize = new HashMap<String, Integer>(){{
			put("brancoP", 1);
			put("brancoM", 2);
			put("brancoG", 3);
			put("vermelhoP", 4);
			put("vermelhoM", 5);
			put("vermelhoG", 6);			
		}};
 
		Map<Integer, String> related = new HashMap<Integer, String>(){{
			put(1, "branco P");
			put(2, "branco M");
			put(3, "branco G");
			put(4, "vermelho P");
			put(5, "vermelho M");
			put(6, "vermelho G");
		}};
 
		int cases = sc.nextInt();
		boolean lineControl = false;
 
		do {
			sc.nextLine();
			if(lineControl) System.out.println();
 
			for(int i = 0; i < cases; i++) {
				String name = sc.nextLine();
				String[] attributes = sc.nextLine().split(" ");
 
				int caseNumber = colorSize.get(attributes[0] + attributes[1]);
				owners.get(caseNumber).add(name);
			}
 
			sortDict(owners);
			/* all good till here */
 
			for(Map.Entry<Integer, ArrayList<String>> entry : owners.entrySet()) {
				if(entry.getValue().isEmpty()) {
					continue;
				}
				for(String owner : entry.getValue()) {
					System.out.printf("%s %s%n", related.get(entry.getKey()), owner);				
				}					
			}
 
			resetState(owners);
			lineControl = true;
 
			cases = sc.nextInt();
 
		}while(cases != 0);
 
	}
 
	static void resetState(Map<Integer, ArrayList<String>> ownersDict) {
		for(Integer element: ownersDict.keySet()) {
			ownersDict.put(element, new ArrayList<String>());
		}
 
	}
 
	static void sortDict(Map<Integer, ArrayList<String>> ownersDict) {
		for(Integer element : ownersDict.keySet()) {
			Collections.sort(ownersDict.get(element));		
		}
 
	}
}
