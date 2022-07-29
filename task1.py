import re  #import regular expression module 

a1=[]  #empty list  to store the value from the file 
with open("task1.txt") as data:  #open and read the file
    for line in data:
        a=line.rstrip().rsplit(" ")   #split data based on the space as givenin file.
        a1.append(a)
        # print(a1)

list_values=sorted(set([list[0] for list in a1]))   #uniqe and sorted values by applying set functions
# print(list_values)

id,name=[],[]    #empty list id=first column name=value in the second column

for value in list_values:
    for list in a1:
        if list[0]==value:
            id.append(list[0])  #append the id 
            name.append(list[1])#append the name

    print(value+"\t"+','.join(name)) #print the stored value for the list 
    del id[:]
    del name[:] 


