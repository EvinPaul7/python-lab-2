import random
import string


print("Welcome to Random Password Generator")

length=int(input("Enter the length of the password you want to generate: "))

a=string.ascii_lowercase
b=string.ascii_uppercase
c=string.punctuation
d=string.digits


total=a+b+c+d

p1=random.sample(total,length)
password="".join(p1)
print(password)
