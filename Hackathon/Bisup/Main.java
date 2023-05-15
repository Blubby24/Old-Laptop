import java.util.ArrayList;
import java.util.Scanner;

public class Main{
    private static int boardw, boardh;
    private static int bisx, bisy;
    public Main(){
        bisx = 5;
        bisy = 5;
        boardh = 8;
        boardw = 8;
    }
    public static void main(String[] args) {

        removeStuff(possible_moves(0, 0, 3, 1));
        removeStuff(possible_moves(1, 0, 3, 1));

    }
    public static ArrayList<int[]> possible_moves(int bisx,int bisy,int boardh,int boardw){
        ArrayList<int[]> possible_moves = new ArrayList<int[]>();
        int j = bisy - 1;
        for(int i = bisx-1; i > 0; i--){
           if(j >= 0){
                int move[] = new int[2];
                move[0] = i;
                move[1] = j;
                //System.out.println(move[0]);
                //System.out.println(bisx);
                possible_moves.add(0, move);
           }
            j -= 1;

        }
        j = bisy -1;
        for(int i = bisx+1; i < boardw; i++){
           if(j >= 0){
                int move[] = new int[2];
                move[0] = i;
                move[1] = j;
                //System.out.println(move[0]);
                //System.out.println(bisx);
                possible_moves.add(0, move);
           }
            j -= 1;

        }
        j = bisy +1;
        for(int i = bisx-1; i > 0; i--){
           if(j <= boardh){
                int move[] = new int[2];
                move[0] = i;
                move[1] = j;
                //System.out.println(move[0]);
                //System.out.println(bisx);
                possible_moves.add(0, move);
           }
            j += 1;

        }
        j = bisy +1;
        for(int i = bisx+1; i < boardw; i++){
           if(j <= boardh){
                int move[] = new int[2];
                move[0] = i;
                move[1] = j;
                System.out.println(move[0]);
                //System.out.println(bisx);
                possible_moves.add(0, move);
           }
            j += 1;

        }
        System.out.println(possible_moves.size());
        return possible_moves;
    }
    public static ArrayList<int[]> removeStuff(ArrayList <int[]> possible_moves){
        ArrayList<int[]> newMoves = new ArrayList<int[]>();
        int failed = 0;
        for(int[] m: possible_moves){
            failed = 0;
            for(int[] mo: possible_moves){
                if(mo[0] == m[0] && mo[1] == m[1]){
                    System.out.println(mo[1]);
                    System.out.println(m[1]);
                    failed += 1;
                }
                
                
                }
                if(failed == 2){
                }
                else{
                    newMoves.add(0, m);
                }
            
            }
            System.out.println(newMoves.size());
            return newMoves;
        }
    
    public static void read(){
        
    }
    
}