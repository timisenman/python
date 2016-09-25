#file name changer

#open folder
#get file names as list
#select image
#find start of file name
#find end of file name
#find name in between
#save name in between

import os

def rename_files():
    #open files
    file_list = os.listdir(r"/Users/timisenman/Documents/python/projects/cs102/prank")
    #print (file_list)
    new_dir = "/Users/timisenman/Documents/python/projects/cs102/prank"
    saved_path = os.getcwd()
    print ("First Working Directory is: " + saved_path)
    os.chdir(new_dir)
    print ("New Working Directory is: " + os.getcwd())
    for file_name in file_list:
        os.rename(file_name, file_name.lstrip("0123456789"))
    os.chdir(saved_path)


rename_files()
                
