import random


class DataExecutor(object):
    """The summary line for class of DataExecutor

    In this class, we initialize on using Attributes directly to create the required data execution payloads(see __init__ method below).

    """
    def __init__(self):
        """Class __init__ method.

        Class initialization to capture required attributes to do test runs and executions

        Parameters
        ----------
        list_cost_of_inventory : :obj: 'list', required
            Predefined list of headers for inventory key values
        list_shipping_times : :obj: 'list', required
            Predefined list of headers for shipping times key values
        list_of_starting_inventory : :obj: 'list', required
            Predefined list of headers for starting inventory key values
        list_list_of_inventory_trigger_reorders : :obj: 'list', required
            Predefined list of headers for inventory triggering reorder key values
        list_of_reorder_values  : :obj: 'list', required
            Predefined list of headers for inventory reorder key values
        list_of_shipping_failure_rates : :obj: 'list', required
            Predefined list of headers for shipping failure rates key values
        list_of_customer_demand : :obj: 'list', required
            Predefined list of headers for customer demand key values
        dictionary_of_input_variables : :obj: 'dictionary', required
            Empty Dictionary to be appended too with results from class execution
        """
        self._list_cost_of_inventory = ['cost_delayed', 'cost_instock', 'cost_unit']
        self._list_shipping_times = ['store_shipping', 'warehouse_shipping', 'manufacturer_shipping']
        self._list_of_starting_inventory = ['starting_store', 'starting_warehouse', 'starting_manufacturer']
        self._list_of_inventory_trigger_reorders = ['reorder_store', 'reorder_warehouse']
        self._list_of_reorder_values = ['reorder_store_values', 'reorder_warehouse_values',
                                        'reorder_manufacture_values']
        self._list_of_shipping_failure_rates = ['shipping_failure']
        self._list_of_customer_demand = ['customer_demand']
        self.dictionary_of_input_variables = {}

    def build_data_points(self):
        """Module

        This function builds random data points to be used in our model for testing

        Parameters
        ----------
        None

        Returns
        -------
        dict
            Returns dictionary of random values for modeling

            The return type is a dictionary that shows builds the environmental variables for intelligent agent processing

            The ``Returns`` section contains dictionary key/pair formatting,
            including literal blocks::

                {
                  "cost_delayed": int,
                  "cost_instock": int,
                  "cost_unit": int,
                  "store_shipping": int,
                  "warehouse_shipping": int,
                  "manufacturer_shipping": int,
                  "starting_store": int,
                  "starting_warehouse": int,
                  "starting_manufacturer": int,
                  "reorder_store": int,
                  "reorder_warehouse": int,
                  "reorder_store_values": int,
                  "reorder_warehouse_values": int,
                  "reorder_manufacture_values": int,
                  "shipping_failure": int,
                  "customer_demand": int
                }

                """
        for cost in self._list_cost_of_inventory:
            self.dictionary_of_input_variables[cost] = self.randomize_input_numeric_value(1, 3)
        if self.dictionary_of_input_variables['cost_unit'] <= self.dictionary_of_input_variables['cost_delayed'] or \
                self.dictionary_of_input_variables['cost_unit'] <= self.dictionary_of_input_variables['cost_instock']:
            self.dictionary_of_input_variables['cost_unit'] += 13
            self.dictionary_of_input_variables['cost_delayed'] += 3
        for shipping_times in self._list_shipping_times:
            if shipping_times == 'store_shipping':
                self.dictionary_of_input_variables[shipping_times] = self.randomize_input_numeric_value(3, 5)
            elif shipping_times == 'warehouse_shipping':
                self.dictionary_of_input_variables[shipping_times] = self.randomize_input_numeric_value(6, 10)
            elif shipping_times == "manufacturer_shipping":
                self.dictionary_of_input_variables[shipping_times] = self.randomize_input_numeric_value(11, 15)
        for reorder_values in self._list_of_reorder_values:
            if reorder_values == 'reorder_store_values':
                self.dictionary_of_input_variables[reorder_values] = self.randomize_input_numeric_value(100,
                                                                                                        150)
            elif reorder_values == 'reorder_warehouse_values':
                self.dictionary_of_input_variables[reorder_values] = self.randomize_input_numeric_value(500,
                                                                                                        1000)
            elif reorder_values == 'reorder_manufacture_values':
                self.dictionary_of_input_variables[reorder_values] = self.randomize_input_numeric_value(1000,
                                                                                                        10000)
        for starting_inventory in self._list_of_starting_inventory:
            if starting_inventory == 'starting_store':
                self.dictionary_of_input_variables[starting_inventory] = self.randomize_input_numeric_value(100, 200)
            elif starting_inventory == 'starting_warehouse':
                self.dictionary_of_input_variables[starting_inventory] = self.randomize_input_numeric_value(200,
                                                                                                            500)
            elif starting_inventory == 'starting_manufacturer':
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
        return random.randrange(numeric_range_low, numeric_range_high)
