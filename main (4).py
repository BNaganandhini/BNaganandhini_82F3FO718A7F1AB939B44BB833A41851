def checkLeapyear(year):
  if (year % 400 == 0 or year % 100 != 0) and (year % 4 == 0):
    return True
  else:
    return False


year = int(input("Enter the number:"))
if checkLeapyear(year):
  print("Given year is a leap year")
else:
  print("Given year is not a leap year")
