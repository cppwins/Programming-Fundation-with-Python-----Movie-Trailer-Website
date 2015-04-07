from os import listdir, rename, chdir, getcwd

def renameFiles:
    file_list = listdir(r"D:\Udacity\fullStackNano\Programming Foundations with Python\Lesson 1\prank")
    print file_list
    saved_path = getcwd()
    chdir(r"D:\Udacity\fullStackNano\Programming Foundations with Python\Lesson 1\prank")

    for file_name in file_list:
        rename(file_name, file_name.translate(None, "0123456789"))

    chdir(saved_path)
