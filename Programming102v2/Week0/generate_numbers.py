
from sys import argv
from random import randint

scrip, file_name, number_of_ints = argv


def generate_numbers(file_name, number_of_ints):
    generated_numbers = ""
    for i in range(0, int(number_of_ints)):
        generated_numbers += "{} ".format(randint(1, 1000))
    file = open(file_name, 'a+')
    file.write(generated_numbers)
    file.close()


def main():
    generate_numbers(file_name, number_of_ints)

if __name__ == '__main__':
    main()
