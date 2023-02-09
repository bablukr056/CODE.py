#Heading: Sorting and Grouping Data from a Text File

"""
gene1 1
gene1 2
gene2 3
gene2 4
gene5 5

output 

gene1 1,2
gene2 2,3
gene5 5

"""
import re  

# empty list to store the data from task1.txt file
a1=[]  

# reading the data from task1.txt and splitting based on space to separate the id and name
with open("task1.txt") as data:  
    for line in data:
        a=line.rstrip().rsplit(" ")   
        a1.append(a)
        # print(a1)

# getting a sorted list of unique ids from the data in a1
list_values=sorted(set([list[0] for list in a1])) 
# print(list_values)

# empty lists to store the id and names
id,name=[],[]    

# looping through each unique id and getting the names for each id
for value in list_values:
    for list in a1:
        if list[0]==value:
            id.append(list[0])  #append the id 
            name.append(list[1])#append the name

    # printing the id and names for each id
    print(value+"\t"+','.join(name)) 
    # clearing the lists for the next iteration
    del id[:]
    del name[:] 
