import java.util.Arrays;

class Solution {
    // iterative approach - space optimized
    // no global initializations
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);
        int[] arr1 = Arrays.copyOfRange(nums, 0, n - 1);
        int[] arr2 = Arrays.copyOfRange(nums, 1, n);
        return Math.max(f(arr1), f(arr2));
    }
    private int f(int[] arr) {
        int a = arr[0];
        int b = Math.max(arr[0], arr[1]);
        for(int i=2; i<arr.length; i++){
            int temp = b;
            b = Math.max(a+arr[i], b);
            a = temp; 
        }
        return b;
    }
}
