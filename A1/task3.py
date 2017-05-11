#Name: Kari Helene Bekkelund

#Defines the delimiters, add a list to store all user input and
#add a count to track the number of given senteces and tokens.
delimiters = ".?!"
charsExcludedFromTokenList = " '-"
userTxt = list()
count = 0;
tokensFound = 0

#variables for analyse text
numberOfChars = 0
totalNumberOfWords = 0
totalUniqueWords = []
wordsStartingWithUppercase = 0
numberOfPunctationMarks = {}
totalNumericWords = 0

#Repeat the process until the condition is fulfilled (5 sentences)
while count is not 5:
    temp = ""

    #Takes user input
    print("Write some text: ")
    userInput = input()

    #Iterate through the given characters
    for index, char in enumerate(userInput):
        #temp value for storing the input in case of a text with more than 5 sentences
        temp += char

        #count total amout of letters
        if char.isalpha() or char.isnumeric():
            numberOfChars += 1

        #Exclude the count of punctation marks which has whitespaces on both sides. Ex: "string , string"
        nextChar = userInput[index + 1] if len(userInput) <= index else ""
        if userInput[index -1] is not " " and nextChar is not " ":
            #count number of special characters that should be count as an individually token but is part of a word Ex: "String, string".
            if not char.isalpha() and not char.isnumeric() and char not in charsExcludedFromTokenList:
                tokensFound += 1;

                #Store the amout of individual punctation marks.
                if char in numberOfPunctationMarks:
                    numberOfPunctationMarks[char] += 1
                else:
                    numberOfPunctationMarks[char] = 1

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

#analyse the stored text
for sentence in userTxt:
    #Count total number of words
    totalNumberOfWords += len(sentence)
    for word in sentence:
        #count uppercase words in text
        if word[0].isupper():
            wordsStartingWithUppercase += 1

        #Remove the punctation mark if exist before checking for unique and numeric words.
        lastChar = word[len(word)-1]
        if not lastChar.isalpha() and not lastChar.isnumeric() and lastChar is not "'":
            word = word[:-1]

        #count the unique words
        if not word.lower() in totalUniqueWords:
            totalUniqueWords.append(word.lower())

        #Count words with digits in text
        if word.isnumeric():
            totalNumericWords += 1

#print text analysis
print("\n\n")
print("Total number of words: " + str(totalNumberOfWords) + " (" + str(numberOfChars) + " characters)")
print("Number of unique words: " + str(len(totalUniqueWords)))
print("Words staring with uppercase: " + str(wordsStartingWithUppercase))
for key in numberOfPunctationMarks:
    print("Punctation mark " + key + " has count equal to: " + str(numberOfPunctationMarks[key]))
print("Number of Numeric words: " + str(totalNumericWords))
