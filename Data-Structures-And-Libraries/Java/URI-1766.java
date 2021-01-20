import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException{
	
	Locale.setDefault(Locale.US);
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	Checker checker = new Checker();
	
	int cases = Integer.parseInt(br.readLine());
	int global = 1;
	
	for(int i = 0; i < cases; i++) {
		String[] numbers = br.readLine().split(" ");
		
		int reindeer = Integer.valueOf(numbers[0]);
		int workReindeer = Integer.valueOf(numbers[1]);
		
		List<Reindeer> reindeers = new ArrayList<Reindeer>();
		
		for(int r = 0; r < reindeer; r++) {
			
			String[] reindeerAttributes = br.readLine().split(" ");
			
			reindeers.add(new Reindeer(reindeerAttributes[0], Integer.valueOf(reindeerAttributes[1]),
					Integer.valueOf(reindeerAttributes[2]), Float.valueOf(reindeerAttributes[3])));
			
		}
		
		Collections.sort(reindeers, checker);
		
		System.out.printf("CENARIO {%d}%n", global);
		
		int count = 1;
		
		for(Reindeer rd : reindeers) {
			
			if(count > workReindeer) break;
			
			System.out.println(count + " - " + rd.getName());
			count += 1;
			
		}
		
		global++;
		
	}
	

	}
	
	static class Reindeer{
		
		private String name;
		private int weight;
		private int age;
		private float height;
		
		public Reindeer(String name, int weight, int age, float height) {
			
			this.name = name;
			this.weight = weight;
			this.age = age;
			this.height = height;
			
		}

		public String getName() {
			return name;
		}

		public int getWeight() {
			return weight;
		}

		public int getAge() {
			return age;
		}

		public float getHeight() {
			return height;
		}	
		
	}
	
	static class Checker implements Comparator<Reindeer>{
		
		public int compare(Reindeer a, Reindeer b) {
			
			if(a.getWeight() == b.getWeight()) {
				
				if(a.getAge() == b.getAge()) {
					
					if(a.getHeight() == b.getHeight()) {
						
						return a.getName().compareTo(b.getName());
					}
					
					else {
						
						return Float.compare(a.getHeight(), b.getHeight());				
					}				
				}
				
				else {
					
					return Integer.compare(a.getAge(), b.getAge());
					
				}								
			}
			
			else {
				
				if(a.getWeight() > b.getWeight()) {					
					return -1;					
				}
				
				else {					
					return 1;					
				}
				
			}
			
		}
		
	}

}
