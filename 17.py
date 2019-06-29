y=int(input())
u=0
h=y
while h>0:
 digit=h%10
 u+=digit**3
 h//=10
if y==u:
 print("yes")
else:
 print("no")
