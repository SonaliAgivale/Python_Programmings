print("********Leap Year*********")
def CheckLeapYear(year):
 if((year % 400 == 0) or
    (year % 100 !=0) and
    (year % 4 == 0)):
  print("Entered year is Leap Year")
 else:
     print("Entered year is not Leap Year")
year=int(input("Enter the year: "))   
CheckLeapYear(year)