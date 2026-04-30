def pro(arr):
    res = []
    
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i != j:
                product *= arr[j]
        res.append(product)
    
    return res

print(pro([7,5,2,1]))
