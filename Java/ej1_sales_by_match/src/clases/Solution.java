
package clases;

import java.util.*;

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