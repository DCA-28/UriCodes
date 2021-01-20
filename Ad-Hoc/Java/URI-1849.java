import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(ir);
		
		String[] sizes = br.readLine().split(" ");
		double finalSquare = 0;		
		int h1, b1, h2, b2;
		
		if(Integer.valueOf(sizes[0]) > Integer.valueOf(sizes[1])) {
			h1 = Integer.valueOf(sizes[0]);
			b1 = Integer.valueOf(sizes[1]);
			
		}
		
		else {
			h1 = Integer.valueOf(sizes[1]);
			b1 = Integer.valueOf(sizes[0]);
			
		}
		
		if(Integer.valueOf(sizes[2]) > Integer.valueOf(sizes[3])) {
			h2 = Integer.valueOf(sizes[2]);
			b2 = Integer.valueOf(sizes[3]);
			
		}
		
		else {
			h2 = Integer.valueOf(sizes[3]);
			b2 = Integer.valueOf(sizes[2]);
			
		}	
		
		int limitingHeight = Math.min(h1, h2);
		int basesSum = b1 + b2;		
		int biggestCommon = Math.min(limitingHeight, basesSum);
		
		finalSquare = Math.pow(biggestCommon, 2);
		
		if(h2 > h1 && b2 > b1) {
			double possibleSquare = Math.pow(Math.min(h2, b2), 2);
			finalSquare = Math.max(possibleSquare, finalSquare);
		}
		else if(h1 > h2 && b1 > b2) {
			double possibleSquare = Math.pow(Math.min(h1, b1), 2);
			finalSquare = Math.max(possibleSquare, finalSquare);
		}
		
		System.out.printf("%.0f%n", finalSquare);

	}

}
