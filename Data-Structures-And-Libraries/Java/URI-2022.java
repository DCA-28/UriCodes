import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;

public class Main {

	public static void main(String[] args) throws IOException, FileNotFoundException{
		Locale.setDefault(Locale.US);
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(ir);
		Checker comparator = new Checker();
		
		while(br.ready()) {
			
			String[] entry = br.readLine().split(" ");
			String owner = entry[0];
			int gifts = Integer.valueOf(entry[1]);
			
			List<Gift> giftList = new ArrayList<Gift>();
			
			for(int i = 0; i < gifts; i++) {
				
				String name = br.readLine();
				
				String[] data = br.readLine().split(" ");
				float price = Float.valueOf(data[0]);
				int priority = Integer.valueOf(data[1]);
				
				giftList.add(new Gift(name, price, priority));
								
			}
			
			/* Sorting the list with the custom Comparator */
			
			Collections.sort(giftList, comparator);
			
			System.out.printf("Lista de %s%n", owner);
			
			for(Gift gift : giftList) {
				
				System.out.println(gift);
				
			}
			
			System.out.println();
			
		}

	}
	
	static class Gift{
		
		private String name;
		private float price;
		private int priority;
		
		public Gift(String name, float price, int priority) {			
			this.name = name;
			this.price = price;
			this.priority = priority;			
		}

		public String getName() {
			return name;
		}

		public float getPrice() {
			return price;
		}

		public Integer getPriority() {
			return priority;
		}
		
		public String toString() {
			return String.format("%s - R$%.2f", name, price);
		}

	}
	
	static class Checker implements Comparator<Gift>{
		@Override
		public int compare(Gift a, Gift b) {
			if(a.getPriority() == b.getPriority() && a.getPrice() == b.getPrice()) {
				return a.getName().compareTo(b.getName());			
			}
			
			else if(a.getPriority() == b.getPriority()) {
				return Float.compare(a.getPrice(), b.getPrice());
			}
			
			else {
				if(a.getPriority() > b.getPriority()) {
					return -1;
				}
				else {
					return 1;
				}
			}
		}
		
	}
}
