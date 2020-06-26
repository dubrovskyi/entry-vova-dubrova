import random
import requests


def project_name_generator(number_of_words=3) -> str:
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    string = ""
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    for x in range(number_of_words):
        word = ""
        while len(word) < 3:
            word = random.choice(WORDS).decode('utf-8').lower()
        string += f"{word} "

    return string


if __name__ == '__main__':
    print(project_name_generator())