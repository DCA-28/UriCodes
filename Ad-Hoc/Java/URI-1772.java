import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(ir);
		
		while(true) {
			String[] entry = br.readLine().split(" ");
			if ((entry[0] + entry[1]).equals("00")) break;
			
			Long number = Long.valueOf(entry[0]);
			int swaps = Integer.valueOf(entry[1]);
			Long actualValue = number;
			
			String bitNumber = Long.toBinaryString(number);
			char[] binNumber = bitNumber.toCharArray();
			Map<Integer, Character> bitDict = new HashMap<Integer, Character>();
			
			initializeDict(bitDict);
			
			int index = binNumber.length - 1;
			
			List<Long> values = new ArrayList<Long>();
			values.add(actualValue);
			
			for(int bit = 0; bit < binNumber.length; bit++) {
				bitDict.put(index, binNumber[bit]);
				
				index -= 1;				
			}
			
			for(int i = 0; i < swaps; i++) {
				String[] swap = br.readLine().split(" ");
				
				if(bitDict.get(Integer.valueOf(swap[0])) == bitDict.get(Integer.valueOf(swap[1]))) {
					continue;				
				}
				
				else {
					if(bitDict.get(Integer.valueOf(swap[1])) == '1') {
						actualValue = (long) (actualValue + Math.pow(2, Integer.valueOf(swap[0])));
						actualValue = (long) (actualValue - Math.pow(2, Integer.valueOf(swap[1])));						
					}
					else {
						actualValue = (long) (actualValue -  Math.pow(2, Integer.valueOf(swap[0])));
						actualValue = (long) (actualValue + Math.pow(2, Integer.valueOf(swap[1])));
						
					}
					
					char temp = bitDict.get(Integer.valueOf(swap[0]));
					bitDict.replace(Integer.valueOf(swap[0]), bitDict.get(Integer.valueOf(swap[1])));
					bitDict.replace(Integer.valueOf(swap[1]), temp);
					
					values.add(actualValue);
					
				}				
				
			}
			double res = actualValue;
			double max = Collections.max(values);
			double min = Collections.min(values);
			System.out.printf("%.0f %.0f %.0f%n", res, max, min);
			
			
		}
			
	}
	
	static void initializeDict(Map<Integer, Character> dict) {
		for(int i = 0; i < 32; i++) {			
			dict.put(i, '0');			
		}
		
	}
}

