from os import listdir, remove, makedirs, getcwd, chdir
from sys import path
from os.path import dirname, abspath, exists, isfile, join as path_join
path.append(dirname(dirname(abspath(__file__))))
from others.Random import generate_pattern

# def path_exists(filename,path=''):
#     try:
#         if type(filename)==str==type(path) and exists(path+filename):
#             return True
#         else:
#             False
#     except Exception as e:
#         return False

def tmpfile_path():
    try:
        filename = generate_pattern("LLDDDDDD")
        while exists("/tmp/tmp-"+filename):
            filename = generate_pattern("LLDDDDDD")
        return "/tmp/tmp-"+filename
    except:
        return ''

def create_tmpfile():
    try:
        filename = tmpfile_path()
        if filename:
            return open(filename, 'w')
        else:
            return None
    except Exception as e:
        print(e)
        return None

def create_file(path):
    try:
        if type(path)==str and not exists(path):
            return open(filename, 'w')
    except Exception as e:
        print(e)
        return None

def use_file(path):
    try:
        if type(path)==str and exists(path):
            return open(filename, 'a')
    except Exception as e:
        print(e)
        return None

def delete_file(file_path):
    """
    Checks if a file exists and deletes it if it does.
    Prints a message if the file does not exist.
    
    Args:
    file_path (str): The path to the file to check and delete.
    """
    try:
        if not type(file_path)==str:
            raise ValueError("File path must be a string")
        
        if isfile(file_path):
            remove(file_path)
            return True
        return False
    except Exception as e:
        print(f"An error occurred: {e}")

def create_directory(path):
    try:
        if type(path)==str:
            if not exists(path):
                makedirs(path)
                return 1
            return 0
        return -1
    except Exception as e:
        print(e)
        return None