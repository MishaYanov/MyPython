import json
import difflib

####loading the dictionary.
data = json.load(open("App_1\data.json","r"))
####return the translation.
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
            return data[w.upper()]
    elif len(difflib.get_close_matches(w, data.keys())):
        var= input("Did you mean: %s. Type Y for yes or N for no:  " % difflib.get_close_matches(w, data.keys())[0])
        if var =='y' or 'Y':
            return data[difflib.get_close_matches(w, data.keys())[0]]
        elif var=='n' or 'N':
            return "The word is does not exist in this dictionary try again."
        else:
                return "Not a valid command please try again."
    else:
        return "The word is does not exist in this dictionary try again."

###the user input.
word=input("please enter a word: ")
translated=translate(word)
if type(translated) == list:
    for item in translated:
        print(item)
else:
    print(translated )