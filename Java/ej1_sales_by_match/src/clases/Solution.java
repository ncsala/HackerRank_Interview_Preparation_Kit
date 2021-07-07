
package clases;

import java.util.*;


/**
 * There is a large pile of socks that must be paired by color. Given an array of
 * integers representing the color of each sock, determine how many pairs of socks 
 * with matching colors there are.
 * 
 * has the following parameter(s):
 * - int n: the number of socks in the pile
 * - int ar[n]: the colors of each sock
 */

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here.  */
        Scanner entry = new Scanner(System.in);
        int[] freq = new int[101];
        int n = entry.nextInt();
        for(int r = 0; r < n; r++){
            int x = entry.nextInt();
            freq[x]++;
        }
        int total = 0;
        for(int r = 1; r < 101; r++){
            total+=freq[r]/2;
        }
        System.out.println(total);
    }
}


/**
 * Solucion que te brinda HackerRank *
 * 
 * class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        HashMap<Integer, Integer> colors = new HashMap<Integer, Integer>();
        
        while(n-- > 0) {
            int c = scan.nextInt();
            Integer frequency = colors.get(c);
            
            // If new color, add to map
            if(frequency == null) {
                colors.put(c, 1);
            }
            else { // Increment frequency of existing color
                colors.put(c, frequency + 1);
            }
        }
        scan.close();
        
        // Count and print the number of pairs
        int pairs = 0;
        for(Integer frequency : colors.values()) {
            pairs += frequency >> 1;
        }
        System.out.println(pairs);
    }
}
 */