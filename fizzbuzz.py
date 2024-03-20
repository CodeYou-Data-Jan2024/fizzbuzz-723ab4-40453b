# FizzBuzz printing numbers 1 to 100

for num in range (101):
   # print(num)

#number is dividable by 3 print Fizz
    
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        continue
    elif num % 3 == 0:
        print('Fizz')
        continue
    elif num % 5 == 0:
        print('Buzz')
        continue

    print (num)  


