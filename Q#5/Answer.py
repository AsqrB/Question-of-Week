#Boolean function to check if the words are anagrams or not
def anagrams(w1, w2):
    #Remove spaces between both words
    w1 = w1.replace(" ","")
    w2 = w2.replace(" ","")
    # Check if the lengths of the two words are equal
    if len(w1) != len(w2):
        return False
    # Convert both words to lowercase for case-insensitive comparison
    # Sorting the characters of the string
    sorted1 = ''.join(sorted(w1.lower()))
    sorted2 = ''.join(sorted(w2.lower()))
    # Compare the sorted strings
    if sorted1 == sorted2:
        return True
    else:
        return False    

#Taking input from user
word1 = input()
word2 = input()

#Checking if the words are anagrams and displaying answer
if(anagrams(word1, word2)):
  print("Yes")
else:
  print("No")
