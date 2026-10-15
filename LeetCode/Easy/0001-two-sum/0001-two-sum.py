class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        result = []
        counter = 0
        for i in nums:
            if (target-i) in seen:
                result.append(seen[target-i])
                result.append(counter)

            else:
                seen[i] = counter
            counter += 1

        return result
        