#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
 public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> my_dict;
    for (int idx = 0; idx < nums.size(); idx++) {
      int curr_value = nums[idx];
      if (my_dict.find(curr_value) != my_dict.end()) {
        return {my_dict[curr_value], idx};
      }
      my_dict[target - curr_value] = idx;
    }
    return {};
  }
};

int main() {
  Solution s = Solution();
  vector<int> nums{2, 7, 11, 15};
  int target = 9;
  vector<int> result = s.twoSum(nums, target);
  for (int value : result) {
    cout << value << endl;
  }
}
