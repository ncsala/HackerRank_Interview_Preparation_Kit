
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