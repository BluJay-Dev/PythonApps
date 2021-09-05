import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        results = get_close_matches(w, data.keys())
        retry = input(f'did you mean? {results[0]} Y / N: ')
        if retry == "Y":
            w = results[0]
            return w
        elif retry == "N":
            no = input(f'did you mean? {results[1]} Y / N: ')
            if no == "Y":
                w = results[1]
                return w
            else:
                print("Sorry I don't know which word you meant please try again")
                exit()
        else:
            print("Please try again!")


word = input("enter word: ")
c = 0
output = translate(word)
if type(output) == list:
    for item in output:
        c += 1
        print(f'{c}: {item}')
else:
    print(output)
