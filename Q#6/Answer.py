#Taking input in the form of 
# string from user
Number = input()

# Checking if the given string
#  have digits only
if( Number.isdigit()):
  # The given string contains
  #  digits only
  print("YES")
else:
  # The given string contains
  #  characters other than digits
  print("NO")
