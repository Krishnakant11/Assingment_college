# 1 Write a program to print Hello world
def practical_1():
    print("Hello World")

# 2 Write a program to Hello world using string variable
def practical_2():
    hello_python = "Hello World"
    print(hello_python)

# 3 Write a program to store data in list and then try to print them
def practical_3():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(data)

# 5 Write a program to store strings of numbers using range an for loop
def practical_5():
    natural_number = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
    for number in range(4, len(natural_number)):
        print(natural_number[number])


# 6 Write a program to store string in list then try to print them
def practical_6():
    sr_data = ["char", "int", "float", "boolean", "double"]
    print(sr_data)

# 7 Write a program to let user enter data in string and then try to print welcome user
def practical_7():
    name = input("Enter your name :")
    print("Welcome "+name + "!")

# 8 Write a program in which an function is defined and calling that function prints Hello world

def practical_8():
    return print("Hello World")
    practical_8()

# 9 Write a program in which an function(with single parameter )is defined and calling that function prints the string parameter given to funciton


def practical_9(user_var):
    user_var = input("Enter your name:")
    print("Welcome " + user_var + " to python programming")

# 10 write a program in which an class define then create object of that class and call simple print fuction define in class

# define a function name called student
class practical_10():

    def __init__(self , name, branch_of_college, college) -> None:
        self.name = name
        self.branch_of_college = branch_of_college
        self.college = college
