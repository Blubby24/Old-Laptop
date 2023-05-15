import java.util.Scanner;


public class Main
{
    public Main(){

    }
    public static void main(String[] args) {
        System.out.println("What number do you wish me to magic");
        Scanner s = new Scanner(System.in);
        int Input = s.nextInt(); 
        System.out.println(Convert(Input, ""));
        s.close();
    }
    public static String Reverse(String s){
        char ch = ' ';
        String nstr = "";
    for (int i=0; i<s.length(); i++)
      {
        ch = s.charAt(i); 
        nstr= ch+nstr; 
    }
      return nstr;
    }
    public static String Convert(int i, String s)
    {
        if(i == 1){
            s += "1";
            return Reverse(s);
        }
        if(i == 0){
            s += "0";
            return s;
        }
        if (i%2 == 0){
            s += "0";
            i = i/2;
            return Convert(i, s);
        }
        i = i/2;
        s += "1";
        return Convert(i,s);
    }
    
}

  