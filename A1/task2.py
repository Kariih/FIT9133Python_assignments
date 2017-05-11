#Name: Kari Helene Bekkelund

#Defines the delimiters, add a list to store all user input and
#add a count to track the number of given senteces and tokens.
delimiters = ".?!"
charsExcludedFromTokenList = " '-"
userTxt = list()
count = 0;
tokensFound = 0

#Repeat the process until the condition is fulfilled (5 sentences)
while count is not 5:
    temp = ""

    #Takes user input
    print("Write some text: ")
    userInput = input()

    #analyse the given characters
    for index, char in enumerate(userInput):
        #temp value for storing the input in case of a text with more than 5 sentences
        temp += char

        #Exclude the count of punctation marks which has whitespaces on both sides. Ex: "string , string"
        #or else they will be counted as both word and delimiter token
        nextChar = userInput[index + 1] if len(userInput) <= index else ""
        if userInput[index -1] is not " " and nextChar is not " ":
            #count number of special characters that should be count as an individually token but is part of a word Ex: "String, string".
            if not char.isalpha() and not char.isnumeric() and char not in charsExcludedFromTokenList:
                tokensFound += 1;

        #check if the character is a delimiter and cancel(break) the process if the condition is fulfilled
        if char in delimiters:

            #Store the sentences in a list of strings
            words = temp.strip().split(" ")

            #Add the number of tokens in each sentence
            tokensFound += len(words)

            #Store the sentence, reset the temporary(temp) variable and
            # and add the number of given senteces
            userTxt.append(words)
            temp = ""
            count += 1

            #Breaks the loop if the first input is longer than 5 sentences.
            if count is 5:
                break

#print the given text with some spacing on top
print("\n\n")
print("Total number of tokens: " + str(tokensFound))
for sentences in userTxt:
    print(' '.join(sentences))
