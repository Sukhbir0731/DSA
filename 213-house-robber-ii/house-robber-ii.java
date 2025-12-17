import java.util.Arrays;

class Solution {
    // no global initializations
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);
        int[] arr1 = Arrays.copyOfRange(nums, 0, n - 1);
        int[] arr2 = Arrays.copyOfRange(nums, 1, n);
        return Math.max(memoizedSolve(arr1), memoizedSolve(arr2));
    }
    private int memoizedSolve(int[] arr) {
        int[] dp = new int[arr.length];
        Arrays.fill(dp, -1); // Fill with -1 to distinguish from a 0 result
        return f(arr.length - 1, arr, dp);
    }
    private int f(int i, int[] arr, int[] dp) {
        if (i < 0) return 0;
        if (i == 0) return arr[0];
        if (dp[i] != -1) return dp[i];
        int rob = arr[i] + f(i - 2, arr, dp);
        int skip = f(i - 1, arr, dp);
        return dp[i] = Math.max(rob, skip);
    }
}
