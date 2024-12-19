class Node:
    def __init__(self , value ):
        self . value = value
        self . next = None
    # here Node class has a simple constructor with two variables value that stores the data registered to the node
    # and next that is a pointer that will dynamically link the current node to the next one created
class LinkedList:
    def __init__(self):
        self . head = None
        # the head of the list is the constructor but is initialized to none
    def append(self , value):
        newNode = Node( value )
        if not self . head:
            self . head = newNode
            return
        lastNode = self . head # put a contor on the head of the list
        while lastNode . next: # while there is available address transitioning
            lastNode  = lastNode . next  # we are a go
        lastNode . next = newNode  # link new node to the last one
    def display(self):
        current = self . head # start on the head of the list
        while current: # as long as current is not None
            print( current . value , end = "->" )
            current = current . next # going along the list
        print( None )

thisLinkedList = LinkedList()
thisLinkedList . append( 1 )
thisLinkedList . append( 10 )
thisLinkedList . append( 5 )
thisLinkedList . append( "Coddy" )
thisLinkedList . append ( ("Learning programming" , "By solving challenges!") )
thisLinkedList . display()


# 2. Addition of an element. Add an element to a certain position given by a value of that node
class Node:
    def __init__(self , value):
        self . value = value
        self . next = None
    # creating the node
    # create the linked list
class LinkedList:
    def __init__(self):
        self . head = None
    def append(self , value):
        newNode = Node( value )
        if not self . head:
            self . head = newNode
            return
        lastNode = self . head
        while lastNode . next:
            lastNode = lastNode . next
        lastNode . next = newNode
    def display(self):
        current = self . head
        while current:
            print( current . value , end="->" )
            current = current . next
        print( None )
    def Addition(self , tagValue , addedValue):
        current = self . head
        while current . value != tagValue:
            current = current . next
        addedNode = Node( addedValue )
        addedNode . next = current . next
        current . next = addedNode

thisLinkedList = LinkedList()
thisLinkedList . append( 1 )
thisLinkedList . append( 2 )
thisLinkedList . append( 3 )
thisLinkedList . append( 4 )
thisLinkedList .display()
thisLinkedList . Addition( 3 , 444 )
thisLinkedList . display()


# 3. Deletion of node in a linked list. Given a tag value delete that node of the tagged value
class Node:
    def __init__(self , value):
        self . value = value
        self . next = None
class LinkedList:
    def __init__(self):
        self . head = None
    def append(self , value):
        newNode = Node( value )
        if not self . head:
            self . head = newNode
            return
        lastNode = self . head
        while lastNode . next:
            lastNode = lastNode . next
        lastNode . next = newNode
    def display(self):
        current = self . head
        while current:
            print( current . value , end="->" )
            current = current . next
        print( None )
    def delition(self , tagValue):
        current = self . head
        while current . next . value != tagValue:
            current = current . next
        current . next = current . next . next

thisLinkedList = LinkedList()
thisLinkedList . append( 1 )
thisLinkedList . append( 2 )
thisLinkedList . append( 3 )
thisLinkedList . append( "Hello" )
thisLinkedList . append( "Python" )
thisLinkedList . display()
thisLinkedList . delition( 3 )
thisLinkedList .display()


# 4. Insertion at the beginning of the list
class Node:
    def __init__(self, value):
        self . value = value
        self . next = None
class LinkedList:
    def __init__(self):
        self . head = None
    def append(self , value):
        newNode = Node(value)
        if not self . head:
            self . head = newNode
            return
        lastNode = self.head
        while lastNode . next:
            lastNode = lastNode . next
        lastNode . next = newNode
    def display(self):
        current = self . head
        while current:
            print( current . value , end="->" )
            current = current . next
        print( None )
    def insertionAtBeginning(self , value):
        firstNode = Node( value )
        firstNode . next = self . head
        self . head = firstNode

ls = LinkedList()
for i in range( 1 , 6 ):
    ls . append( i )
ls . display()
ls . insertionAtBeginning( 100 )
ls . display()
ls . insertionAtBeginning( "Charlie!" )
ls . display()

# 5. Reverse a linked list. Create a linked list and then reverse it by inverting the pointers
class Node:
    def __init__(self,value):
        self . value = value
        self . next = None
