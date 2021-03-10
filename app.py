import wordninja
import os
import ntpath

# Point this to the folder with all your books
DIRECTORY_PATH = r"C:\Users\mdjco\Documents\books"


def get_file_name(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def gen_new_name(file, extension):
    result = wordninja.split(file)
    return " ".join(result) + extension


def process_file(file):
    '''
    Tries to rename the file, using the wordninja package
    The file is passed with it's full path
    '''
    full_path, extension = os.path.splitext(file)
    name = get_file_name(full_path)
    path = full_path[:full_path.index(name)]

    old = full_path + extension

    new_name = gen_new_name(name, extension)
    new = path + new_name

    print(old)
    print(new)

    os.rename(old, new)


def iterate_over_directory(directory):
    '''
    Iterates over the specified directory, processing each file
    '''
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)

        is_dir = os.path.isdir(full_path)

        if is_dir:
            iterate_over_directory(full_path)
        else:
            process_file(full_path)


if __name__ == '__main__':
    iterate_over_directory(DIRECTORY_PATH)
