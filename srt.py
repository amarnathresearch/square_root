import math;
# print(math.sqrt(2))
# Binary Search Tree
def sqrt(lower, upper, n, er):
    print("iterations")
    mid = (lower+upper)/2
    if(mid*mid == n):
        return mid
    elif(abs(mid*mid-n) < er):
        return mid
    if mid*mid > n:
        upper = mid
    if mid*mid < n:
        lower = mid
    return sqrt(lower, upper, n, er)

n = 10
lower = 1
upper = n
er = .000000001

ans = sqrt(lower, upper, n, er)
print("our ans", ans)

sys = math.sqrt(n)
print("sys ans", sys)