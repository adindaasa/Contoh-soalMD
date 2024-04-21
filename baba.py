n= 10

total_1= 0
for i in range(n+1):
    total_1 += i

total_2=0
for i in range(n+1):
    total_2 += pow(i,3)

print(total_1,"=", int((1/2)*n*(n+1)))
print(total_2,"=", int((1/4)*pow(n,2)*pow(n+1,2)))
print("Habis dibagi 5", (pow(3,2*n)+pow(2,2*n+2))%5==0)