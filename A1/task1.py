#Name: Kari Helene Bekkelund

#Defines the delimiters, add a list to store all user input and
#add a count to track the number of given senteces.
delimiters = ".?!"
userTxt = list()
count = 0;

#Repeat the process until the condition is fulfilled
while count is not 5:

    #Takes user input
    print("Write some text: ")
    userInput = input()

    #temp value for storing the input in case of a text with more than 5 sentences
    temp = ""
    for char in userInput:
        temp += char
        #check if the character is a delimiter and cancel(break) the process if the condition is fulfilled
        if char in delimiters:
            count += 1
            if count is 5:
                break

    #Store the input in case of more iterations
    userTxt.append(temp)

#print the given text with some spacing on top
print("\n\n")
print(' '.join(userTxt))
