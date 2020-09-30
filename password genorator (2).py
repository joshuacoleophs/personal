# password maker 

activity = str(input("enter an activity you like to do >>> ")).lower()
number = int(input("enter your favourite number >>> "))
randomObject = str(input("enter a random object >>> ")).upper()
randomInstrument = str(input("enter a random instrument >>>" )).lower()
specialCharater = input("enter a special charater >>> ")
specialCharacter2 = input("enter another special charater >>> ")
number2 = int(input("enter a random number >>> "))

print("the password that was genorated was ")
print(" ")
print(activity[3:5],specialCharater,randomObject[-1],number2,randomInstrument[0:3],specialCharacter2,number)
