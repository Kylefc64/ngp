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
		//the file we will be deleting duplicates from 
		//File file = new File("/KylesDirectory/folder.txt");
		File file = new File("C:/Users/ndenk/Documents/Green.txt");
		//scanner to read the file
		Scanner scan = new Scanner(file);
		String uneditedListString = "";
		while (scan.hasNext()) {
			//add every line from the file to our string to be handled
			uneditedListString = uneditedListString.concat(scan.nextLine() + "\n");
		}
		//strore the string in a string array, every new line means new entry
		String[] editedList = uneditedListString.split("\n");
		//make it into hashset that does not allow duplicates then swithc back
		editedList = new HashSet<String>(Arrays.asList(editedList)).toArray(new String[0]);
		//this is where the finished file will write to
		FileWriter writer = new FileWriter("C:/Users/ndenk/Documents/Green2.txt");			
		for (int i = 0; i < editedList.length; i++) {
			//writed every item to the new file seperated by comma except the last item
			if (i != editedList.length-1) {
				writer.write(editedList[i]+=",");
			}
			else {
				writer.write(editedList[i]);
			}
		}
		writer.close();
	}
}
