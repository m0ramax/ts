# two sum
# given an array = [1,2,3,4]
# and an integer = 3
# find the elements that sum that
# in that case [0,1]

# brute force On*n
def twoSum1(nums: list[int], n: int) -> list[int]:
    acc = 0
    l = []
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            acc = nums[i]+nums[j]
            if(acc == n):
                l.extend((i,j)) # extend para añadir múltiples elementos a una lista
                return l
    return l

# una mejor solución es un usar un dict o hashmap 
def twoSum(nums: list[int], n: int) -> list[int]:
    seen = {} # val:index
    for i, num in enumerate(nums): # se recorre la lista, guardando el valor y el indice 
        complement = n - num # como tenemos que saber el resultado de la suma, podemos hacer la resta de n - num
        if complement in seen: # si ese valor está en el hashmap
            return [seen[complement], i] # retornamos los índices en una lista
        seen[num] = i # si no, asignamos los valores e indices al hashmap
    # return []

l1 = [2,1,4,3]
l2 = [3,2,4]
l3 = [3,3]
l4 = [2,11,5,7,8,19,1000]

print(twoSum(l1,7))
print(twoSum(l2,6))
print(twoSum(l3,6))
print(twoSum(l4,10))
