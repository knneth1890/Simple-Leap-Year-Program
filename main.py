#Simple Leap-Year Checker Program

print("Welcome to Leap-Year Checker 1.0")

year = int(input("please enter a year: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
