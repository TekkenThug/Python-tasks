v=int(input())
t=int(input())
p=v*t
c=p
if abs(p)>108:
    while abs(p)>109:
        p=abs(p)-109
if c<0:
    p=109-abs(p)
else:
    p=0+p
print(p)
    

    
