number = int(input("Enter a number: "))
print("İs it a Prime number?")


prime = []
for i in range(number+1):# ranging number. stop number = 13 number+1 (0,1,2,3,4,5,6,7,8,9,10,11,12,13)
    prime.append(i)
prime.remove(0)# we must remove "0" (1,2,3,4,5,6,7,8,9,10,11,12,13)

prime_number =[] #(1,2,3,4,5,6,7,8,9,10,11,12,13) tranform (False and True)
for ii in prime:
    prime_number.append(number%ii == 0) # chosing number % ii == 0 --> True
    
if prime_number.count(True) == 2: #prime number only has 2 True
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
