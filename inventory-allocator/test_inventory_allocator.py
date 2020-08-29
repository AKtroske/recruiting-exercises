import pytest

from inventory_allocator import InventoryAllocator

ia = InventoryAllocator()

def test_1():
    print("\n\nRunning tests...\n--------------------------------")
    print("Test 1 ...")
    assert [{'warehouse36': {'aa': 2}}] == ia.process_order({'aa':2}, [{'name':'warehouse36','inventory':{'a':3, 'aa':3, 'aaa': 3}}])

def test_2():
    print("Test 2 ...")
    assert [
        {'abc': {'apple': 6, 'orange': 6}},
        {'ghi': {'apple': 4}},
        {'def': {'orange': 1, 'banana': 4}}
    ] == ia.process_order({'apple': 10, 'orange': 7, 'banana': 4}, [
        {'name': 'abc', 'inventory': {'apple': 6, 'orange': 6}},
        {'name': 'def', 'inventory': {'banana': 4, 'orange': 1}},
        {'name': 'ghi', 'inventory': {'banana': 3, 'orange': 3, 'apple': 5}}
    ])
