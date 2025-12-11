// Recursive approach
class Solution {
    int dp[];
    public int f(int n){
        if (n <= 2){
            return n;
        }
        if (dp[n] != -1){
            return dp[n];
        }
        dp[n] = f(n-1) + f(n-2);
        return dp[n];
    }
    public int climbStairs(int n) {
        dp = new int[n + 1];
        Arrays.fill(dp, -1);
        return f(n);
    }
}