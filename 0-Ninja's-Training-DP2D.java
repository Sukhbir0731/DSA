/*
 * Ninja's training

A Ninja has planned a n-day training schedule. Each day he has to perform one of three activities 
- running, stealth training, or fighting practice. The same activity cannot be done on two consecutive days and the ninja earns 
a specific number of merit points, based on the activity and the given day.
Given a n x 3-sized matrix, where matrix[i][0], matrix[i][1], and matrix[i][2], represent the merit points associated with running, 
stealth and fighting practice, on the (i+1)th day respectively. Return the maximum possible merit points that the ninja can earn.

Example 1
Input: matrix = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
Output: 210
Explanation:
Day 1: fighting practice = 70
Day 2: stealth training = 50
Day 3: fighting practice = 90
Total = 70 + 50 + 90 = 210
This gives the optimal points.

Example 2
Input: matrix = [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
Output: 290
Explanation:
Day 1: running = 70
Day 2: stealth training = 20
Day 3: running = 200
Total = 70 + 20 + 200 = 290
This gives the optimal points.
*/



// This is a Recursive DP/Top down solution

import java.util.*;
public class Dp2DExercise {
	
	private static int f(int day, int last, int[][] matrix, int[][] dp) {
		if(day == 0) {
			int maxi = 0;
			for(int i=0; i<=2; i++) {
				if(i!=last) maxi = Math.max(maxi, matrix[0][i]);
			}
			return maxi;
		}
		if(dp[day][last]!=-1) return dp[day][last];
		int maxi = 0;
		for(int i=0; i<=2; i++) {
			if(i!=last) {
				int points = matrix[day][i] + f(day-1, i, matrix, dp);
				maxi = Math.max(maxi, points);
			}
		}
		return dp[day][last] = maxi;
	}
	
    private static int ninjaTraining(int[][] matrix) {
    	int n = matrix.length;
    	int[][] dp= new int[matrix.length][matrix[0].length+1];
        for (int i = 0; i < n; i++)
            Arrays.fill(dp[i], -1);
    	return f(matrix.length-1, 3, matrix, dp);
    }
	
	public static void main(String[]args) {
		int[][] matrix = {{20,10,10}, {20,10,10}, {20,30,10}};
		System.out.println(ninjaTraining(matrix));
	}
}
