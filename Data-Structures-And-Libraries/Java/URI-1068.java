import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		
		Map<Character, String> values = new HashMap<Character, String>() {{		
			put(')', "avaible");
			put('(', "avaible");
		}};
		
		while(sc.hasNextLine()) {
			String equation = sc.nextLine();
			
			if(equation.length() == 0) {
				System.out.println("correct");
				continue;
			}
			
			String result = analysis(equation, values);
			System.out.println(result);
		}
		 
		
		
	}
	static String analysis(String equation, Map<Character, String> values) {
		int state = 0;
		
		for(int i = 0; i < equation.length(); i++) {
			if(values.get(equation.charAt(i)) == null) {
				continue;
			}
			else{
				
				if(equation.charAt(i) == ')' && state == 0) {
					return "incorrect";
				}
				else if(equation.charAt(i) == ')' && state > 0) {
					state -= 1;				
				}
				else if(equation.charAt(i) == '(') {
					state += 1;					
				}
				
				}
			
			}
		if(state != 0) return "incorrect";
		
		else return "correct";
		}
	
}
