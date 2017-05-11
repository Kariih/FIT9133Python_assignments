#Kari Helene Bekkelund, studentnr. 28556844
#Created 20.04.17
#Last modified 28.04.17

from Task1 import StringClass
from Task2 import StringListClass

#Adding constants that will be used in the tests
INPUT_STR_BANANA = "bananas"
INPUT_STR_TESTER = "tester"
INPUT_STR_NOPE = "nope"
INPUT_STR_UPPERCASE_BANANA = "BANANAS"
TOKENS_IN_BANANA_WITH_N_DELIMITER = ["ba", "a", "as"]
STRING_LIST_SIZE = 4
STRING_OF_DCBA = "dcba"
LIST_OF_ABCD = ["a","b","c","d"]

print("Testing String Class")
print("Testing Initialisation of String \n")

#Create instances of the StringClass object based on constants
string_banana = StringClass(INPUT_STR_BANANA)
string_tester = StringClass(INPUT_STR_TESTER)
string_nope = StringClass(INPUT_STR_NOPE)
string_banana_upper = StringClass(INPUT_STR_UPPERCASE_BANANA)

#Check if the string_tester is equal to StringClass with INPUT_STR_TESTER.
print("Is new String equal to String \"tester\"?")
print(str(string_tester == StringClass(INPUT_STR_TESTER)))
print()

#Check if there are 3 as in the word bananas. If it is, print True, else False
print("Is there 3 a's in bananas?")
if string_banana.frequency('a') == 3:
    print(True)
else:
    print(False)
print()

#If there isnt any f in bananas, it prints True. Else print False
print("There are no f's in bananas?")
if not string_banana.search('f'):
    print(True)
else:
    print(False)
print()

#Print return value if a is found in the StringClass instance of bananas
print("Does bananas contain a?")
print(str(string_banana.search('a')))
print()

#Check if string representation of uppercase bananas is same as uppercase string bananas
#If it is uppercase, print true.
print("Does uppercase turn bananas to BANANAS?")
if str(string_banana.uppercase()) == INPUT_STR_UPPERCASE_BANANA:
    print(True)
else:
    print(False)
print()

#Check if string representation of lowercase bananas is same as lowercase string bananas
#If it is uppercase, print true.
print("Does lowercase turn BABANAS to bananas?")
if str(string_banana_upper.lowercase()) == INPUT_STR_BANANA:
    print(True)
else:
    print(False)
print()

#Check if given return value of tokenise method is equal to the expected return
#value given in the TOKENS_IN_BANANA_WITH_N_DELIMITER constant.
print("Check if tokenise generates the correct list \
for bananas when n is the delimiter.")
tokenise_banana = string_banana.tokenise('n')
for token in tokenise_banana:
    if token in TOKENS_IN_BANANA_WITH_N_DELIMITER:
        print("\"" + str(token) + "\" is in token list")
print()

#--------TASK 2 TEST----------
print("*******")
print("Testing StringList Class")
print()

#Check if creation of StringListClass is a instance of StringListClass
print("Testing Initialisation of List")
string_list = StringListClass(STRING_LIST_SIZE)
if isinstance(string_list, StringListClass):
    print("Instantiation test successful")
else:
    print("Instantiation test failed")
print()

#Check it the list length is 0 when no StringClass instances is added.
#Print true if correct.
print("Is new String list length 0?")
if len(string_list) == 0:
    print(True)
else:
    print(False)
print()

#Test if adding StringClass to StringListClass instance will be successful.
#If StringClass is found in instance, print True
print("Test addition")
print("List contain both nope and tester?")
string_list.add(string_nope)
string_list.add(string_tester)
for string in string_list.str_list:
    if string == string_nope or string == string_tester:
        print(True)
print()

#Test of adding two qual instances to the StringListClass and removing the object
#actuallty removes both objects in list. If instance is empty, print True. Else False.
print("Test remove")
string_list_two = StringListClass(STRING_LIST_SIZE)
string_list_two.add(string_banana)
string_list_two.add(string_banana)
print("Is list of two of the same string empty after one remove?")
string_list_two.remove(string_banana)
if len(string_list_two) == 0:
    print(True)
else:
    print(False)
print()

#Check if the StringListClass instance still has the same length than first given.
#The test check the actual length and not the number of instances in list.
print("Is the maximum size the same as the original?")
count = 0
for item in string_list_two.str_list:
    count += 1
if count == STRING_LIST_SIZE:
    print(True)
else:
    print(False)
print()

#Test the bubblesort method sorts the list dcba into the right order. If not,
#print False, else print True.
print("Test sort")
print("Is list dcba now abcd after sort?")
#Setting up the instance of StringListClass to test
string_list_tree = StringListClass(STRING_LIST_SIZE)
for char in STRING_OF_DCBA:
    string_list_tree.add(StringClass(char))
string_list_tree.sort()
#Check if it was sorted correctly
is_sorted_correctly = False
for index, char in enumerate(string_list_tree.str_list):
    if str(char) is not LIST_OF_ABCD[index]:
        break
    else:
        is_sorted_correctly = True
print(is_sorted_correctly)
print()

#Check if the searching method finds the requested character.
print("Test search")
print("Does a exist in list via search")
print(string_list_tree.search(StringClass('a')))
print()

#Check if the searching method doesn't find the requested character.
print("Does search fail to find 'f' in list?")
if not string_list_tree.search(StringClass('f')):
    print(True)
else:
    print(False)
