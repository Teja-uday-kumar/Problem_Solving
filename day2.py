#write a program to check if a number is even or odd.
num=int(input('enter a num:'))
if num%2==0:
    print('it is even num')
else:
    print('it is odd number')


# write a program to find the largest of three numbers
num1=int(input('enter a num: '))
num2=int(input('enter a num: '))
num3=int(input('enter a num: '))

if num1>=num2 and num1>=num3:
    largest=num1
elif num2>=num3 and num2>=num1:
    largest=num2
else:
    largest=num3

print(largest)


#check whether the number is a positive or negative
num=int(input('enter a num:'))

if num>0:
    print('it is positive number')
elif num<0:
    print('it is negative number')
else:
    print('it is zero')


#check whether a number is a prime number
num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print("It is prime")
else:
    print("It is not prime")


#find the factorial of a given number
num=int(input('enter a num'))
fact=1
for i in range(1,num+1):
    fact=fact*i

print(fact)



