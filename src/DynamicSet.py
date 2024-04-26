#########################################################################################
#                                                                                       #
#                                      PART 3                                           #
#                                                                                       #
#########################################################################################

import random
import time
import os

# A class to represent a node in a doubly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    
    # Getters
    def get_val(self):
        return self.value

    def get_prev(self):
        return self.prev
    
    def get_next(self):
        return self.next

    # Setters
    def set_val(self, value):
        self.value = value

    def set_prev(self, prev):
        self.prev = prev 
    
    def set_next(self, next):
        self.next = next

# A class to represent a doubly linked list
class DynamicSet_LinkedList:
    # Constructor to create a new empty set of given size
    def __init__(self):
        self.head = None
        self.tail = None

    # Method for adding new element to the set
    def add(self, x):
        # Check if value is already in the set, returning if so
        if self.is_element(x):
            return

        nodeX = Node(x)
        # Check if this is the first node to be added, making it the head and tail if so
        if self.set_empty():
            self.head = nodeX
            self.tail = self.head
            return
    
        # Otherwise insert the node at the end of the set by updating the tail pointer
        temp = nodeX
        temp.set_prev(self.tail)
        self.tail.set_next(temp)
        self.tail = temp

    # Method for removing element from the set
    def remove(self, x):
        # First check whether x is even in the set, returning if not
        if self.is_element(x):
            pointerNode = self.head
            nodeX = None
            # Traverse the set, looking for x (stop once it is found) 
            while pointerNode is not None:
                if pointerNode.get_val() == x:
                    nodeX = pointerNode
                    break
                pointerNode = pointerNode.get_next()

            # Corner case handling for if x is the only element in the set
            # i.e. it is both the head and the tail
            if self.head == nodeX and self.tail == nodeX:
                self.head = None
                self.tail = None
                return

            # Otherwise, remove the node found to store x using appropriate method
            if self.head == nodeX:
                self.head = nodeX.get_next()
                self.head.set_prev(None)
            elif self.tail == nodeX:
                self.tail = nodeX.get_prev()
                self.tail.set_next(None)
            else:
                nextNode = nodeX.get_next()
                prevNode = nodeX.get_prev()
                nextNode.set_prev(prevNode)
                prevNode.set_next(nextNode)
        else:
            # x is not in set
            return

    # Method for checking if element is in the set
    def is_element(self, x):
        pointerNode = self.head

        # Traverse the set, looking for x (stop once tail is reached or it is found) 
        while pointerNode is not None and pointerNode.value != x:
            pointerNode = pointerNode.next

        # Return True/False indicating whether node was found
        return True if pointerNode else False
        
    # Method for checking if set is empty
    def set_empty(self):
        # If there exists a head node, return True else return False to show empty set 
        return self.head is None

    # Method for returning the number of elements in the set
    def set_size(self):
        nodes = 0
        pointerNode = self.head
        # Loop through, counting nodes until you reach the tail
        while pointerNode is not None:
            nodes += 1
            pointerNode = pointerNode.get_next()
        return nodes
    
    # Function 'traverse_nodes' is outwith exercise specification
    # Purely used to help me visualise the doubly linked list
    def traverse_nodes(self):
        pointerNode = self.head
        nodeCounter = 1
        while pointerNode is not None:
            print("**** Node " + str(nodeCounter) + " ****")
            print("Previous Node: " + str(pointerNode.get_prev()))
            print("Value: " + str(pointerNode.get_val()))
            print("Next Node: " + str(pointerNode.get_next()))
            print()
            nodeCounter += 1
            pointerNode = pointerNode.get_next()


# A class to represent a doubly linked list
# Array values will be stored sequentially i.e. all None values will be stored at the end
class DynamicSet_Array:
    def __init__(self, size):
        self.values = [None] * size
        self.size = size

    # Method for adding new element to the set
    def add(self, x):
        # Check if value is already in the set, returning if so
        if self.is_element(x):
            return
        
        # Iterate through array, finding first None value 
        # and setting it to the supplied x value
        for i in range(self.size):
            if self.values[i] is None:
                self.values[i] = x
                return
        
        # If this code is reached, then the array is full -- overflow error
        print("Error: Overflow")

    # Method for removing element from the set
    def remove(self, x):
        # First check whether x is even in the set, returning if not
        if self.is_element(x):
            # Find where x is in array and set value to None
            position = self.values.index(x)
            self.values[position] = None
            
            # Shift up all non-None values
            for i in range(position, self.size - 1):
                if self.values[i + 1] is not None:
                    self.values[i] = self.values[i + 1]
                    self.values[i + 1] = None

    # Method for checking if element is in the set
    def is_element(self, x):
        return x in self.values

    # Method for checking if set is empty
    def set_empty(self):
        isEmpty = True
        # Loop through array, stopping at first non-None value
        for i in range(self.size):
            if self.values[i] is not None:
                isEmpty = False
                break

        # Return True/False value, depending on whether non-None value was found in array
        return isEmpty

    # Method for returning the number of elements in the set
    def set_size(self):
        elements = 0
        for element in self.values:
            if element is not None:
                elements += 1
            else:
                # First time a None value is encountered means end of set values
                break
        return elements
    

#########################################################################################
#                                                                                       #
#                                      PART 4                                           #
#                                                                                       #
#########################################################################################
#DONE: Create empty Linked List set "S"
#DONE: Read in all numbers from "Int20k.txt" and add them to "S"
#DONE: Generate 100 random numbers between 0 and 49999
#DONE: Record time to find each random number "x" in "S" (using is_element method)
#DONE: Write time to file "results_problem4.txt"
#DONE: Redo steps 2-5 but for an Array set
#DONE: Calculate average time of is_element over 100 calls (for each implementation)

def run_test(S, implementation, times_list, randomNumbers):
    # Read in all integers from file and add them to the given set S
    print("********** " + implementation + " **********")
    with open(os.getcwd() + "\\resource\\Int20k.txt", "r") as file:
        for integer in file:
            value = int(integer.strip())
            S.add(value)
    print("Numbers added to " + implementation + ".")


    # Gather the times to find each element and write them to file
    writeMode = "w" if implementation == "Linked List" else "a"
    with open("results_problem4.txt", writeMode) as file:
        file.write("Results for " + implementation + " based implementation\n")
        for number in randomNumbers:
            start = time.perf_counter()
            S.is_element(number)
            stop = time.perf_counter()
            performanceTime = (stop - start) * 1000
            file.write(str(performanceTime) + "\n")
            times_list.append(performanceTime)
        print("Results written to file.")
    print("*******************************")

# Main method to run operations for part 4
def main():
    # Generate 100 random numbers
    randomNumbers = []
    for i in range(100):
        randomNumbers.append(random.randint(0, 49999))
    print("Random numbers generated.")
    
    S = DynamicSet_LinkedList()
    LL_Times = []
    run_test(S, "Linked List", LL_Times, randomNumbers)

    S = DynamicSet_Array(19999)
    A_Times = []
    run_test(S, "Array", A_Times, randomNumbers)

    LL_Average = sum(LL_Times)/len(LL_Times)
    print("Average time for Linked List: " + str(LL_Average))
    A_Average = sum(A_Times)/len(A_Times)
    print("Average time for Array: " + str(A_Average))

    # Producing scatter plot for report (uses a script I wrote in a different file --- plotter.py)
    import plotter
    plotter.create_scatter_plot(LL_Times, A_Times)

# Uncomment this line to generate problem .txt file 
main()