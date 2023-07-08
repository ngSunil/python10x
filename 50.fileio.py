myfile = open('tips.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfile.close()
# ---better way to read file and no need to close the files too
#  w mode witll overwrite all content and write the new text
# a mode will append the text to the end of the file
# w also creates the file if file is not found
# most common are r w a
# use pathlib for cross os file paths
print('----')
with open('tips.txt', mode='a') as my_file:
    text = my_file.write('\sunil')
    print(text)

# try except
try:
    with open('tip1s.txt', 'r') as file:
        print(file.readlines())
except FileNotFoundError as err:
    print(f'File is n ot found {err}')
    raise err
