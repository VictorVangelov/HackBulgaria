from sys import argv


def reading_from_one_file():
    script, text_file = argv
    file = open(text_file, "r")
    content = file.read()
    print(content)


def main():
    reading_from_one_file()


if __name__ == '__main__':
    main()
