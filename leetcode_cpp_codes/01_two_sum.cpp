#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
 public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> indices;
    for (int i = 0; i < nums.size(); i++) {
      if (indices.find(target - nums[i]) != indices.end()) {
        return {indices[target - nums[i]], i};
      }
      indices[nums[i]] = i;
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