class LinkedList:
    def __init__(self):
        self . head = None
    def append(self , value):
        newNode = Node( value )
        if not self . head:
            self . head = newNode
            return
        lastNode = self . head
        while lastNode . next:
            lastNode = lastNode . next
        lastNode . next = newNode
    def display(self):
        current = self . head
        while current:
            print( current . value , end="->" )
            current = current . next
        print( None )
    def Reversing(self):
        prev = None
        current = self . head
        while current:
            nextNode = current . next
            current . next = prev
            prev = current
            current = nextNode
        self . head = prev

ls = LinkedList()
for i in range( 1 , 11 ):
    ls . append( i )
ls . display()
ls . Reversing()
ls . display()


# 6. Cycle detection. Implement an algorhythm that determines if a linked list has a cycle or not.
# A cycle must have more then 1 element and to close in the starting node.
# well the key idea here is to check if the list has more than 1 element and if there is an element that links with the head
def Check_For_Cycle( linkedList ):
    NoElem = 0
    current = linkedList . head
    while current:
        NoElem += 1
        if current . next == linkedList . head and NoElem > 1:
            return "There is a cycle"
        current = current . next
    return "There is no cycle"
ls = LinkedList()
for i in range(1,10):
    ls . append( i )
curr = ls . head
while curr.next:
    curr = curr . next
curr . next = ls . head
print( Check_For_Cycle( ls ) )


