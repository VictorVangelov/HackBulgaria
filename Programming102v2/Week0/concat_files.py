from sys import argv


def reading_from_many_files():
    contents = argv
    content_of_all_files = ""
    if len(contents) >= 3:
        megatron_file = contents[-1]
    else:
        megatron_file = input(
            "Pleace , enter the file name, where u wanna save the whole information of the file -\n example: \"savedFile.txt\" \n> ")
    for arg in range(1, len(contents) - 1):
        the_file = str(contents[arg])
        print(the_file)
        file = open(the_file, "r")
        content = file.read()
        content_of_all_files += content + "\n\n"
    file = open(megatron_file, 'a+')
    file.write(content_of_all_files)
    file.close()


def main():
    reading_from_many_files()


if __name__ == '__main__':
    main()
