#Decker Gramlich
#CS325
#poject 3 - 2nd module

#inputs the content and the name of the file(which includes the path to the proper folder)
#outputs the file. is used twice

def save_content_to_file(content, filename):

    file = open(filename, "w") #creates file
    file.write(content) #puts text in file
    file.close() #closes file