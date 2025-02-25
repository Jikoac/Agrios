import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(*filepath,binary=False):
    file = os.path.join(path,*filepath)
    f = open(file,('rb' if binary else 'r'))
    return f.read()

def save(*filepath,data='',binary=False):
    file = os.path.join(path,*filepath)
    f = open(file,('wb' if binary else 'w'))
    f.write(str(data))

def list_files(*filepath):
    directory=os.path.join(path,*filepath)
    files = []
    for entry in os.listdir(directory):
        file_path = os.path.join(directory, entry)
        if os.path.isfile(file_path):
            files.append(entry)
    return files

def list_folders(*filepath):
    directory=os.path.join(path,*filepath)
    files = []
    for entry in os.listdir(directory):
        file_path = os.path.join(directory, entry)
        if os.path.isdir(file_path):
            files.append(entry)
    return files

def list_path(**filepath):
    return os.listdir(os.path.join(path,*filepath))

def check_path(*filepath):
    return os.path.exists(os.path.join(path,*filepath))

def check_file(*filepath,data=None):
    if data:
        if os.path.isfile(os.path.join(path,*filepath)):
            return data == load(*filepath)
    return os.path.isfile(os.path.join(path,*filepath))

def check_folder(*filepath):
    return os.path.isdir(os.path.join(path,*filepath))