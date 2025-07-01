#write a program to print the sum of digits in the number
num=110
sum_of_digits=0
while num!=0:
    last_digit=num%10
    sum_of_digits+=last_digit
    num=num//10
print(sum_of_digits)


#write a program to print reverse of the given number
num=2304
reversed=0
while num!=0:
    last_digit=num%10
    reversed=(reversed*10)+last_digit
    num=num//10
print(reversed)


#write a program to print multiply of the given number
num=444
mul=1
while num!=0:
    last_digit=num%10
    mul=mul*last_digit
    num=num//10
print(mul)


# write a program to print given number is palindrome or not
num=121
rev=0
given_num=num
while num!=0:
    last_digit=num%10
    rev=(rev*10)+last_digit
    num=num//10

if rev==given_num:
    print('it is palindrome')
else :
 print('it is not palindrome')

