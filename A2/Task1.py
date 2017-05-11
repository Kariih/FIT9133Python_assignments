#Kari Helene Bekkelund, studentnr. 28556844
#Created 20.04.17
#Last modified 28.04.17

#Class that handles and modifies strings in a list structure.
class StringClass:

    #creates a new StringClass object
    def __init__(self, str_value):
        self.str_data = []
        for char in str_value:
            self.str_data += char

    #Search for any occurences of the given target_char
    #Return false if an empty object is given
    def search(self, target_char):
        if self.__is_empty_list():
            return False
        for char in self.str_data:
            if char == target_char:
                return True
        return False

    #Finds the number of occurences for given target_char
    #Return false if an empty object is given
    def frequency(self, target_char):
        if self.__is_empty_list():
            return False
        count = 0
        for char in self.str_data:
            if char == target_char:
                count += 1
        return count

    #Replace all occurences of target_char with new_char
    #Return false if an empty object is given
    def replace(self, target_char, new_char):
        if self.__is_empty_list():
            return False
        temp = ""
        for char in self.str_data:
            if char == target_char:
                temp += new_char
            else:
                temp += char
        return temp

    #Returns a copy of string in lowercase
    def lowercase(self):
        temp = ""
        for char in self.str_data:
            temp += self.__change_case_lower(char)
        return temp

    #Returns a copy of string in uppercase
    def uppercase(self):
        temp = ""
        for char in self.str_data:
            temp += self.__change_case_upper(char)
        return temp

    #Returns a list with elements splitted on given delimiter
    #Return false if an empty object is given
    def tokenise(self, the_delimiter):
        if self.__is_empty_list():
            return False
        temp = ""
        tokens = []
        for char in self.str_data:
            if char == the_delimiter:
                tokens.append(temp)
                temp = ""
            else:
                temp += char
        tokens.append(temp)
        return tokens

    #Operator overloaded methods

    #If both elements is instance of StringClass and same length, it checks
    #every char element is the same.
    #Return true if it has the same content. Else return false.
    def __eq__(self, other):
        if isinstance(other, StringClass):
            if len(self) == len(other):
                for index, char in enumerate(other.str_data):
                    if self.str_data[index] != other.str_data[index]:
                        return False
                return True
        return False

    #Return a string representation of the list
    def __str__(self):
        temp = ""
        for char in self.str_data:
            temp += char
        return temp

    #Returns the number of char in list
    def __len__(self):
        count = 0
        for char in self.str_data:
            count += 1
        return count

    #Check if a instance of StringClass is greater or lesser than other instance.
    #Compare the strings based on ASCII values
    #Return True if element a is less than element b. Else return False
    def __lt__(a, b):
        for index, char in enumerate(a.str_data):
            if a != None and b != None:
                if index == len(b.str_data):
                    if len(a.str_data) < len(b.str_data):
                        return True
                    else:
                        return False
                elif ord(char) < ord(b.str_data[index]):
                    return True
        return False

    #following is private methods

    #Responsible for converting uppercase to lowercase char.
    #Returns a lowercase char.
    def __change_case_lower(self, char):
        ascii_value = ord(char)
        if 65 <= ascii_value <= 90:
            ascii_value += 32
            char = chr(ascii_value)
        return char

    #Responsible for converting lowercase to uppercase char.
    #Returns a uppercase char.
    def __change_case_upper(self, char):
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            ascii_value -= 32
            char = chr(ascii_value)
        return char

    #Check if parameter in method is empty.
    #Return True if list is empty else False
    def __is_empty_list(self):
        if not self.str_data:
            return True
        return False
