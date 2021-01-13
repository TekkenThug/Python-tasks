n=int(input())
time=540
lesson=n*45
n=n-1

u=((n//2)*15)+((n-(n//2))*5)



lesson=lesson++time+u
h=lesson//60
m=lesson-(h*60)

print(h,m)
