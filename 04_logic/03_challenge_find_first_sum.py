"""
 Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus indices. Si no existe tal combinacion, devuelve None

 nums = [1,2,3.4,32]
 goal = 8

 find_first_sum(nums,goal)
"""

def find_first_sum(nums,goal):

    for i in nums:
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == goal:
                return[i,j]

    return None

nums=[1,2,3,4,5]
goal=8

print(find_first_sum(nums,goal))

#con diccionarios

def find_first(nums,goal):
    seen = {}
    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen:
            return [seen[missing], index]

        seen[value] = index
    return None

nums=[1,2,3,4,5]
goal=8

print(find_first(nums,goal))