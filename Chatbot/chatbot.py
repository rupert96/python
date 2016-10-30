text_file = open ("stopwords.txt")
file_content = text_file.read()
stopWords = file_content.split('\n')
text_file.close()

nonStopWords = []
nRespond = ["nah", "no", "bad", "sad", "unhappy", "upset", "angry"]
pRespond = ["yeah", "yes", "good", "thanks", "great", "happy"]

response = raw_input("Yo.")
response = raw_input("What name do you go by?")
response = raw_input("Cool, alright " + response + "?")
userInputList = response.split(" ")
for everyWord in userInputList:
    if (everyWord not in stopWords):
        nonStopWords.append(everyWord)
        
#if the current word being checked (everyWord) is not in the stop words list, put it in "nonStopWords" list

for everyFilteredWord in nonStopWords:
    if (everyFilteredWord in pRespond):
        response = raw_input ("Sick. You got a spare cig, lad?")
    elif (everyFilteredWord in nRespond):
        response = raw_input ("Ah bugger, not ideal really. Why not?")
    elif (everyFilteredWord not in nRespond or pRespond):
        response = raw_input("Ahem. I said ARE YOU ALRIGHT LAD?")
        
        userInputList = response.split(" ")
        nonStopWords = []
        #split up the userInputList into individual words
        #overwrite the old nonStopWords list with a new empty one
        
        for everyWord in userInputList:
            if (everyWord not in stopWords):
                nonStopWords.append(everyWord)
                #for every individual word in the userInputList, if the word is not in the stop words list then put it into the nonStopWords list

        print(nonStopWords)
        
        for everyFilteredWord in nonStopWords:
                if (everyFilteredWord in pRespond):
                    response = raw_input ("Nice mate, nice. Sorry i didnt understand. You got a spare cig lad?")
                elif (everyFilteredWord in nRespond):
                    response = raw_input ("Nah? Why not mate?")
                elif (everyFilteredWord not in nRespond or pRespond):
                    print ("Whatever mate you're a dick, i'll go and ask someone else.")

                    print(nonStopWords)

#--------------------------------------------------------------------------------------------------------------------------------------------
                    userInputList = response.split(" ")
                    nonStopWords = []
        
                    for everyWord in userInputList:
                        if (everyWord not in stopWords):
                            nonStopWords.append(everyWord)
                #for every individual word in the userInputList, if the word is not in the stop words list then put it into the nonStopWords list

                    print(nonStopWords)
        
        for everyFilteredWord in nonStopWords:
                            if (everyFilteredWord in pRespond):
                                response = raw_input ("Cheers bro. You know smoking is bad for ya but i do it anyway...")
                            elif (everyFilteredWord in nRespond):
                                response = raw_input ("No worries bro. Smoking kills anyway. Catch you later m8er")
                            elif (everyFilteredWord not in nRespond or pRespond):
                                print ("Sorry mate the dance floor is calling out for me. Better shoot, cya later.") 
       
    
   













#print("Cool. Nice to meet you" + name + ". Im chat LAD")
