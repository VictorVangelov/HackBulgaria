from sys import argv

scrip, arg = argv

# solution 1 , that doesnt trancate file
# def import_boilerplate():
#     boilerplate_pattern = """import sys\n\n\ndef main():
#     pass\n\nif __name__ == '__main__':
#     main()\n\n"""
#     file = open(arg, "r+")
#     content = file.read()
#     file.truncate()
#     file.write(boilerplate_pattern + content)


def import_boilerplate():
    boilerplate_pattern = """import sys\n\n\ndef main():
    pass\n\nif __name__ == '__main__':
    main()\n\n"""
    file = open(arg, "r")
    content = file.read()
    file = open(arg, "w")
    file.write(boilerplate_pattern + content)


def main():
    import_boilerplate()

if __name__ == '__main__':
    main()
