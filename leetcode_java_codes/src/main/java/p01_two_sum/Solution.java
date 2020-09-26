package p01_two_sum;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        // 存储内容：当前元素的差值和下标
        Map<Integer, Integer> map = new HashMap<>();
        int len = nums.length;
        for (int i = 0; i < len; i++) {
            if (map.containsKey(nums[i])) {
                int index = map.get(nums[i]);
                return new int[]{index, i};
            } else {
                map.put(target - nums[i], i);
            }
        }
        return new int[2];
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(Arrays.toString(
                s.twoSum(new int[]{2, 7, 11, 15}, 9)
        ));
    }
}