import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;

public class Main {

	public static void main(String[] args) throws IOException{
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(ir);
		
		GoalSort goalSort = new GoalSort();
		VictorySort victorySort = new VictorySort();
		PointSort pointSort = new PointSort();
		
		int cases = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < cases; i++) {
			String[] entry = br.readLine().split(" ");
			int teamsNumber = Integer.valueOf(entry[0]);
			int matches = Integer.valueOf(entry[1]);
			
			LinkedHashMap<String, Team> teamsDict = new LinkedHashMap<String, Team>();
			
			for(int j = 0; j < teamsNumber; j++) {
				String team = br.readLine();
				teamsDict.put(team, new Team(team));
							
			}
			
			
			for(int k = 0; k < matches; k++) {
				String[] matchData = br.readLine().split(" ");
				if(Integer.valueOf(matchData[0]) == Integer.valueOf(matchData[2])) {
					teamsDict.get(matchData[1]).setPoints(1);
					teamsDict.get(matchData[3]).setPoints(1);
					
					teamsDict.get(matchData[1]).setGolas(Integer.parseInt(matchData[0]));
					teamsDict.get(matchData[3]).setGolas(Integer.parseInt(matchData[2]));
					
				}
			
				else if(Integer.valueOf(matchData[0]) > Integer.valueOf(matchData[2])) {
					teamsDict.get(matchData[1]).setPoints(3);
					teamsDict.get(matchData[1]).setVictorys(1);
					
					teamsDict.get(matchData[1]).setGolas(Integer.parseInt(matchData[0]));
					teamsDict.get(matchData[3]).setGolas(Integer.parseInt(matchData[2]));
				}
				
				else {
					teamsDict.get(matchData[3]).setPoints(3);
					teamsDict.get(matchData[3]).setVictorys(1);
					
					teamsDict.get(matchData[1]).setGolas(Integer.parseInt(matchData[0]));
					teamsDict.get(matchData[3]).setGolas(Integer.parseInt(matchData[2]));
					
				}
				
			}
			
			List<Team> teamsList = new ArrayList<Team>(teamsDict.values());
					
			Collections.sort(teamsList, goalSort);
			Collections.sort(teamsList, victorySort);
			Collections.sort(teamsList, pointSort);
					
			for(Team team: teamsList) {
				System.out.println(team);
			}
			
			
		}

	}
	
	static class Team{
		String name;
		int points, victorys, goals;
		
		public Team(String name) {
			this.name = name;
			this.points = 0;
			this.victorys = 0;
			this.goals = 0;
			
		}
		
		public void setPoints(int points) {
			this.points += points;
		}
		public void setVictorys(int victorys) {
			this.victorys += victorys;
		}
		public void setGolas(int goals) {
			this.goals += goals;
		}
		
		public int getPoints() {
			return points;
		}
		public int getGoals() {
			return goals;
		}
		public int getVictorys() {
			return victorys;
		}
		
		public String toString() {
			return String.format("%s", name);
		}
		
		public String stats() {
			return String.format("%s -> Points: %d, Victorys: %d, Goals: %d", name, points,
					victorys, goals);
		}
		
	}
		
	
	static class GoalSort implements Comparator<Team>{
		public int compare(Team a, Team b) {
			if(a.getGoals() > b.getGoals()) {
				return -1;
			}
			else if(a.getGoals() == b.getGoals()) {
				return 0;
			}
			else {
				return 1;
			}
		}
	}
	
	static class VictorySort implements Comparator<Team>{
		public int compare(Team a, Team b) {
			if(a.getVictorys() > b.getVictorys()) {
				return -1;
			}
			else if(a.getVictorys() == b.getVictorys()) {
				return 0;
			}
			else {
				return 1;
			}
			
		}
	}
	
	static class PointSort implements Comparator<Team>{
		public int compare(Team a, Team b) {
			if(a.getPoints() > b.getPoints()) {
				return -1;
			}
			else if(a.getPoints() == b.getPoints()) {
				return 0;
			}
			else {
				return 1;
			}
		}
	}

}
