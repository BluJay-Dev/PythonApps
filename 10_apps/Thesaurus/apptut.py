import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("did you mean %s instead? Enter Y if yes, or N if no " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist please try again"
        else:
            return "Sorry please try again!"
    else:
        return "The word doesn't exist"


word = input("enter word: ")
output = translate(word)
c = 0
if type(output) == list:
    print("Your results below:")
    for item in output:
        c += 1
        print(f'{c}: {item}')
else:
    print(output)
