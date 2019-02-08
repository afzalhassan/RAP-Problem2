# 2.  Given an array print all the numbers that are repeating in it and the number of times they are repeating.
# 
# Below is an example:
# 
# Input: [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
# Output:
# 1 - 4
# 2 - 2
# 5 - 3
# 8 - 2
# 4 - 2

from collections import Counter

lst = list(map(int,input().split()))
count = Counter(lst)
for k,v in count.items():
    if v > 1:
        print (k,end=" - ")
        print (v)
