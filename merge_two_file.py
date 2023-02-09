"""



Q. Joining Two Files and Printing Output - data1_output.txt and data2.txt

This code reads two files, data1_output.txt and data2.txt, and combines the data in them based on a matching character in the data. The code uses the re library to perform regular expression operations and the rsplit method to split strings.

The first file, data1_output.txt, is read line by line and the data is stored in a dictionary with the matching character as the key and the rest of the data as the value. The second file, data2.txt, is also read line by line and the matching character is extracted from each line.

If the matching character is found in the dictionary created from the first file, the rest of the data from both files is combined and printed with a tab as the separator. If the matching character is not found in the dictionary, a line with "- " is printed.

Example Input:
data1_output.txt
abc 123 456
def 789 1011

data2.txt
ghi|abc|jkl 100 200 300
mno|pqr|stu 400 500 600

Example Output:
ghi|abc|jkl 100 200 300 abc 123 456
mno|pqr|stu 400 500 600 - - -
"""
# Importing the re (regular expressions) library 
import re

# Creating an empty dictionary named 'data1_output_dic'
data1_output_dic={}

# Opening two files named 'data1_output.txt' and 'data2.txt' in read mode and storing it in 'file1' and 'file2' respectively
with open ("data1_output.txt","r") as file1, open("data2.txt","r") as file2:
    # Loop over each line in 'file1'
    for line_1 in file1:
        # Strip the line of whitespaces and split the line based on tabs into a list 'a'
        a=line_1.rstrip().rsplit("\t") 
        # Storing the first element of 'a' in the variable 'x'
        x=a[0]
        # Creating a string with tab separated elements from the list 'a'
        y="\t"+a[0]+"\t"+a[1]+"\t"+a[2]
        # Adding the string 'y' as the value for the key 'x' in the dictionary 'data1_output_dic'
        data1_output_dic[x]=y

    # Loop over each line in 'file2'
    for line_2 in file2:
        # Strip the line of whitespaces and split the line based on tabs into a list 'b'
        b=line_2.rstrip().rsplit('\t')
        # Convert the first element of 'b' into a string and store it in 'b1'
        b1=str(b[0])
        # Split 'b1' based on '|' and store the result in a list 'b2'
        b2 = b1.rsplit('|') 
        # If the third element of the list 'b2' is present as a key in the dictionary 'data1_output_dic'
        if b2[2] in data1_output_dic:
            # Print the elements of 'b' joined by tabs, followed by the value of the key 'b2[2]' from the dictionary 'data1_output_dic'
            print(b[0]+"\t"+b[1]+"\t"+b[2]+"\t"+b[3]+data1_output_dic[b2[2]])
        else:
            # If the key 'b2[2]' is not present in the dictionary 'data1_output_dic', print the elements of 'b' joined by tabs, followed by '-' separated by tabs
            print(b[0]+"\t"+b[1]+"\t"+b[2]+"\t"+b[3]+"\t"+"-"+"\t"+"-"+"\t"+"-")


