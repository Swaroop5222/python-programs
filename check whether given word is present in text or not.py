word=input("Enter the word\n")
text=input("Enter the text\n")

if word in text.lower():
    print("yes the word you entered is present in the text\n")
else:
    print("no the word you entered is not present in the text\n")