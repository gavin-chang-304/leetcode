class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        res=[]
        print(len(nums))
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1

            while(l<r):
                if l==i:
                    l+=1
                elif r==i:
                    r-=1
                elif(nums[l]+nums[r]==(0-nums[i])):
                    res.append(sorted([nums[l],nums[r],nums[i]]))
                    #print(nums[i])
                    r-=1
                    l+=1
                    while(l<r and nums[l]==nums[l-1]):
                        l+=1
                    while(l<r and nums[r]==nums[r+1]):
                        r-=1
                elif(nums[l]+nums[r]>(0-nums[i])):
                    
                    while(l<r and nums[r]==nums[r-1]):
                        r-=1                    
                    r-=1
                elif(nums[l]+nums[r]<(0-nums[i])):
                    
                    while(l<r and nums[l]==nums[l+1]):
                        l+=1
                    l+=1
                else:
                    print('hi')
                
        #s = set(tuple(a) for a in res)
        #res = [list(b) for b in s]
        return res