#!/usr/bin/env python

#Find the first occurence of the words 'not' and 'good'.
#If not proceeds good, change the whole string to 'bad'




input1 = input ("please input1:")

if input1.find("not") < input1.find("good"):
    not_index = input1.find("not")
    good_index = input1.find("good")
    mysubstr = input1[not_index:(good_index+4)]
    print (input1.replace(mysubstr, "bad"))
else:
    print (input1)        




#print merge
#print ("bye")
