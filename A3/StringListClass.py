#Kari Helene Bekkelund, studentnr. 28556844
#Created 24.04.17
#Last modified 28.04.17

from StringClass import StringClass

#Class that handles and modifies lists of StringClass instances
class StringListClass:

    #Create new instance of StringListClass with the length of size
    def __init__(self, size):
        self.str_list = [None] * size
        self.original_size = size

    #Add new StringClass instance to list
    #Raise exception if list is full
    def add(self, new_item):
        if self.str_list[-1] is not None:
            raise Exception("List is full")
        if isinstance(new_item, StringClass):
            for index, item in enumerate(self.str_list):
                if item is None:
                    self.str_list[index] = new_item
                    break

    #remove all occurances of the target_item.
    #Moves all available spots to the end of list
    def remove(self, target_item):
        removed = 0
        index_to_move = 0
        if isinstance(target_item, StringClass):
            for index, item in enumerate(self.str_list):
                if item == target_item:
                    self.str_list[index] = None

        for i in range(len(self.str_list)):
            for index in range(len(self.str_list)-1):
                if self.str_list[index] is None:
                        self.__swap(index)

        return self.str_list

    #Use bubblesort algorith to sort StringClass instances in a list.
    #Sorting is based on ASCII values.
    def sort(self):
        for i in range(len(self.str_list)):
            for index in range(len(self.str_list)-1):
                if self.str_list[index +1] is not None:
                    if self.str_list[index] > self.str_list[index +1]:
                        self.__swap(index)

    #search for the given target_item in list using binary search
    #Return true if target_item is found and false if the element doesn't exist.
    def search(self, target_item, left, right):
        current_index = int((left + right) / 2)

        if left > right:
            return False

        if target_item == self.str_list[current_index]:
            return True
        elif target_item < self.str_list[current_index]:
            return self.search(target_item, left, current_index - 1)
        else:
            return self.search(target_item, current_index + 1, right)

    #Operator overloaded methods

    #Returns a string prepresentation of the list
    def __str__(self):
        temp = ""
        for index, string in enumerate(self.str_list):
            temp += str(string) + "\n"
        return temp

    #Returns the number of StringClass instances in list
    def __len__(self):
        count = 0
        for char in self.str_list:
            if char != None:
                count += 1
        return count

    #Private methods

    #Swap two instances of StringClass in list
    def __swap(self, index):
        temp = self.str_list[index]
        self.str_list[index] = self.str_list[index + 1]
        self.str_list[index + 1] = temp
