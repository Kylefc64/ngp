import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
//this will take a file path as input , go through each line 
//and write every new line seperation as a comma instead
public class Uniquify {
	public static void main (String[] args) throws IOException {
		if (args.length != 1) {
			System.out.println("Expected input directory as first argument.");
			return;
		}
		File directory = new File(args[0]);
		HashSet<String> phrases = new HashSet<>();
		for (File file : directory.listFiles()) {
			if (!file.getName().endsWith(".txt"))
				continue;
			Scanner scan = new Scanner(file);
			while (scan.hasNext()) {
				phrases.add(scan.nextLine().trim().toLowerCase());
			}
		}
		FileWriter writer = new FileWriter("skribblio.txt");
		for (String phrase : phrases) {
			writer.write(phrase + ",");
		}
		writer.close();
	}
}
