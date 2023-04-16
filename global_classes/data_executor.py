import random


class DataExecutor(object):

    def __init__(self, random_input=False, **kwargs):

        self._random_inputs = random_input
        self._list_cost_of_inventory = ['delayed', 'instock', 'unit']
        self._list_shipping_times = ['store', 'warehouse', 'manufacturer']
        self._list_of_starting_inventory = ['store', 'warehouse', 'manufacturer']
        self._list_of_inventory_trigger_reorders = ['store', 'warehouse']
        self._list_of_shipping_failure_rates = ['shipping_failure']
        self._list_of_customer_demand = ['customer_demand']
        self.dictionary_values = kwargs
        self.dictionary_of_input_variables = {}
        self.build_data_points = self.build_data_points()

    def build_data_points(self):
        if self._random_inputs:
            # start with cost of inventory building
            for cost in self._list_cost_of_inventory:
                self.dictionary_of_input_variables[cost] = self.randomize_input_numeric_value(1, 5)
            for shipping_times in self._list_shipping_times:
                if shipping_times is 'store':
                    self.dictionary_of_input_variables[shipping_times] = self.randomize_input_numeric_value(1, 5)
                if shipping_times is 'warehouse':
                    self.dictionary_of_input_variables[shipping_times] = self.randomize_input_numeric_value(6, 10)
                else:
                    self.dictionary_of_input_variables[shipping_times] = self.randomize_input_numeric_value(11, 15)
            for starting_inventory in self._list_of_starting_inventory:
                if starting_inventory is 'store':
                    self.dictionary_of_input_variables[starting_inventory] = self.randomize_input_numeric_value(100,
                                                                                                                200)
                if starting_inventory is 'warehouse':
                    self.dictionary_of_input_variables[starting_inventory] = self.randomize_input_numeric_value(200,
                                                                                                                500)
                else:
                    self.dictionary_of_input_variables[starting_inventory] = self.randomize_input_numeric_value(1000,
                                                                                                                10000)

    @staticmethod
    def randomize_input_numeric_value(numeric_range_low, numeric_range_high):
        return random.randint(numeric_range_low, numeric_range_high)
