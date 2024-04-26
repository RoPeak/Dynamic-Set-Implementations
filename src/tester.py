from DynamicSet import *
# testing LinkedList-based Implementation
#----------------------------------------
dsll =  DynamicSet_LinkedList()

dsll.add(1)
dsll.add(3)
dsll.add(5)
dsll.add(1)
dsll.set_empty()

try:
    assert (not dsll.set_empty() == True)
    assert (dsll.set_size() == 3)
    assert (dsll.is_element(3))
    assert (dsll.is_element(5))
    assert (dsll.is_element(1))
    assert (not dsll.is_element(8))
    
    dsll.remove(5)
    dsll.remove(3)
    dsll.remove(3)
    dsll.remove(1)
    assert (not dsll.is_element(3))
    assert (dsll.set_empty())
    assert (dsll.set_size()==0)
    print (f"LinkedList Implementation of Dyanmic Set ADT... PASS")
except AssertionError:
    print (f"LinkedList Implementation of Dyanmic Set ADT... FAIL")
    


# testing Array based Implementation
#-----------------------------------
dsa =  DynamicSet_Array(10)

dsa.add(1)
dsa.add(3)
dsa.add(5)
dsa.add(1)
dsa.set_empty()

try:
    assert (not dsa.set_empty() == True)
    assert (dsa.set_size() == 3)
    assert (dsa.is_element(3))
    assert (dsa.is_element(5))
    assert (dsa.is_element(1))
    assert (not dsa.is_element(8))
    
    dsa.remove(5)
    dsa.remove(3)
    dsa.remove(3)
    dsa.remove(1)
    assert (not dsa.is_element(3))
    assert (dsa.set_empty())
    assert (dsa.set_size()==0)
    print (f"Array-based Implementation of Dyanmic Set ADT... PASS")
except AssertionError:
    print (f"Array-based Implementation of Dyanmic Set ADT... FAIL")