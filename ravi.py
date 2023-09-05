def func(a):
    count=0
    for i in range(len(a)):
        
        if a[i]!=0:
          a[count]=a[i]
          count+=1
            
    for j in range(count,len(a)):
        a[i]=0


a=[0,1,2,3,0,9,0]
func(a)

print(a)
