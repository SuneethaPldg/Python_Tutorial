print("file is for working on datatypes")
#num=input("enter any integer number:",)
#print("your number is : ", num)
'''
print("string operations:")
str1= "python"
str2= "tutorial"
#print(str1+str2) #string concat
print((str1 + " ") * 3) #string repeat
#string slicing
print(str2[3:6])
print(str1[:4])
str3=str1+str2
print(str3)
#print(str3[::-1])
print("string type specific methods:")
#print(str3.count('t',0,13))
#print(str3.find('tor'))
print(str3.upper())
print(min(str3))
print(max(str3))
print(min(str1))
print(max(str2))
'''
'''
print("Data type Tuples")
my_tup1 = ('Suneetha','Phani','Sanjana','Saanvika')
my_tup2 = ('Dasari','Paladugu')
print("my_tup1 is:",my_tup1)
print("my_tup2 is:",my_tup2)
print("my_tup3 is:", my_tup1+my_tup2)
print(my_tup1 *3)
print("---tuple slicing---")
print(my_tup1[-1])
print(my_tup1[:-2]) #doubt
my_tup3=my_tup1+my_tup2
print(my_tup3)
'''
#my_list = [[1,2,3],[['a','b','c'],5,6]]
#print(my_list[1][0][1])
#print(my_list)
#number = input("enter list of numbers:")
#print(num)
#number = number.split()
#print(number)
#accepting list using split and forloop
n = int(input('enter the no of elements:'))
#print(n)
numbers= input('enter the numbers:').split()
print(numbers)
for i in range(n):
    numbers[i]=int(numbers[i])
print(numbers)