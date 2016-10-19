#!/usr/bin/env python

input1 = input ("please input1:")
input2 = input ("please input2:")

input1len = len(input1)
input2len = len(input2)

input1last = input1[input1len-1]
input2last = input2[input2len-1]
print (input1[0]+input1last + input2[0] + input2last)
merge = input1[0]+input1last + input2[0] + input2last

#print merge
#print ("bye")
