from sys import argv


def simple_read_and_print():
    filename = argv[1]
    file = open(filename, "r")
    content = file.read()
    print(content)
    file.close()


def read_in_lines():
    filename = argv[1]
    file = open(filename, "r")
    content = file.read().split("\n")
    for line in content:
        print(line)

    file.close()


def main():
    read_in_lines()
    #simple_read_and_print


if __name__ == '__main__':
    main()
