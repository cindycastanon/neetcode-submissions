class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}

        for i, num in enumerate(numbers):
            needed = target - num

            if needed in mp:
                return [mp[needed], i + 1]

            mp[num] = i + 1  