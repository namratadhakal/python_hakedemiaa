sentence = input("Enter the sentence: ")

vowels = consonants = digits = spaces = 0

for i in sentence:
    if i.isalpha():
      if i.lower() in "aeiou":
        vowels +=1
      else:
         consonants +=1
    elif i.isdigit():
        digits +=1
    elif i.isspace():
       spaces +=1
    
print(f"No of Vowels: {vowels}")
print(f"No of Consonants: {consonants}") 
print(f"No of Digits: {digits}")
print(f"No of Spaces: {spaces}")

# for case conversion
print("Uppercase :", sentence.upper())
print("Lowercase :", sentence.lower())


## for removing extra spaces
sentence = " ".join(sentence.split())
print(sentence)



#1. Why is string processing critical in cybersecurity and NLP?
 
 # Ans : In cybersecurity, string processing helps to detect  malicious code, passwords and patterns of attackers. And in NLP, to understand and analyze human languages like  chats and documents string processing is useful.  Overall, string processing is critical as it helps detect harmful text in cybersecurity and understand human language in NLP.
 

 #2. How can improper string handling introduce vulnerabilities? 

#Ans : Improper string handling means not checking user inpur properly before using it in program. Such action can introduce  vulnerabilities  by allowing attackers to inject malicious input  which can steal data or crash the whole system.