#! python3

# Author:  Shuvam Shah

import requests, bs4, sys

def findMeaning(word):
    baseURL = 'http://www.dictionary.com/browse/'
    missSpellingBaseURL = 'http://www.dictionary.com/misspeling?term='

    # Download the specific word page.
    res = requests.get('%s%s?s=t' % (baseURL, word))

    try:
        res.raise_for_status()
    except:
        print("%s not found..." % word)
        another_word = str(input('Wanna search for another word? Type the word else type \'exit\': '))
        if another_word == 'exit':
            findMeaning(another_word)
        sys.exit()

    # Parse it using BeautifulSoup4
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find required data
    sections = soup.select('section.ce-spot')

    # Present it.
    print('Searching for your word(s): %s' % word)

    for i in range(len(sections)):
        header = sections[i].select('header span')[0].getText()
        meanings = sections[i].select('div.def-set div.def-content')

        print('%s' % header)
        for j in range(len(meanings)):

            print('%s. %s' % (j + 1, meanings[j].getText()))

        print('\n')

    print('\n')

    print('That\'s all for %s' % word)

word = str(' '.join(sys.argv[1:]))

findMeaning(word)