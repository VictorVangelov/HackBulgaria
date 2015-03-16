from sys import argv


def reading_from_many_files():
    contents = argv
    content_of_all_files = ""
    for arg in range(1, len(contents)):
        the_file = str(contents[arg])
        file = open(the_file, "r")
        content = file.read()
        content_of_all_files += content + "\n\n"
    print content_of_all_files


def main():
    reading_from_many_files()


if __name__ == '__main__':
    main()
