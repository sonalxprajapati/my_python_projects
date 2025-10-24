
"""VARIABLES: is a named "container" for a value"""""

"""DATATYPES: int, float, str"""
a=100 # integer (int): whole number
temperature=31.45 #float (float): decimal number
name="pypypy" #string (str): text, characters, "" or '' used

"""OPERATORS: + - * / // %"""
#// (floor div) divides and  rounds down to the nearest whole number
# % (modulo operator) gives the remainder of a division
result=12/2
print(result) #->> results to 6.0
result1=12//2
print(result1) #->> results to 6
result2=10%3
print(result2) #->> results to 1

"""LIST: Collection of items stored within [] and separated by commas"""
"""index starts from 0, syntax=name[index]"""
""" .append() adds a new item to the end"""
primeNUM=[1,2,3,5,7,11] #integers
vowels=["a","e","i","o","u"] #string
data=["arjun",162,0.2] #mixed datatype
title=data[0]
height=data[1]
print(title)
print(height)
data.append("SS")
print(data)
rank=data[3]
print(rank)
data[2]="36degrees"
temp=data[2]
print(temp)

"""TUPLES: Collection of items similar to list but immutable, () is used"""
coordinates = (10, 20)
student_info = ("Priya", "Computer Science", "Sophomore")
student_name = student_info[0]
major = student_info[1]
print(student_name,",",major)
student_info[2] = "Junior" #->> causes TypeError

""" f string printing """
print(f"I am {5*9} years old")