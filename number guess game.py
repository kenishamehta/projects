import random #used to generate random values

target=random.randint(1,100)

while True:
     userChoice =int(input("guess the target:"))
     if (userChoice == target):
          print("success: correct guess!!")
          break
     elif(userChoice < target):
          print("your number was to small..take bigger guess..!")
     else:
        print("your number was too big.")

print("______________game over________________")


