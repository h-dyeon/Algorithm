# def numberOfArithmeticSlices(nums):
#     if len(nums)<3:
#         return 0
#     nums=[nums[i+1]-nums[i] for i in range(len(nums)-1)]
#     nums=[nums[i+1]-nums[i] for i in range(len(nums)-1)]
#     print(nums)
#     answer=0
#     for i in range(len(nums)):
#         if nums[i]==0:
#             for j in range(i,len(nums)):
#                 if nums[j]!=0:
#                     break
#                 print(nums[i:j+3])
#                 answer+=1
                
#     return answer

def numberOfArithmeticSlices(nums):
    if len(nums)<3:
        return 0
    nums=[nums[i+1]-nums[i] for i in range(len(nums)-1)]
    nums=[nums[i+1]-nums[i] for i in range(len(nums)-1)]
    print(nums)
    answer=0
    for i in range(len(nums)):
        if nums[i]==0:
            for j in range(i,len(nums)):
                if nums[j]!=0:
                    break
                answer+=1
                
    return answer

nums = [1,2,3,4,6,7,8,7]
print(numberOfArithmeticSlices(nums))