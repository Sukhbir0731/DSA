class Solution {
    int[] nums;
    int[] dp;
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        this.nums = nums;
        dp = new int[nums.length];
        Arrays.fill(dp, -1);

        dp[0] = nums[0];
        dp[1] = Math.max(nums[1], nums[0]);
        return f(2);
    }
    public int f(int i){
        if (i >= nums.length) return dp[nums.length - 1];
        if (dp[i] == -1) dp[i] = Math.max(dp[i-2]+nums[i], dp[i-1]);
        return f(i+1);
    }
}