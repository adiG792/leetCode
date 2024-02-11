def threeSum(nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
                if i>0 and nums[i] == nums[i-1]: #skip duplicates
                        continue

                left = i+1
                right = len(nums) - 1

                while left<right:
                        current_sum = nums[i] + nums[left] + nums[right]
                        if current_sum == 0:
                                result.append([nums[i],nums[left],nums[right]])
                                left +=1
                                right -=1
                                while left<right and nums[left]==nums[left-1]: #skip duplicates
                                        left+=1
                                while left<right and nums[right] == nums[right+1]: #skip duplicates
                                        right -=1
                        elif current_sum<0:
                                left+=1
                        else:
                                right-=1
        return result
        
        
        
        

        
        
                            

check = [1,0,2,-1,-1]

print(threeSum(check))