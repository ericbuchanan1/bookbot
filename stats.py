def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def sort(input):
    test = {}
    for key in sorted(input, key=input.get, reverse = True):
        if key.isalpha():
            test[key] = input[key]
            print(f"{key}: {test[key]}")

    return
    

def get_num_letter(text):
    output = {}
    lower_text = text.lower()

    for word in lower_text:
        for letter in word:
            if letter in output:
                output[letter] = output[letter] + 1
            else:
                output[letter] = 1 
    return (output)


