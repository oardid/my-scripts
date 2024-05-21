import ssl
import nltk
from nltk.corpus import words

try: 
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_words():
    nltk.download('words')
    word_list = words.words()
    return word_list

def check_for_word(words):
    user_answer = input("Enter a word: ").lower()
    if user_answer in words:
        print("The word is in the dictionary")
    else:
        print("The word is not in the dictionary")

def load_external_file():
    password_list = []
    with open('rockyou_sample.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.rstrip()
            password_list.append(line)
            print(password_list)


if __name__ == "__main__":
    external_words = get_words()
    # # print(external_words)
    # check_for_word(external_words)
    load_external_file()