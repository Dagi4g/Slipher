import os

def get_files(path,file_extension='.py'):
    """this module finda files in a directory with file extension provided."""
    file_list = []
    # os.walk returns a list if tuples that contain the root directory,the directory and file name.
    #when the file name is combined with the  root it gives the relative path from the path given in the parameter. 
    for root, dirs , files in os.walk(path):
        for file in files:
            if file.endswith(file_extension):
                file_list.append(os.path.join(root,file))
    return file_list

def write_license(path):
    files = get_files(path)
    licenses = """
# Licensed under the Apache License, Version 2.0 (the "License");"""
    for file in files[:2]:
        with open(file,"r+") as f:
            content = f.read()
            f.seek(0) # tge cursor doesn't know where to write, so make the cursor at the top.
            f.write(licenses+"\n"+content)
        print(file)

def remove_duplicated(path,start_with='#'):
    files = get_files(path)
    comment_set = set()
    result = []
    for file in files:
        with open(file,'r+') as f:
            lines = f.readlines()
        for line in lines:
            if line.strip().startswith(start_with):
                if line not in comment_set:
                    result.append(line)
                    comment_set.add(line)
            else:
                result.append(line)

        with open(file,'w') as f:
            f.writelines(result)
            result = [] #empity the list before another operation.

if __name__== "__main__":
    remove_duplicated('.')

    #write_license(".")

