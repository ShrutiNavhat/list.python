a=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=1
max=0
max1=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
print(max)
i=0
while i<len(a):
    if a[i]>max1:
       if a[i]!=max:
           max1=a[i]
    i=i+1
print(max1)



