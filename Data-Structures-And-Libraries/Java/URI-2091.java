import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while(true) {
			int numbers = Integer.parseInt(br.readLine());
			
			if(numbers == 0) break;
			
			String[] values = br.readLine().split(" ");
			Map<String, Integer> valuesDict = new HashMap<String, Integer>();
			
			for(String value: values) {
				if(valuesDict.get(value) == null) {
					valuesDict.put(value, 1);
					
				}
				
				else {
					valuesDict.replace(value, valuesDict.get(value) + 1);
					
				}
				
			}
			
			
			for(String number: valuesDict.keySet()) {
				
				if(valuesDict.get(number) % 2 != 0) {
					System.out.println(number);
					break;
					
				}
				
			}
			
		}

	}

}
