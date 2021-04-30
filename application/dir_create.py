import os


def dir_create(dir_name):
    if os.path.exists(dir_name) is False:
        os.mkdir(dir_name)
    return dir_name