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
