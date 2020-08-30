class InventoryAllocator:

    def process_order(self, order, warehouses):
        """
            Process order by finding the cheapest shipment given order and inventory variables. Items are filled as passed in.
            For each item, iterate through warehouses until order is 0 (filled) or all warehouses checked (order can't be filled).

            Parameters
            ----------
                order: dict - { item : quanitity, ... }
                    A dict. of items with corresponding quantities to be filled
                warehouses: list[dict] - [{ name : 'x', inventory : { item : quantity, ...}}, ...]
                    A list of dict. with name and inventory keys. Inventory represented
                    by item : quantity pair. Order from cheapest to most expensive.

            Returns
            ----------
                shipment: list[dict] - [{name : { item: quanitity, ... }}, ...]
        """

        print("Order: ")
        print(order)
        print("Warehouses: ")
        print(warehouses)
        order, warehouses = self.remove_empty_items(order, warehouses)

        if len(order) == 0:
            return []

        if len(warehouses) == 0:
            return []

        final_shipment = []
        names_index = {}

        for item in order:
            i = 0
            # Iterate until we have checked every warehouse or we have satisfied the quantity for item
            while order[item] > 0 and i < len(warehouses):

                inventory = warehouses[i]['inventory']
                name = warehouses[i]['name']

                if item in inventory:

                    # Inventory can't satisfy order for item -> amt_to_take is all of inventory - clear inventory
                    if inventory[item] - order[item] <= 0:
                        amt_to_take = inventory[item]
                        order[item] -= inventory[item]
                        del inventory[item]
                    # Inventory can satisfy order for item -> amt_to_take is equal to the order amount
                    else:
                        amt_to_take = order[item]
                        order[item] = 0

                    # Create new warehouse object if warehouse not in final shipment
                    if name not in names_index:
                        warehouse = { name : { item : amt_to_take } }
                        names_index[name] = len(final_shipment) # add to end of names
                        final_shipment.append(warehouse)
                    # Names_order[name] == index of warehouse in final shipment. Add (item : amt_to_take ) pair
                    else:
                        final_shipment[names_index[name]][name][item] = amt_to_take

                i += 1

            # Check if order for specific item has been satisfied
            if i == len(warehouses) and order[item] > 0:
                return []

        print("Final shipment: ")
        print(final_shipment)
        return final_shipment

    def remove_empty_items(self, order, warehouses):
        """
        Checks and removes ordered items that have quantity greater than zero using list, dict comprehension

        Parameters
        ----------
            order: dict - { item : quanitity, ... }
                A dict. of items with corresponding quantities to be filled
        Returns
        ----------
            cleaned: dict - { item : quanitity, ...}
                All items have quantity > 0
        """

        cleaned_order = {k:v for (k, v) in order.items() if v > 0}
        cleaned_warehouses =  [{'name':warehouse['name'], 'inventory':{k:v for k, v in warehouse['inventory'].items() if v > 0}} for warehouse in warehouses]
        return cleaned_order, cleaned_warehouses

if __name__ == '__main__':
    ia = InventoryAllocator()
