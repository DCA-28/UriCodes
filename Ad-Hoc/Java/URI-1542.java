import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(ir);
		
		while(true) {
			
			try {
			
			String[] entry = br.readLine().split(" ");		
			
			int q, d, p;
			q = Integer.valueOf(entry[0]);
			d = Integer.valueOf(entry[1]);
			p = Integer.valueOf(entry[2]);
			
			float pagsDifference = p - q;
			float daysDifference = p * d;
			
			float days = daysDifference / pagsDifference;
			int totalPages = (int) (days * q);
			
			if (Math.abs(totalPages) > 1){
				System.out.printf("%d paginas\n", totalPages);
				
			}
			
			else {
				System.out.printf("%d pagina\n", totalPages);
				
			}
			
			
		}
			
		catch(ArrayIndexOutOfBoundsException e) {
			break;
		
		}
			
	}

  }
	
}
