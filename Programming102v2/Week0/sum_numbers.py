from sys import argv
scrip, filename = argv


def sum_numbers(text_file):
    file = open(text_file, "r")
    content = file.read()
    print (sum(int(x) for x in ((content.split()))))


def main():
    sum_numbers(filename)

if __name__ == '__main__':
    main()
