import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int cases = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < cases; i++) {
			int digits = Integer.parseInt(br.readLine());
			String[] numbers = br.readLine().split(" ");
			
			Integer[] originalList = new Integer[numbers.length];
			
			int count = 0;
			for(String number : numbers) {
				originalList[count] = Integer.parseInt(number);
				count += 1;
			}
			
			Integer[] sortedList = new Integer[numbers.length];
			
			int count2 = 0;
			for(String number : numbers) {
				sortedList[count2] = Integer.parseInt(number);
				count2 += 1;
			}
			
			Arrays.sort(sortedList);
			int swaps = 0;
			int limit = originalList.length - 1;
			int temp;
						
			while(Arrays.equals(originalList, sortedList) == false) {
				for(int j = 0; j < limit; j++ ) {
					if(originalList[j] > originalList[j+1]) {
						temp = originalList[j+1];
						originalList[j+1] = originalList[j];
						originalList[j] = temp;
						swaps += 1;
					}
					
					else continue;			
				}
				
				limit -= 1;
			}
			
			System.out.printf("Optimal train swapping takes %d swaps.%n", swaps);
						
		}

	}

}
