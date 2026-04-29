def cal(arr):
  odd_sum=0
  even_sum=0
  for i in range (len(arr)):
    if i%2==0:
      even_sum+=arr[i]
    else:
      odd_sum+=arr[i]
  return odd_sum-even_sum
  print(cal([1,2,3,4,5]))

