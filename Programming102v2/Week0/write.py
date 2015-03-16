def simple_write_in_file():
    filename = "text.txt"
    file = open(filename, 'w')
     # Here, "w" stands for open for writing
    contents = ["Python is awesomeeee.", "You should check it out!"]
# Here, we are joining each element with a new line
    file.write("\n".join(contents))

# when we are done, we close the file
    file.close()




def main():
    simple_write_in_file()


if __name__ == '__main__':
    main()
