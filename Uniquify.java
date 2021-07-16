import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
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
		
		//read every line of the file
		while (scan.hasNext()) {
			//add every line from the file to our string to be handled
			uneditedListString = 
					uneditedListString.concat(scan.nextLine() + "\n");
			
			//comment this out to see what lines are being handled
//			System.out.println(scan.nextLine());
		
		}
		//strore the string in a string array every new line means new entry
		String[] uneditedList = uneditedListString.split("\n");
		
		
		
		//new edited array will go here
//		ArrayList<String> editedList = new ArrayList<String>();
		
		
//		String[] editedList = new String[0]; 
		//make it into hashset that does not allow duplicates then swithc back
		String[] editedList = new HashSet<String>(Arrays.asList(uneditedList)).toArray(new String[0]);
		
		for (int i = 0; i < editedList.length; i++ ) {
						
			//editedList.add(uneditedList[i]);
			System.out.println(editedList[i]);
		}
		
		//this is where the finished file will write to
		FileWriter writer = new FileWriter
					("C:/Users/ndenk/Documents/Green2.txt");
				
		for (int i = 0; i < editedList.length; i++) {
			//writed every item to the new file seperated by comma except the last
			if (i != editedList.length-1) {
			//editedList.add(uneditedList[i]);
				writer.write(editedList[i]+=",");
			}
			else {
				writer.write(editedList[i]);
			}
		}

		writer.close();
	}

}
