

#### Akahi Troske Inventory Allocator Solution

My solution to Deliverr's [Inventory Allocation](https://github.com/deliverr/recruiting-exercises/tree/master/inventory-allocator) recruiting exercise problem. Solved using python and pytest.

## Prerequisites

..* python3
..* pytest

## Testing

Tests are located in test_inventory_allocator.py file and are written and run using pytest.

To run tests:
```
  pytest
```
To run tests displaying input (order, warehouses) and output (final shipment):
```
  pytest -s
```

## Assumptions

..* The algorithm assumes both inputs always exists. Both inputs may be empty, ```{}``` or ```[]``` respectively.
..* If an order cannot be filled (invalid) then an empty list is returned.

## Author
Akahi Troske - akahitroske@gmail.com
