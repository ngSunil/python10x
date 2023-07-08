from translate import Translator
translator = Translator(to_lang='as')
with open('tips.txt', 'r+') as file:
    file_content = file.read()
    translation = translator.translate(file_content)

    with open('tips-ja.txt', 'a') as my_file:
        my_file.write(translation)
