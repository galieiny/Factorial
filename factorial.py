def FactorialIterative(n):
  ans=1
  for i in range(2,n+1):
    ans*=i
  return ans

def FactorialRecursive(n):
  if n==1 or n==0:
    return 1
  return n*factorial_recursive(n-1)

def IsPrime(n):
  for i in range(2,n):
    if n%i==0:
      return False
  return True
