n=int(input())
m=int(input())
day1=m//n
day=m%n
day=(day/(day+1.000001))
#day=day1+day
print(day)
