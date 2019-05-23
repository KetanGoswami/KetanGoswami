# help from https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/

import os
 
'''
    For the path given, proving List of all files in the directory list 
'''
def getListOfFiles(dirName):    # create a list of file and sub directories 
    listOfFile = os.listdir(dirName)
    allFiles = list()

    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry) 
        if os.path.isdir(fullPath):           # If entry is a directory then get the list of files in this directory
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

def main():
    dirName = '/home/student/Downloads';                   # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
    for elem in listOfFiles:
       print(elem)
    print ("****************")

    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    for elem in listOfFiles:                        # Print the files
        print(elem)    

if __name__ == '__main__':
    main()


