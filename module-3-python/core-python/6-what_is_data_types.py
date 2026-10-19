# # print a dtatypes of variables
# a=10.05
# print(a)
# print(type(a))

# a=10
# print(a)
# print(type(a))

# name='abc'
# print(name)
# print(type(name))

# #int
# # accept number
# # a=10
# #b=144555

# # string
# # string is a set of character
# #  string enclosed within '' or ""
# # a=name='bhavika'
# # name1="hey bhavika"
# # print(a)
# # print(name)
# # print(name1)

# # integer
# # stored numbers or integer values in variables.
# a=10
# b=20214436547658
# c=3334567
# print(a)
# print(b)
# print(c)
# print(type(c))

# # type casting is used to change the data type to anthor data type.
# # string to float
# a=int("10")
# b=20
# c=a+b
# print(c)

# # convert into string to int
# a=int(input("enter a value:"))
# b=int(input("enter b value"))
# c=a*b
# print(c)

# comlax data type
# a=2+3j
# print(type(a))

# #boolean
# a=Trueb=False
# print(type(a))
# print(type(a))

# # float
# a=10.8867
# print(type(a))

# # type casting for float value
# a=float(input("enter a value:"))
# b=float(input("enter b value"))
# c=a*b
# print(c)

print("-------dictonary:---------")
# stored data inside of {key:value}
# dictonary provides mutable data can be changed
employee={
    "id":1,
    "name":"abc",
    "age":32
    }
print(employee)
print(type(employee))
print(employee["name"])

print("-------list:---------")
# stored data inside of[]
# list provides mutable data can be changed

employee=["a","2",30.5,True]
print(employee)
print(type(employee))
print(employee[0])
print(employee[2])

print("-------tuple:---------")
# tuple is a data type of python
# tuple provides immutable data can not be changed
employee=("a",2,20.3,False)
print(employee)
print(type(employee))
print(employee[1])

print("-------set:---------")
# set is also a datatype of python
# set is also stored data inside of {}
# ex -> {"a","b","c",284,28.5,True}
employee={"a","b","c",284,28.5,True}
print(employee)
print(type(employee))