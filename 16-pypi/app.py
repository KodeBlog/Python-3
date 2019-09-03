from spellchecker import SpellChecker #imports our third-party package that we installed using pip

spell = SpellChecker()

word_list = ['Jakc','was','ak','work','on','satuday']

misspelled = spell.unknown(word_list)

for word in misspelled:
    correct_word = spell.correction(word)
    print(f'The word "{word}" has been mispelled. The correct spelling is {correct_word}')
    print(f'Other likely words are {spell.candidates(word)}')