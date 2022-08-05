#FILE MANIPULATION IN PYTHON
#i want to open file, there are two way and three mode
#write(w), read(r), append(a)

#1.Open file
# openFile =  open("story.txt", "r")    #but if it is in a file openFile = open(./story.txt)
# print(openFile)

# with open
# with open("story.txt","r") as openFile:
#     print("This file is true")


# #2. read our file
# with open("story.txt","r") as openFile:
#     readFile = openFile.read()
#     print(readFile)

#. split word and count words using the def function n.b in the examples 
# given she called the  name -->def readFile(filename):
# def  readFile():
#     with open("story.txt","r") as openFile:
#         readFile = openFile.read()
#         return(readFile)

# def countwords():
    #note in the class readFile("story.txt")
    # text = readFile()
    # split_text = text.split()
    # print(split_text)
    
    #creating a dictionary words that counts the value,so you have to create an empty dictionary
    #Make use of for loop that will go over each words in the list 
    # and store each words to check how many times it occured
    # count ={}
    # for i in split_text:
    #     if i in count:
    #         count[i] +=1
    #     else:
    #         count[i] =1
    # return(count)

#without the print funtn it wont count the words"gives an empty terminal"
#print(countwords())



#3.write a new file:when writing a file you have to create a new file and 
# if you have a previous document that ypu have a previous document 
# and you want to add something to it "IT WONT WORK " because 
# whatever you dd to the previous file will just replace the words written in the previous file

#newFile = open("story.txt", "w") #--> this is to check if the file exist or not
#note if the "story.txt" file does not exist like crating a 
# new file e.g"zuri.txt" it will create the file itself

# new_file = open("zuri.txt", "w")
# #openFile = new_file.read()-->to check if the file has been created
# writeFile = "Hello world i am attending the zuring class and it has been an intresting session."
# finalDoc = new_file.write(writeFile)
# new_file.close() #-->it means to save the file incase the system goes off

# #now read the file 
# new_file = open("zuri.txt", "r")

# read_file = new_file.read()
# print(read_file)

#To append the file
# new_file = open("zuri.txt", "a")
# write_file = " This class has been a very enjoyable and understing sesion"
# final_doc = new_file.write(write_file)
# #new_file.close()


#To read the append file
# new_file = open("zuri.txt","r")
# write_file = new_file.read()
# print(write_file)

#why we use i in for loop
# x = ["you", "me", "our",35]
# count = []
# for i in x:
#     #count[i] +=1 #-->n.b:this is not iterable it means we are adding 1 anytime its stores the value
#     print(i)

#combining the files together
def readFile():
    openFile = open("story.txt", "r")
    readFile = openFile.read()
    #print(readFile)
#readFile()--> if the text is inside a file, it will have an argument in the def readfile(filename)
#  and called in read file as "story.txt" 
    new = readFile.split()
    print(new)
    count = {}
    for i in new:
        if i in count:
            count[i] +=1
        else:
            count[i] =1
    return(count)
print(readFile())