import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int totalPoints;
		int toDraw;
		List<Integer> defeats = new ArrayList<Integer>();
		boolean balance = true;
		
		while(true) {
			totalPoints = 0;
			toDraw = 0;
			defeats.clear();
			balance = true;
			
			String entry = br.readLine();
			if(entry == null) break;
			String[] values = entry.split(" ");
			int matches = Integer.valueOf(values[0]);
			int goalsBalance = Integer.valueOf(values[1]);
			
			for(int i = 0; i < matches; i++) {
				String[] goals = br.readLine().split(" ");
				int goalsScored = Integer.valueOf(goals[0]);
				int goalsConceded = Integer.valueOf(goals[1]);
				
				if(goalsScored > goalsConceded) {
					totalPoints += 3;
				}
				
				else if(goalsScored == goalsConceded){
					if(goalsBalance > 0) {
						totalPoints += 3;
						goalsBalance -= 1;
					}
					else {
						totalPoints += 1;
						balance = false;
						
					}
				}
				
				else if(goalsConceded - goalsScored == 1){
					toDraw += 1;
				}
				
				else {
					defeats.add(goalsConceded - goalsScored);
					
				}
								
			}
			
			Collections.sort(defeats);
			
			if(balance) {
				for(int i = 0; i < toDraw; i++) {
					
					if(goalsBalance >= 2) {
						totalPoints += 3;
						goalsBalance -= 2;					
					}
					else if(goalsBalance == 1) {
						totalPoints += 1;
						goalsBalance -= 1;
						balance = false;
						break;
					}
					else {
						balance = false;
						break;
					}
					
				}
			}
			
			if(balance) {
				for(int difference : defeats) {
					if(goalsBalance >= difference + 1) {
						totalPoints += 3;
						goalsBalance = goalsBalance - (difference + 1);
					}
					
					else if(goalsBalance == difference) {
						totalPoints += 1;
						goalsBalance = goalsBalance - difference;
						balance = false;
						break;						
					}
					
					else {
						balance = false;
						break;
					}
					
				}
				
			}
		
		  System.out.println(totalPoints);
		}
		
	}

}
