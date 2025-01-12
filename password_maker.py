import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0','1','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','+']
print("wwelcomee to the password generator!")

nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input("how many symbols would you like?\n"))
nr_numbers=int(input("hoe many numbers would you like?\n"))

password=[]
for char in range(0,nr_letters+1):
    password.append(random.choice(letters))

for char in range(0,nr_numbers+1):
    password.append(random.choice(numbers))
    
for char in range(0,nr_symbols+1):
    password.append(random.choice(symbols))
    
random.shuffle(password)
print(password)

passwords = ""
for char in password:
    passwords+=char
print(f"Your password is {passwords}")