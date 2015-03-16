
from sys import argv
script, the_command, file_name = argv


def split_text_on_words(text_file, command):
    file = open(text_file, 'r')
    content = file.read()
    file.close()
    if command == "chars":
        print (sum(len(x) for x in (content.split())))
    elif command == 'words':
        print (len(list(content.split())))
    elif command == "lines":
        print (len(list(content.split("\n"))))
    else:
        print("unknown command, please try again ")
        return split_text_on_words(text_file, input("> "))


def main():
    split_text_on_words(file_name, the_command)

if __name__ == '__main__':
    main()
