import java.util.Arrays;

class Solution {
    // iterative approach
    // no global initializations
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);
        int[] arr1 = Arrays.copyOfRange(nums, 0, n - 1);
        int[] dp1 = new int[arr1.length];
        int[] arr2 = Arrays.copyOfRange(nums, 1, n);
        int[] dp2 = new int[arr2.length];
        return Math.max(f(arr1, dp1), f(arr2, dp2));
    }
    private int f(int[] arr, int[] dp) {
        dp[0] = arr[0];
        dp[1] = Math.max(arr[0], arr[1]);
        for(int i=2; i<arr.length; i++){
            dp[i] = Math.max(dp[i-2]+arr[i], dp[i-1]);
        }
        return dp[arr.length-1];
    }
}
