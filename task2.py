# help from https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/

import os
os.listdir(path='.')

def getListOfFiles(dirName):

    listOfFile = os.listdir(dirName)
    allFiles = list()

    for entry in listOfFile:
				        # Create full path
        fullPath = os.path.join(dirName, entry)
       				 # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

dirName = '/home/student/Downloads';
				# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)
