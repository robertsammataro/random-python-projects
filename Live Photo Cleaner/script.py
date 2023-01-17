#Simple Live Photo Removal Script
#Robby Sammataro
# 17 January 2023
#
#Removes .MOV files that have the same name as a .HEIC file

import os
import os.path

print("Enter source folder path")
file_path = input()

os.chdir(file_path)

for file in os.listdir(file_path):
    if(file.lower().endswith(".heic")):
        
        new_file = file.lower().replace(".heic", ".mov")
        
        if(os.path.exists(os.getcwd() + "\\" + new_file)):
            
            print("Found file pair:", file, new_file)
            os.remove(os.getcwd() + "\\" + new_file)