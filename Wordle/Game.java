
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
public class Game extends JPanel implements Runnable, KeyListener{
private BufferedImage back;
private LetterBox[][] gameBoard;
private int guessNumR, guessNumC;
private StringManip s;
private boolean win, lose;

public Game() {
    s = new StringManip();
    win = false;
    lose = false;
    new Thread(this).start();
    this.addKeyListener(this);
    guessNumR = 0;
    guessNumC = 0;
    gameBoard = new LetterBox[6][5]; 
    gameBoard = PopArray(); 
    back=null;
}
    public void run() {
    try {
        while(true) {
        Thread.currentThread().sleep(5);
        repaint();
    }
    }
    catch(Exception e) {}
    }
    public LetterBox[][] PopArray(){
        int x = 100;
        int y = 100;
        for(int i = 0; i < 6; i++){
            for(int j = 0; j < 5; j++){
                gameBoard[i][j] = new LetterBox(x, y, 40, 40, ' ', Color.gray);
                x += 50;
            }
            y += 60;
            x = 100;
        }
        return gameBoard;
    }

    public void paint (Graphics g)
    {   
        Graphics2D twoDgraph = (Graphics2D)g;
    if (back==null) {
        back =(BufferedImage) (createImage(getWidth(), getHeight()));
    }
        Graphics g2d = back.createGraphics();
        g2d.clearRect(0, 0, getSize().width, getSize().height);
        //we draw here 
        if(win == true){
            g2d.drawString("You win", 300, 50);
        }
        if(lose == true){
            g2d.drawString("You Lose", 300, 50); 
        }
        for(int i = 0; i < 6; i++){
            for(int j = 0; j < 5; j++){
                gameBoard[i][j].DrawSquare(g2d);   
            }
        }

        twoDgraph.drawImage(back, 0, 0, null);
    }
    @Override
    public void keyPressed(KeyEvent e) {
        // TODO Auto-generated method stub
        if(e.getKeyCode() == 8 && !(guessNumC == 0) && lose == false){
            gameBoard[guessNumR][guessNumC-1].setC(' ');
            guessNumC -= 1;
        }
        else{
            if(!(guessNumC > 4) && !(e.getKeyCode() == 10) && lose == false){
                gameBoard[guessNumR][guessNumC].setC(e.getKeyChar());
                guessNumC += 1;
            }
        }
        System.out.println(e.getKeyCode());
        if(e.getKeyCode() == 10){
            //enter is pressed
            String Guess = "";
            for(int i = 0; i < guessNumC; i++){
                Guess += String.valueOf(gameBoard[guessNumR][i].getC());
            }
            if(guessNumC > 4 && s.checkWord(Guess) == true && lose == false){
                if(s.CheckGuess(gameBoard, Guess, guessNumR) == false){
                    guessNumR += 1;
                    guessNumC = 0;
                    if(guessNumR > 5){
                        lose = true;
                    }
                }
                else{
                    win = true;
                }
            }
            
        }
    }
    @Override
    public void keyReleased(KeyEvent e) {
        // TODO Auto-generated method stub
       
    }
    @Override
    public void keyTyped(KeyEvent e) {
        // TODO Auto-generated method stub
       
    }
}
