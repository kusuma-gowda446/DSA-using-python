def sol(arr,target):
  if len(arr)<2:
    return -1
  arr.sort()
  a,b=arr[0],arr[1]
  if a+b<=target:
    return a*b
  else:
    return 0
print(sol([15],19))
  

