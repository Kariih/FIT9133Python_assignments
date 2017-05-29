from StringClass import StringClass
from StringListClass import StringListClass

INPUT_STR_APE = "ape"
INPUT_STR_BANANA = "bananas"
INPUT_STR_COW = "cow"
INPUT_STR_HORSE = "horse"
INPUT_STR_TESTER = "tester"
INPUT_STR_NOPE = "nope"

string_ape = StringClass(INPUT_STR_APE)
string_banana = StringClass(INPUT_STR_BANANA)
string_cow = StringClass(INPUT_STR_COW)
string_horse = StringClass(INPUT_STR_HORSE)
string_tester = StringClass(INPUT_STR_TESTER)
string_nope = StringClass(INPUT_STR_NOPE)

print("There are s's in bananas?")
print(string_banana.search('s', len(string_banana)-1))

string_list = StringListClass(5)
string_list.add(string_ape)
string_list.add(string_banana)
string_list.add(string_horse)
string_list.add(string_nope)
string_list.add(string_tester)

print(str(string_list))

print("There are ape in list?")
print(str(string_list.search(string_ape, 0, len(string_list)-1)))

#Linear search implemented in StringClass

#def search(self, target_char, number):
#    if self.__is_empty_list():
#        return False

#    if number == 0:
#        return False
#    elif self.str_data[number] == target_char:
#        return True

#    return self.search(target_char, number-1)

#binary search method implemented in StringListClass

#def search(self, target_item, left, right):
#    current_index = int((left + right) / 2)

#    if left > right:
#        return False

#    if target_item == self.str_list[current_index]:
#        return True
#    elif target_item < self.str_list[current_index]:
#        return self.search(target_item, left, current_index - 1)
#    else:
#        return self.search(target_item, current_index + 1, right)