# 7. Create a function that determines the middle of a linked list. If it is odd 1 element, if it is even 2 elements
# in the middle. Be creative
def Middle_of_Linked_List( ls ):
    curr = ls . head
    HowManyNodes = 0
    while curr:
        HowManyNodes += 1
        curr = curr . next
    curr = ls . head
    if HowManyNodes % 2 == 1: # even -> one middle element
        for _ in range( HowManyNodes // 2  ):
            curr = curr . next
        print( f"Middle element: {curr.value}")
    else:
        for _ in range( HowManyNodes // 2 - 1 ):
            curr = curr . next
        print( f"Middle elements: {curr.value} , {curr.next.value}" )

ls = LinkedList()
for i in range( 1 , 10 ):
    ls . append( i )
ls . display()
Middle_of_Linked_List( ls )



# 8. Find the n th element of a given list. Write a function that gets a list and an index n and returns the value at the
# n th node. Make use of any methods that you wish. The nodes indexation starts from 1
ls = LinkedList()
for i in range( 1 , 11 ):
    ls . append( i )
def Find_Nth_Element( lkdLst , n ):
    current = lkdLst . head
    aux = n
    n -= 1
    # we already took into account one elemnt
    while current:
        current = current . next
        n -= 1
        if n == 0:
            return f"{aux}th element of the list is: {current.value}"
    if n != 0:
        return f"Index {aux} exceeds the limit of the list"
ls . display()
print( Find_Nth_Element( ls , 12 ) )


# 9. Merge two sorted linked lists. Create a function Sorting that will take two sorted linked list , simple linked lists
# and will be merge them into a final sorted linked list
def Create_A_List( list1 , list2 ):
    class Node:
        def __init__(self , value):
            self . value = value
            self . next = None
    class linkedListCreation:
        def __init__(self):
            self . head = None
        def append(self , currList ):
            for el1 in currList:
                newNode = Node( el1 )
                if not self . head:
                    self . head = newNode
                else:
                    lastNode = self.head
                    while lastNode.next:
                        lastNode = lastNode.next
                    lastNode.next = newNode
        def display(self):
            current = self . head
            while current:
                print( current . value , end="->" )
                current = current . next
            print(None)

    ls1 = linkedListCreation()
    ls1 . append( list1 )
    ls1 . display()
    ls2 = linkedListCreation()
    ls2 . append( list2 )
    ls2 . display()
    return ls1 , ls2

firstList , secondList = Create_A_List( [1,3,5,7,9] , [2,4,6,8,10,100] )
# constructed the two simple linked lists now to construct the function that will reassign the
def Sorted_List_Merger( lst1 , lst2 ):
    element1 = lst1 . head
    element2 = lst2 . head
    mergedList = LinkedList()
    while element1 is not None and element2 is not None:
        if element1 . value > element2 . value:
            mergedList . append( element2 . value )
            element2 = element2 . next
        elif element1 . value < element2 . value:
            mergedList . append( element1 . value )
            element1 = element1 . next
        # go on the lists accordingly
    # only one loop will be executed now ----> there are still elements either in list1 or in list2
    while element1 is not None:
        mergedList . append( element1 . value )
        element1 = element1 . next
    while element2 is not None:
        mergedList . append( element2 . value )
        element2 = element2 . next
    return mergedList

merged_list = Sorted_List_Merger( firstList , secondList )
current = merged_list.head
while current:
    print(current.value, end="->")
    current = current.next
print(None)


# 10. Find the intersection point in two linked list objects if they have such a thing. An intersection point its a node with the same address for both
# lists. Attention: not the same value in different appended nodes
def Creating_Two_Intersected_Lists():
    class Node:
        def __init__(self,value):
            self . value = value
            self . next = None
    class LkdLst:
        def __init__(self):
            self . head = None
        def append(self , value):
            newNode = Node( value )
            if not self . head:
                self . head = newNode
                return
            lastNode = self . head
            while lastNode . next:
                lastNode = lastNode . next
            lastNode . next = newNode
        def display(self):
            it = self . head
            while it:
                print( it . value , end="->" )
                it = it . next
            print( None )
    ls1 = LkdLst()
    ls1 . append( "Emma" )
    ls1 . append( "Charlie" )

    ls2 = LkdLst()
    ls2 . append( "Echo" )
    ls2 . append( "Zulu" )

    commonNode = Node( "Bravo" )

    it1 = ls1 . head
    it2 = ls2 . head
    # integrate common node into the 2 lists
    while it1 . next:
        it1 = it1 . next
    it1 . next = commonNode
    while it2 . next:
        it2 = it2 . next
    it2 . next = commonNode
    # now continue to add the junction has been made

    ls1 . append( "Bob" )
    ls1 . append( "Alice" )

    ls2 . append( "Alpha" )

    ls1 . display()
    ls2 . display()

    commonNodes = {}
    it1 = ls1 . head
    while it1:
        if id( it1 ) not in commonNodes:
            commonNodes[id(it1)] = it1 . value
        it1 = it1 . next
    it2 = ls2 . head
    while it2:
        if id(it2) not in commonNodes:
            commonNodes[id(it2)] = it2 . value
        else:
            if it2 . value == commonNodes[id(it2)]:     # return the first common node
                return f"There is an intersection in the two lists: {it2.value , it2}"
        it2 = it2 . next
    return "There is no intersection of the 2 lists"

print(Creating_Two_Intersected_Lists())



# 10. Rotate a linked list with a given number of positions. Also create the simple linked list and rotate to right(clockwise)
def List_Rotation_To_Right():
    class Node:
        def __init__(self,value):
            self . value = value
            self . next = None
    class LkdLst:
        def __init__(self):
            self . head = None
        def append(self,value):
            newNode = Node(value)
            if not self . head:
                self . head = newNode
            lastNode = self . head
            while lastNode . next:
                lastNode = lastNode . next
            lastNode . next = newNode
        def display(self):
            it = self . head
            while it:
                print( it . value , end="->" )
                it = it . next
            print( None )
    list1 = LkdLst()
    list1 . append( 1 )
    list1 . append( 2 )
    list1 . append( 3 )
    list1 . display()

List_Rotation_To_Right()






#  ====================== FROM HERE ON THE DOUBLE LINKED LISTS ARE IN DISCUSSION ===========================
# Double linked lists are structure like simple linked list but with the additional property that one can go to the
# previous node by memory directioning i.e. pointers
# consists of Node creation and of course the list creation
# lets call the knowledge about classes to do this
class Node:
    def __init__(self , value): # in constructor we initialize the value of the node and directionals
        self . value = value # assigning
        self . next = None  # next node directional
        self . prev = None # previous node directional
class DoubleLinkedList:
    def __init__(self):
        self . head = None # the head of the list must still exist and its firstly unknown
        self . tail = None
    def append(self , value):
        newNode = Node( value )
        if not self . head:
            self . head = newNode
            return
        lastNode = self . head
        while lastNode . next:
            lastNode = lastNode . next
        lastNode . next = newNode
        newNode . prev = lastNode
        self . tail = newNode
    def displayNext(self):
        current = self . head
        while current:
            print( current . value , end="->" )
            current = current . next
        print(None)
    def displayPrev(self):
        current = self . tail
        while current:
            print( current . value , end="->" )
            current = current . prev
        print(None)
dls = DoubleLinkedList()
dls . append( 1 )
dls . append( 2 )
dls . append( 3 )
dls . append( 4 )
#dls . displayNext()
#dls . displayPrev()