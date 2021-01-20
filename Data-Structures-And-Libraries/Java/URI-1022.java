import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException{
		InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
       
        int cases = Integer.parseInt(br.readLine());
        
        int N1, D1, N2, D2;
        
        for(int i = 0; i < cases; i++) {
            String[] elements = br.readLine().split(" ");
            N1 = Integer.valueOf(elements[0]);
            D1 = Integer.valueOf(elements[2]);
            N2 = Integer.valueOf(elements[4]);
            D2 = Integer.valueOf(elements[6]);
            
            String operation = elements[3];
            
            int[] numbers = fractionValue(N1, D1, N2, D2, operation);
            
            BigInteger b1 = BigInteger.valueOf(numbers[0]);
            BigInteger b2 = BigInteger.valueOf(numbers[1]);
            BigInteger gcd = b1.gcd(b2);
            
            int commonDivisor = gcd.intValue();
            
            if(commonDivisor != 1) {
                    int simplified1 = (int) numbers[0] / commonDivisor;
                    int simplified2 = (int) numbers[1] / commonDivisor;
                    
                    System.out.println(String.format("%d/%d = %d/%d", numbers[0], numbers[1],
                                    simplified1, simplified2));
                    
            }
            
            else {
                    System.out.println(String.format("%d/%d = %d/%d", numbers[0], numbers[1],
                                    numbers[0], numbers[1]));
                    
            }
            
        }
    }
           	
	
	static int[] fractionValue(int N1, int D1, int N2, int D2, String operation) {
		
		int firstTerm, secondTerm;
		int[] terms = new int[2];
		
		if(operation.equals("+")){
			
			//System.out.println("Addition");
			firstTerm = N1 * D2 + N2 * D1;
			secondTerm = D1 * D2;
		}
		
		else if(operation.equals("-")){
			
			//System.out.println("Subtration");
			firstTerm = N1 * D2 - N2 * D1;
			secondTerm = D1 * D2;
			
		}
		
		else if(operation.equals("*")) {			
			//System.out.println("Multiplication");
			firstTerm = N1 * N2;
			secondTerm = D1 * D2;
			
		}
		
		else {
			//System.out.println("Division");
			firstTerm = N1 * D2;
			secondTerm = N2 * D1;
			
		}
		
		terms[0] = firstTerm;
		terms[1] = secondTerm;
		
		return terms;
		
	} 
	
}
