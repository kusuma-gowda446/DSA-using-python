def rat(arr,rat,unit):
  if len(arr)==0:
    return-1
  total_unit=rat*unit 
  add=0
  for i in range (len(arr)):
    add+=arr[i]
    if add>=total_unit:
      return i+1
  else:
    return 0
print(rat([],4,4))

