import statistics


class Calculations(object):
    """The summary line for class of Calculations

    In this class, we initialize on using Attributes directly tied into impact to JIT vs On Demand(see __init__ method below).

    """
    def __init__(self, total_days, results, delay_cost, unit_cost, storage_cost):
        """Class __init__ method.

        Class initialization to capture required attributes to do test runs and executions

        Parameters
        ----------
        results : :obj: 'json', required
            Dictionary of results to test against.
        total_days : :obj:`int` required
            Total execution attempts to run
        delay_cost : :obj:`int`, required
            Cost of a delayed unit
        unit_cost : :obj:`int`, required
            Cost of a unit being sold
        storage_cost : :obj:`int`, required
            Cost of a unit being stored over time
        """
        self._result_payload = results
        self._total_days = total_days
        self._store_inventory = []
        self._customer_demand = []
        self._missed_sales_requests = []
        self._total_made_sales = []
        self._delay_cost = delay_cost
        self._unit_cost = unit_cost
        self._storage_cost = storage_cost
        self._calculated_results = {}

    def gather_all_metrics(self):
        """Module

        Function parameters should be documented in the ``Parameters`` section.
        The name of each parameter is required. The type and description of each
        parameter is optional, but should be included if not obvious.

        If \*args or \*\*kwargs are accepted,
        they should be listed as ``*args`` and ``**kwargs``.

        The format for a parameter is::

            name : type
                description

                The description may span multiple lines. Following lines
                should be indented to match the first line of the description.
                The ": type" is optional.

                Multiple paragraphs are supported in parameter
                descriptions.

        Parameters
        ----------
        starting_store : int
            The overall current store inventory
        customer_demand : int
            The customer demand value for desired inventory
        *args
            Variable length argument list.
        **kwargs
            Arbitrary keyword arguments.

        Returns
        -------
        dict
            Returns dictionary of calculated results

            The return type is a dictionary that can be ingested at a later time for evaluation

            The ``Returns`` section contains dictionary key/pair formatting,
            including literal blocks::

                {
                    'cost_of_storage': int,
                    'units_sold_value': int,
                    'determined_cost_missed_sale': int
                }
                """
        for key, value in self._result_payload.items():
            if value['starting_store'] == 0:
                self._missed_sales_requests.append(value['customer_demand'])
            elif value['starting_store'] != 0:
                if value['customer_demand'] > value['starting_store']:
                    total_sales = value['starting_store']
                else:
                    total_sales = value['customer_demand']
                self._total_made_sales.append(total_sales)
            for key_name in value:
                if key_name == "starting_store":
                    self._store_inventory.append(value[key_name])
                elif key_name == "customer_demand":
                    self._customer_demand.append(value[key_name])
        self._calculated_results['cost_of_storage'] = self.determine_cost_of_storage()
        self._calculated_results['units_sold_value'] = self.determine_units_value_sold()
        self._calculated_results['determine_cost_missed_sale'] = self.determine_cost_of_missed_sales()
        self._calculated_results['total_losses'] = self.determine_total_lost_revenue()
        self._calculated_results['avg_customer_demand'] = self.determine_average_customer_order()
        self._calculated_results['avg_store_inventory'] = self.determine_average_onhand_inventory()
        self._calculated_results['overall profit'] = self.determine_total_profit()
        return self._calculated_results

    def determine_units_value_sold(self):
        total_sales = 0
        for inventory in self._total_made_sales:
            total_sales += inventory * self._unit_cost
        return total_sales

    def determine_cost_of_storage(self):
        total_cost = 0
        for inventory in self._store_inventory:
            if inventory > 1:
                total_cost += inventory * self._storage_cost
        return total_cost

    def determine_cost_of_missed_sales(self):
        total_cost = 0
        for inventory in self._missed_sales_requests:
            total_cost = inventory * self._delay_cost
        return total_cost

    def determine_total_lost_revenue(self):
        return self._calculated_results['determine_cost_missed_sale'] + self._calculated_results['cost_of_storage']

    def determine_total_profit(self):
        return self._calculated_results['units_sold_value'] - self._calculated_results['total_losses']

    def determine_average_customer_order(self):
        return round(statistics.mean(self._customer_demand), 2)

    def determine_average_onhand_inventory(self):
        return round(statistics.mean(self._store_inventory), 2)
