import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		Map<String, String> languages = new HashMap<String, String>(){{
			put("brasil", "Feliz Natal!");
			put("alemanha", "Frohliche Weihnachten!");
			put("austria", "Frohe Weihnacht!");
			put("coreia", "Chuk Sung Tan!");
			put("espanha", "Feliz Navidad!");
			put("grecia", "Kala Christougena!");
			put("estados-unidos", "Merry Christmas!");
			put("inglaterra", "Merry Christmas!");
			put("australia", "Merry Christmas!");
			put("portugal", "Feliz Natal!");
			put("suecia", "God Jul!");
			put("turquia", "Mutlu Noeller");
			put("argentina", "Feliz Navidad!");
			put("chile", "Feliz Navidad!");
			put("mexico", "Feliz Navidad!");
			put("antardida", "Merry Christmas!");
			put("canada", "Merry Christmas!");
			put("irlanda", "Nollaig Shona Dhuit!");
			put("belgica", "Zalig Kerstfeest!");
			put("italia", "Buon Natale!");
			put("libia", "Buon Natale!");
			put("siria", "Milad Mubarak!");
			put("marrocos", "Milad Mubarak!");
			put("japao", "Merii Kurisumasu!");
		}};
		
		while(sc.hasNext()) {
			String entry = sc.next();
			
			if(languages.get(entry) != null) System.out.println(languages.get(entry));
			
			else System.out.println("--- NOT FOUND ---");
			
		}
				
	  }

	}
