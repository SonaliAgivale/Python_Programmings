#User Input and Replace String Template “Hello <<UserName>>, How are you?”

name = input("Enter your name: ")
if len(name)>=3:
   print('\nHello',name, end=" How are you?")
else:
    print("Enter minimum three characters")

