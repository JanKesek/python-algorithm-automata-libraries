def fibo(n, memo = {}):
    if n==0:
        memo[n]=0
        return 0
    elif n==1:
        memo[n]=1
        return 1
    else:
        s = fibo(n-1,memo) + fibo(n-2,memo)
        memo[n]=s
        return s
print(fibo(6))
print(fibo(22))
