"""
You need to start traversing from index k till end of string and then you can traverse back from end to beginning 
At index k you need to check if the character is vowel or consonant 
If it vowel you need to convert it into any consonant and vice versa and according you need to convert entire 
string into one kind of characters i.e vowels or consonants
Now
The cost of moving from one index to next index is 1 coin
And cost of converting a character into another character is also 1 coin
Output should be total cost to get desired output string

"""

# Vowel Verification Function
def isVowelWord(string):
    isVowel = True
    vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    for char in string:
        if char in vowels:
            pass;
        else:
            isVowel = False
            break;
    return isVowel

# Consonant Verification Function
def isConsonantWord(string):
    isConsonant = True
    vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    for char in string:
        if char not in vowels:
            pass;
        else:
            isConsonant = False
            break;
    return isConsonant

# Random Input String: aeioaaeiou
string = list(input("String: "))
index = int(input("Index: "))
vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']

# Random Consonant
consonant = 'c'
# Random Vowel
vowel = 'a'

cost = 0
length = len(string)
print("length: ",length)

# Traversing the given String
while(True):
    if(string[index] in vowels):
        # swap
        string[index] = consonant
        cost+=1
    else:
        string[index] = vowel
        cost+=1
    # Check
    if(isVowelWord(string) or isConsonantWord(string)):
        break;
    #move next
    if(index == length-1):
        index = 0
        string.reverse()
    else:
        index+=1
    cost+=1

print("Cost of entire process: ",cost)
print("Updated String: ", ''.join(string))


"""
Code Analysis:

I picked another Input VIJAYAWADA. But process never stops because this string has 
Consonant, Vowel and so on. So the program runs life time may be breaks at a point 2^n with an error.
So if you want to look out possible output please enter the Random input String.

""" 
