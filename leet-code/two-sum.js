/**  Input: nums = [2,7,11,15], target = 9
 Output: [0,1]
 Output: Because nums[0] + nums[1] == 9, we return [0, 1].
 */

var twoSum = function (nums, target) {

    let result = []
    for (i = 0; i < nums.length; i++) {
        const diff = target - nums[i];
        const index = nums.indexOf(diff);
        if (index !== -1 && index !== i) {
            result.push(index)
            result.push(i);

        }
    }
    return result;
};

console.log(twoSum([3, 2, 3], 6))