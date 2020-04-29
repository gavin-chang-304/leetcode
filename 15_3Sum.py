class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ''' use 2 pointer to find the answer in O(n^2) '''
        
        res = []
        nums.sort()
        lenth = len(nums)
        
        # if lenth < 3, it's impossible to find the answer
        if lenth<3:
            return []
        
        # find the target and do 2 pointers
        for i in range(lenth-2):
            left = i+1
            right = lenth-1
            while(left < right):
                
                # if left + right < target, we have to let left bigger
                if nums[left]+nums[right] < -1*nums[i]:
                    left+=1
                    while left < right and (nums[left] == nums[left-1]):
                        left+=1
                
                # if left + right > target, we have to let right smaller
                elif nums[left]+nums[right] > -1*nums[i]:
                    right-=1
                    while right>left and(nums[right] == nums[right+1]):
                        right-=1
                
                # find answer
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while left < right and (nums[left] == nums[left-1]):
                        left+=1
                    right -= 1
                    while right>left and(nums[right] == nums[right+1]):
                        right-=1
        
        #use set to avoid redundancy
        res = list(set(tuple(sorted(sub)) for sub in res))
        return res