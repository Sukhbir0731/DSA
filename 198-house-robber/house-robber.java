// iterative approach with better space complexity
class Solution {
    // int[] dp;
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        // dp = new int[nums.length];
        // Arrays.fill(dp, -1);
        int a = nums[0];
        int b = Math.max(nums[1], nums[0]);
        if (nums.length == 2) return b;
        for(int i=2; i<nums.length; i++){
            // dp[i] = Math.max(nums[i]+dp[i-2], dp[i-1]);
            int temp = b;
            b = Math.max(nums[i]+a, b);
            a = temp;
        }
        return b;
    }
}