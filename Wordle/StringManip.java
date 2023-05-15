import java.awt.Color;
import java.awt.List;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class StringManip {

    private String[] LegalWords, PossibleAnswers;
    private String answer;
    
    public StringManip(){
        LegalWords = new String[14855];
        LegalWords = MakeList("valid-wordle-words.txt");
        PossibleAnswers = new String[2315];
        PossibleAnswers = MakeList("wordle-answers-alphabetical.txt");
        Random Dice = new Random(); 
        int n = Dice.nextInt(2315);
        answer = PossibleAnswers[n];
        System.out.println(answer);
    }

    public String[] MakeList(String file){
        try {
            File myObj = new File(file);
            Scanner myReader = new Scanner(myObj);
            int i = 0;
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            LegalWords[i] = data;
            i = i+1;
        }
            myReader.close();
            return LegalWords;
      } catch (FileNotFoundException e) {
        System.out.println("An error occurred.");
        e.printStackTrace();
        return null;
      }
    }
    public String[] getLegalWords(){
        return LegalWords;
    }
    public boolean checkWord(String Guess){
        for(String s: LegalWords){
           
            if(s.contains(Guess)){
                return true;
            }
        }
        System.out.println("Not a real word");
        return false;
    }
    
    public boolean CheckGuess(LetterBox[][] gameBoard, String Guess,int row){
        if(Guess.contains(answer)){
            for(int i = 0; i < 5; i++){
                gameBoard[row][i].setColor(Color.GREEN);
            }
            return true;
        }
        char[] answerLetter = answer.toCharArray();
        int j = 0;
        for(char c: answerLetter){
            for(int i = 0; i < 5; i++){
                if(c == gameBoard[row][i].getC()){
                    if(j==i){
                        gameBoard[row][i].setColor(Color.GREEN);
                        break;
                    }
                    else{
                        gameBoard[row][i].setColor(Color.YELLOW);
                    }
                }
            }
            j += 1;
        }
        return false;
    }
}
