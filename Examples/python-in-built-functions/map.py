def mapFunction (a,b):
    print(a,b,'\n')
    return a+b
x = map(mapFunction,[1,2,3],[1,2,3])

print(x) #[2, 4, 6]