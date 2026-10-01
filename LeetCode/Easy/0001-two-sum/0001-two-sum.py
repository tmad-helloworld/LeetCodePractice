class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        result = []
        counter = 0
        for n in nums:
            if f"{(target-n)}" in seen:
                result.append(seen[f"{target-n}"])
                result.append(counter)

            else:
                seen[f"{n}"] = counter
            counter += 1
                
        return result
            
        