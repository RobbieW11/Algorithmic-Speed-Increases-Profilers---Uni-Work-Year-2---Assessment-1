import  random
import time
import string
import bisect
from  collections import deque
import matplotlib.pyplot as plt

#you will need to import matlibplot your self. don't forget to indlue

"""
Correct format strings for O(N?)  answers 

O(1)
O(LOG(N))
O(N) 
O(N LOG(N))
O(N**2)
O(N**2 LOG(N))
O(N**3) 
O(N**4) 
O(2**N)
O(N!) 

"""

# The developer left this code below



d = deque()   #Alter this code
d = []
#more developer code was here but you don't need to know about it.

def Question1Example(d , K:int ) : #DO NOT ALTER THIS CODE
	for i in range(K):   #Do not Alter this code
    		d[ len(d)//2   ] = 6  #Do not Alter this code
def Question1_a():
    return "O(N)" # If using N use N and if power use N**"
def Question1_c():
    return "O(1)" # If using N use N and if power use N**"


#------------------------------------------------
Q2 =  list() # list() #Alter this code
Q2 = deque()

#the collection is filled in the assessment code.
#there is more code showing extensive use of list access.

def Question2Example( Q2, K:int ) :
	for i in range(K):      #Do not Alter this code
    		Q2.insert(0,i) #Do not Alter this code

def Question2_a():
    return "O(N)"

def Question2_c():
    return "O(1)"

#------------------------------------------------
Q3 = set()   # OK to alter this

def Question3ExampleADD( Q3, item :int ) :
    # OK TO CHANGE THE CODE BELOW TO HELP
    Q3.add(item )

def Question3ExampleFind( Q3 , What ):
    #OK TO CHANGE THE CODE BELOW TO HELP
    if What in Q3:
            return True
    #end for
    return False #not found

def Question3_a():
    return "O(N)"

def Question3_c():
    return "O(1)"

#------------------------------------------------
Q4 = {}  #[ "fhfh" , "djdjd", "wewew"]
Q4_index = 0  # [ 0, 1, 2]

def Question4ExampleADD( Q4, item :str ) :
    # OK TO CHANGE THE CODE BELOW TO HELP
    global Q4_index
    if item not in Q4:
        Q4[item] = Q4_index
        Q4_index += 1

# So if user asks for What =  "djdjd" return 1
def Question4ExampleFind( Q4 , what ):
    #OK TO CHANGE THE CODE BELOW TO HELP
    return Q4.get(what, -1)
    #end for

# What is the O notation for Question4ExampleFind
def Question4_a():
    return "O(N)"
# What is the O notation for Question4ExampleFind after you fix it
def Question4_c():
    return "O(1)"

#------------------------------------------------
Q5a = set()
Q5b = set()
def Question5Add(  Q5a , whattoAdd_A , Q5b,  whatToAdd_B ):
    # OK TO change the code below to help
    Q5a.add( whattoAdd_A)
    Q5b.add( whatToAdd_B )

#return a itterable collection of everything in A which is in B
# Order is not important in the collection
def Question5Find( Q5a , Q5b )  :
    return list(set(Q5a) & set(Q5b))

def Question5_a():
        return "O(N**2)"

    # What is the O notation for Question4ExampleFind after you fix it
def Question5_c():
        return "O(1)"

#------------------------------------------------
Q6 = deque()
def Question6WhatIsMyONotation(  items ):   # DO NOT ALTER THIS CODE
    global Q6
    for it in items:
        Q6.insert(  len( Q6) //2 , it )

def Question6():
            return "O(N**2)"

#------------------------------------------------
Q7 = set()
def Question7WhatIsMyONotation( item )-> bool:
    return item in Q7

def Question7():
    return "O(1)"

#------------------------------------------------
Q8 = list() # don't change this
def Question8WhatIsMyONotation( Q8 , item )-> int :
        index = bisect.bisect_left(Q8, item)

        if index < len(Q8) and Q8[index] == item:
            return index  # Item found
        else:
            return -1  # Item not found

def Question8():
    return "O(LOG(N))"

#------------------------------------------------
Q9  = [random.uniform(-100, 100) for _ in range(10000)]

def Question9WhatIsMyTime(Q9) :
    return Q9.sort( )

def Question9():
    # Your code wraps around test
    global Q9
    start_time = time.perf_counter()
    Question9WhatIsMyTime(Q9)
    end_time = time.perf_counter()
    # Your code wraps around test
    execution_time = (end_time - start_time) * 1000
    return execution_time

#------------------------------------------------
def Question10():
    function_time = []
    Q9_size = []
    global Q9
    for x in range(0, 100, 10):
        Q9 = [random.uniform(-100, 100) for _ in range(10000*x)]
        Q9_size.append(len(Q9))
        function_time.append(Question9())


    plt.plot(Q9_size, function_time, label='Execution Time')
    plt.xlabel('Number of Elements')
    plt.ylabel('Time to Execute (seconds)')
    plt.title('Function Execution Performance')
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()
    pass

Question10()