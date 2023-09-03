
animals=['lion','tiger','elephant','monkey']

a=[i for i in animals if 'lion'in i]
print(a)

n=[1,2,3,4,5,]
m=[]
b=list(filter(lambda a: a%2==0,n))
print(b)

c=list(map(lambda a:a*a,n))
print(c)


