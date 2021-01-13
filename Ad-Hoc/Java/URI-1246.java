import java.io.BufferedReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while(true) {
			String readLine = br.readLine();
			
			if(readLine == null) break;
			
			String[] entry = readLine.split(" ");
			
			int size = Integer.valueOf(entry[0]);
			int operations = Integer.valueOf(entry[1]);
			
			Parking parking = new Parking(size);		
			Map<String, Integer[]> parkingMap = new HashMap<String, Integer[]>();
			
			int balance = 0;
			
			for(int i = 0; i < operations; i++) {
				String[] data = br.readLine().split(" ");
				
				String status;
				String carPalate;
				int carSize;
				
				if(data.length == 3) {
					
					status = data[0];
					carPalate = data[1];
					carSize = Integer.parseInt(data[2]);
					
					StringBuilder strBuilder = new StringBuilder();
					for(int j = 0; j < carSize; j++) {
						strBuilder.append('-');
					}
					
					String parkSpace = new String(strBuilder);					
					int beginning = parking.getSize().indexOf(parkSpace);
					
					if(beginning != -1) {
						parking.occupyParking(parkSpace, beginning);
						
						parkingMap.put(carPalate, new Integer[] {beginning, beginning + carSize});
						
						balance += 10;
						
					}				
					
				}
				
				else{
					status = data[0];
					carPalate = data[1];
					
					int initial = parkingMap.get(carPalate)[0];
					int end = parkingMap.get(carPalate)[1];
					
					parking.vacateSpace(initial, end);
					
					parkingMap.remove(carPalate);
					
				}
				
			}
			
			System.out.println(balance);
			
			
		}

	}
	
	static class Parking{
		
		private StringBuilder size = new StringBuilder();	
		
		public Parking(int spaces) {
			for (int i = 0; i < spaces; i++) {
				size.append('-');
				
			}
			
		}
		
		public StringBuilder getSize() {
			
			return size;
		}
		
		public void occupyParking(String spaceToPark, int beginning) {
			
			StringBuilder toPark = new StringBuilder();
			
			for(int i = 0; i < spaceToPark.length(); i++) {
				toPark.append("*");		
			}
			
			String car = new String(toPark);
			
			size.replace(beginning, beginning + car.length(), car);
			
		}
		
		public void vacateSpace(int beginning, int end) {
			
			int carSize = end - beginning;
			
			StringBuilder toRelease = new StringBuilder();
			
			for(int i = 0; i < carSize; i++) {
				toRelease.append("-");		
			}
			
			String freeSpace = new String(toRelease);
			
			size.replace(beginning, end, freeSpace);
			
		}
		
	}
}
