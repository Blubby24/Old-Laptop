import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;


public class LetterBox {
    private int x, y, w, h;
    private char c;
    private Color color;

    public LetterBox(){
        x = 20;
        y = 0;
        w = 0;
        h = 0;
        c = 'b';
        color = new Color(0,0,0);
    }
    
    public LetterBox(int vx, int vy, int vw, int vh, char vc, Color vcolor){

        x = vx;
        y = vy;
        w = vw;
        h = vh;
        c = vc;
        color = vcolor;

    }
    public int getX(){
        return x;
    }
    public void setX(int vx){
        x = vx;
    }
    public int getY(){
        return y;
    }
    public void setY(int vx){
        y = vx;
    }
    public int getH(){
        return h;
    }
    public void setH(int vx){
        h = vx;
    }
    public int getW(){
        return w;
    }
    public void setW(int vx){
        w = vx;
    }
    public char getC(){
        return c;
    }
    public void setC(char vx){
        c = vx;
    }
    public Color getColor(){
        return color;
    }
    public void setColor(Color vx){
        color = vx;
    }
    public void DrawSquare(Graphics g2d){
        g2d.setColor(color);
        g2d.fillRect(x, y, w, h);
        g2d.setColor(Color.BLACK);
        String s = String.valueOf(c);
        g2d.setFont(new Font("Times New Roman", Font.BOLD, 25));
        g2d.drawString(s, x + (w/2) -10, y + (h/2) + 10);
        //System.out.println(x);
    }

}
