def reduce_file_path(path):
    path = path.split('/')
    for i, item in enumerate(path):
        #to read enumeate
            if item == '..':
                del path[i-1]
            if item == ".":
                del path[i]

    return '/'.join(path)
    #ne rabotiiii pravilno !!!
