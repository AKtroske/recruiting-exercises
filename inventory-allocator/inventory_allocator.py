class InventoryAllocator:

    def process_order(self, order, warehouses):
        """
            Process order by finding the cheapest shipment given order and inventory variables.

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

        if not self.validate_order(order):
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

                    # Inventory can't satisfy order for item -> amt_to_take is all of inventory then clear inventory
                    if inventory[item] - order[item] <= 0:
                        amt_to_take = inventory[item]
                        order[item] -= inventory[item]
                        del inventory[item]
                    # Inventory can satisfy order for item -> amt_to_take is equal to the order amount
                    else:
                        amt_to_take = order[item]
                        order[item] = 0

                    # Create new warehouse object if warehouse not in final shipment list
                    if name not in names_index:
                        warehouse = { name : { item : amt_to_take } }
                        names_index[name] = len(final_shipment) # add to end of names
                        final_shipment.append(warehouse)
                    # Names_order[name] == index of warehouse in final shipment. Add (item : amt_to_take ) pair
                    else:
                        final_shipment[names_index[name]][name][item] = amt_to_take

                i += 1

        print(final_shipment)
        return final_shipment

    def validate_order(self, order):
        """
        Parameters
        ----------
            order: dict - { item : quanitity, ... }
                A dict. of items with corresponding quantities to be filled

        Returns
        ----------
            valid - bool describing validity of order
        """

        def remove_empty_items(order):
            """
            Checks and removes ordered items that have quantity greater than zero
            Parameters
            ----------
                order: dict - { item : quanitity, ... }
                    A dict. of items with corresponding quantities to be filled
            Returns
            ----------
                cleaned: dict - { item : quanitity, ...}
                    All items have quantity > 0
            """

            cleaned = [k for k, v in order.items() if v > 0]
            return cleaned

        order = remove_empty_items(order)

        return True
