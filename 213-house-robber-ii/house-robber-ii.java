import java.util.Arrays;

class Solution {
    int[] dp;
    public int f(int i, int[] arr){
        if (i==arr.length) return dp[i-1];
        if (dp[i] != 0) return dp[i];
        dp[i] = Math.max(dp[i-2]+arr[i], dp[i-1]);
        return f(i+1, arr);
    }
    public int rob(int[] nums) {
        //Base cases
        if(nums.length == 1) return nums[0];
        if(nums.length == 2) return Math.max(nums[0], nums[1]);

        dp = new int[nums.length - 1];
        int[] arr1 = Arrays.copyOfRange(nums, 0, nums.length - 1);
        dp[0] = arr1[0];
        dp[1] = Math.max(arr1[0], arr1[1]);
        int res1 = f(2, arr1);
        dp = new int[nums.length - 1];
        int[] arr2 = Arrays.copyOfRange(nums, 1, nums.length);
        dp[0] = arr2[0];
        dp[1] = Math.max(arr2[0], arr2[1]);
        int res2 = f(2, arr2);
        return Math.max(res1, res2);
    }
}