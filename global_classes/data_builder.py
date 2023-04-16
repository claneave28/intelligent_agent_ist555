import random


class DataExecutor(object):

    def __init__(self):

        self._list_cost_of_inventory = ['cost_delayed', 'cost_instock', 'cost_unit']
        self._list_shipping_times = ['store_shipping', 'warehouse_shipping', 'manufacturer_shipping']
        self._list_of_starting_inventory = ['starting_store', 'starting_warehouse', 'starting_manufacturer']
        self._list_of_inventory_trigger_reorders = ['reorder_store', 'reorder_warehouse']
        self._list_of_shipping_failure_rates = ['shipping_failure']
        self._list_of_customer_demand = ['customer_demand']
        self.dictionary_of_input_variables = {}

    def build_data_points(self):

        # Building Out random inputs for each value unless otherwise stated explicitly in the original configuration
        for cost in self._list_cost_of_inventory:
            self.dictionary_of_input_variables[cost] = self.randomize_input_numeric_value(1, 5)
        if self.dictionary_of_input_variables['cost_unit'] <= self.dictionary_of_input_variables['cost_delayed'] or self.dictionary_of_input_variables['cost_unit'] <= self.dictionary_of_input_variables['cost_instock']:
            self.dictionary_of_input_variables['cost_unit'] += 2
        for shipping_times in self._list_shipping_times:
            if shipping_times == 'store_shipping':
                self.dictionary_of_input_variables[shipping_times] = self.randomize_input_numeric_value(1, 5)
            if shipping_times == 'warehouse_shipping':
                self.dictionary_of_input_variables[shipping_times] = self.randomize_input_numeric_value(6, 10)
            else:
                self.dictionary_of_input_variables[shipping_times] = self.randomize_input_numeric_value(11, 15)
        for starting_inventory in self._list_of_starting_inventory:
            if starting_inventory == 'starting_store':
                self.dictionary_of_input_variables[starting_inventory] = self.randomize_input_numeric_value(100,
                                                                                                            200)
            if starting_inventory == 'starting_warehouse':
                self.dictionary_of_input_variables[starting_inventory] = self.randomize_input_numeric_value(200,
                                                                                                            500)
            else:
                self.dictionary_of_input_variables[starting_inventory] = self.randomize_input_numeric_value(1000,
                                                                                                            10000)
        for trigger_reorder in self._list_of_inventory_trigger_reorders:
            if trigger_reorder == 'reorder_store':
                self.dictionary_of_input_variables[trigger_reorder] = self.randomize_input_numeric_value(25, 100)
            else:
                self.dictionary_of_input_variables[trigger_reorder] = self.randomize_input_numeric_value(100, 250)

        for shipping_failure in self._list_of_shipping_failure_rates:
            self.dictionary_of_input_variables[shipping_failure] = self.randomize_input_numeric_value(0, 2)

        for customer_demand in self._list_of_customer_demand:
            self.dictionary_of_input_variables[customer_demand] = self.randomize_input_numeric_value(75, 100)
        return self.dictionary_of_input_variables

    @staticmethod
    def randomize_input_numeric_value(numeric_range_low, numeric_range_high):
        return random.randint(numeric_range_low, numeric_range_high)
