class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        result = []
        counter = 0
        for i in nums:
            if f"{target-i}" in seen:
                result.append(seen[f"{target-i}"])
                result.append(counter)

            else:
                seen[f"{i}"] = counter

            counter += 1

        return result