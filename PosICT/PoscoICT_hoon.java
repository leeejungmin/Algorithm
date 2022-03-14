import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class PoscoICT {
	public static void main(String[] args){
		BufferedReader 					reader 		= new BufferedReader(new InputStreamReader(System.in));
		int 							personCnt 	= Integer.parseInt(reader.readLine());
		int 							voterCnt 	= 0;
		ArrayList<Person> 				persons 	= new ArrayList<Person>(); 
		ArrayList<ArrayList<Integer>> 	votes 		= new ArrayList<>();
		
		for (int i = 0; i < personCnt; i++) {
			String person = reader.readLine();
			persons.add(new Person(i, person));
		}
		
		String input = "";
		while((input = reader.readLine()) != null && !input.isEmpty()) {
			voterCnt++;
			
			ArrayList<Integer> 	vote = new ArrayList<>();
			String[] 			line = input.split(" ");
			
			for (int i = 0; i < line.length; i++) {
				vote.add(Integer.parseInt(line[i]));
			}
			
			votes.add(vote);
		}
		
		int 				depth 		= 0;
		ArrayList<Person> 	deadPerson 	= new ArrayList<>();
		
		while (!isFinished(persons, voterCnt)) {
			calcVote(persons, votes, depth, deadPerson);
			deadPerson = setResult(persons);
			depth++;
		}
		
		printFinisher(persons);
	}
	
	public static class Person {
		int 	index;
		String 	name;
		boolean isAlive = true;
		int 	voteCnt = 0;
		
		public Person(int index, String name) {
			this.index 	= index;
			this.name 	= name;
		}
		
		public void printPerson() {
			System.out.println(index + " " + name);
			System.out.println("status : " + isAlive);
			System.out.println("vote   : " + voteCnt);
			System.out.println();
		}
	}
	
	public static boolean isFinished(ArrayList<Person> persons, int voterCnt) {
		for(Person person : persons) {
			if (person.isAlive && person.voteCnt > (voterCnt / 2)) {
				return true;
			}
		}
		
		return false;
	}
	
	public static void calcVote(
				ArrayList<Person> 				persons
			, 	ArrayList<ArrayList<Integer>> 	votes
			, 	int 							depth
			, 	ArrayList<Person> 				deadPerson
	) {
		for (int i = 0; i < votes.size(); i++) {
			int targetVote = votes.get(i).get(depth) - 1;
			
			//두번째 투표
			if (depth != 0) {
				int 	beforeVote 	= votes.get(i).get(depth - 1) - 1;
				boolean isContinued = false;
				
				for (Person person : deadPerson) {
					if (person.index == beforeVote) {
						isContinued = true;
					}
				}
				
				if (!isContinued) {
					continue;
				}
			}
			
			Person targetPerson = persons.get(targetVote);
			//vote counting
			if (targetPerson.isAlive) {
				targetPerson.voteCnt++;
			}
		}
	}
	//Make list Deadperson 
	public static ArrayList<Person> setResult(ArrayList<Person> persons) {
		int 				maxVote 	= -1;
		int 				minVote 	= 1000;
		ArrayList<Person> 	deadPerson 	= new arrayList<>(); 
		
		for (Person person : persons) {
			if (person.isAlive) {
				if (person.voteCnt > maxVote) {
					maxVote = person.voteCnt;
				} else if (person.voteCnt < minVote) {
					minVote = person.voteCnt;
				}
			}
		}-          
		
		for (Person person : persons) {
			if (person.isAlive &&
				person.voteCnt != maxVote &&
				person.voteCnt == minVote
			) {
				person.isAlive = false;
				deadPerson.add(person);
			}
		}
		
		return deadPerson;
	}
	
	public static void printFinisher(ArrayList<Person> persons) {
		for (Person person : persons) {
			if (person.isAlive) {
				System.out.println(person.name);
			}
		}
	}
	
	public static void printVotes(ArrayList<ArrayList<Integer>> votes) {
		for (int i = 0 ; i < votes.size(); i++) {
			for (int j = 0 ; j < votes.get(i).size(); j++) {
				System.out.print(votes.get(i).get(j));
			}
			System.out.println();
		}
	}
}