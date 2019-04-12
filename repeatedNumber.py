class main(): 
def fun(): 
N = int(input()) a = [] list = [] count = 0 a = input().split() a.sort() 
for i in range (0,N): 
k = i+1 for j in range (k,N): 
if j<(N): 
if a[i] == a[j] and a[j] not in list: 
list.append(a[i]) count += 1 l = len(list) for i in range (0,l): 
if i<l-1: 
print (list[i],end=" ")
 else: 
 print (list[i],end="") 
 if count == 0: 
 print ("unique") ob = mainob.func()