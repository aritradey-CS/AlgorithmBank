# Two Pointers Moving Towards Each Other:
# In this scenario, one pointer starts from the beginning of an array, while the other pointer starts from the end of the array. They move towards each other until they meet or cross each other.

def find_target_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

# Example usage
nums = [2, 4, 7, 11, 15]
target = 9

result = find_target_sum(nums, target)
if result:
    print(f"Indices: {result[0]} and {result[1]}")
    print(f"Values: {nums[result[0]]} and {nums[result[1]]}")
else:
    print("No pair found")
