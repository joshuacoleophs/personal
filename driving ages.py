age = int(input("enter your age >>> "))

if age >= 17:
    print("you are old enough to drive")
elif age < 17:
    print ("you are to young to drive, you have to wait", 17 - age, "years")

question_1 = str(input("do you want to know how long youve been driving? >>> "))

if question_1 == "yes":
      print("youve been driving for",age - 17,"years")
elif question_1 == "no ":
      exit()
