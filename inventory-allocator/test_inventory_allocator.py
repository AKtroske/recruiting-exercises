import pytest

from inventory_allocator import InventoryAllocator

ia = InventoryAllocator()

def test_1():
    print("\n\nRunning tests...\n--------------------------------")
    print("Test 1 ...")
    assert [
        {'w1': {'a': 2}}
    ] == ia.process_order({'a':2}, [
        {'name':'w1','inventory':{'a':3, 'aa':3, 'aaa': 3}}
    ])

def test_2():
    print("\nTest 2 ...")
    assert [
        {'w1': {'apple': 6, 'orange': 6}},
        {'w3': {'apple': 4}},
        {'w2': {'orange': 1, 'banana': 4}}
    ] == ia.process_order({'apple': 10, 'orange': 7, 'banana': 4}, [
        {'name': 'w1', 'inventory': {'apple': 6, 'orange': 6}},
        {'name': 'w2', 'inventory': {'banana': 4, 'orange': 1}},
        {'name': 'w3', 'inventory': {'banana': 3, 'orange': 3, 'apple': 5}}
    ])

# Test invalid order
def test_3():
    print("\nTest 3 ... Order cannot be filled")
    assert [] == ia.process_order({'apple':5}, [
        {'name':'w1', 'inventory':{'apple':2}},
        {'name':'w2', 'inventory':{'apple':2}}
    ])

# Test remove empty-items
def test_4():
    print("\nTest 4 ... Test removing empty items")
    co, cv = ia.remove_empty_items({'apple':-1}, [{'name':'a', 'inventory':{'apple':-10, 'banana':-15, 'choco':10}}, {'name':'b', 'inventory':{'b_apple':-10, 'b_banana':-15, 'b_choco':10}}])
    assert co == {} and cv == [{'name': 'a', 'inventory': {'choco': 10}}, {'name': 'b', 'inventory': {'b_choco': 10}}]

# Example 1 from github
def test_5():
    print("\nTest 5 ... Example 1 from problem statement")
    assert [{'owd': {'apple':1}}] == ia.process_order({'apple':1}, [
        {'name': 'owd', 'inventory' : {'apple':1}}
    ]
    )

# Example 2 from github
def test_6():
    print("\nTest 6 ... Example 2 from problem statement")
    assert [{'owd': {'apple':5}}, {'dm': {'apple':5}}] == ia.process_order({'apple':10}, [
        {'name': 'owd', 'inventory' : {'apple':5}},
        {'name': 'dm', 'inventory' : {'apple':5}}
    ]
    )

# Example 3 from github
def test_7():
    print("\nTest 7 ... Example 3 from problem statement - Order cannot be shipped because there is not enough inventory")
    assert [] == ia.process_order({'apple':1}, [
        {'name':'owd', 'inventory':{'apple':0}},
    ])

def test_8():
    print("\nTest 8 ... Example 4 from problem statement - Order cannot be shipped because there is not enough inventory")
    assert [] == ia.process_order({'apple':2}, [
        {'name':'owd', 'inventory':{'apple':1}},
    ])

# Empty order
def test_9():
    print("\nTest 9 ... Empty order")
    assert [] == ia.process_order({}, [
        {'name':'owd', 'inventory':{'apple':1}},
    ])

def test_10():
    print("\nTest 10 ... Empty warehouses")
    assert [] == ia.process_order({'apple':1}, [])

def test_11():
    print("\nTest 11 ... Empty warehouses")
    assert [{'w1': {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}}] == ia.process_order(
        {'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1},
        [{'name':'w1','inventory':{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1}}]
    )
