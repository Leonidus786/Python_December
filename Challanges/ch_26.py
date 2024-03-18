'''026
Pig Latin takes the first consonant of a word,
moves it to the end of the word and adds on an
“ay”. If a word begins with a vowel you just add
“way” to the end. For example, pig becomes igpay,
banana becomes ananabay, and aadvark becomes
aadvarkway. Create a program that will ask the
user to enter a word and change it into Pig Latin.
Make sure the new word is displayed in lower case.'''

word = input("Enter a word: ")

first_char = word[0]

length = len(word)

rest_word = word[1:length]

if first_char != 'a' and first_char != 'e' and first_char != 'i' and first_char != 'o' and first_char != 'u':
    new_word = rest_word + first_char + "ay"
else:
    new_word = word + "way"

print(new_word.lower())

