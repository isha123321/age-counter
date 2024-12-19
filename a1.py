try:
       age = int(input("Enter your age: ")) 
    
if age < 0 or age > 125:
    print("The age entered is not real. Please enter an accurate age.")
else:
  if age % 2 == 0: 
      print("The age is even.")
  else: print("The age is odd.")
  except ValueError:
  print("Invalid age. Please enter an accurate value for the age.")