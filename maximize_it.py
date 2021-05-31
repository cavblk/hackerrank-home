# https://www.hackerrank.com/challenges/maximize-it/problem
from itertools import product

K, M = tuple(map(int , input().split()))
# print(K, M)
list_of_num = [[]] * K
# print(list_of_num)
for i in range(K):
    list_of_num[i] = sorted(set(map(int, input().split()[1:])))
    list_of_num[i] = [k * k for k in list_of_num[i] ]
    

# print(list_of_num)

sum_max = 0

li = list(product(*list_of_num))

for lista in li:
    lsum = sum(lista) % M
    if lsum > sum_max:
        sum_max = lsum
        
print(sum_max)
