#import os


#path = "/Users/shoyo/Desktop/PycharmProjects/Lessons/Random/FileHandling.py"

#if os.path.exists(path):
 #   print("Exists")
 #   if os.path.isfile(path):
 #       print("This is a file")
 #   elif os.path.isdir(path):
 #       print('That is a directory')

#else:
#    print("Doesn't exist")



#Read a file

#try:
    #with open('/Users/shoyo/Desktop/PycharmProjects/Lessons/Random/sampleforreadingafile.txt') as file:
        #print(file.read())
        #print(file.closed)

#except FileNotFoundError:
    #print("That file was not found :(")



#Write a File


#with open('filename.extension','w' ##To append, use 'a'##) as file:
    #file.write(textvalue)



#Copy a File


# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy () + copies metadata (file's creation and modification times)

#import shutil

#shutil.copyfile('filename.extension','copy.txt') #src.dst



#Move a File



#source = "sample.txt"
#destination = "location"


#try:
    #if os.path.exists(destination):
    #    print("There is alreadya file here")
    #else:
     #   os.replace(source,destination)
     #   print(source+" was moved")
#except FileNotFoundError:
    #print(source+ 'was not found')



#Deleting a File

#try:
    #os.remove('filename.extension/filepath')    #deletes a file
    #os.rmdir(path)                              #deletes an empty directory
    #shutil.rmtree(path)                         #deletes a directory containing files
#except FileNotFoundError:
    #print('File not Found')
#except PermissionError:
    #print('You do not have permission to delete that')
#except OSError:
    #print('You cannot delete using that function')
#else:
    #print(path+' was deleted')

