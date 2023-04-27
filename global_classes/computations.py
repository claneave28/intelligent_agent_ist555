import statistics


class Calculations(object):
    """The summary line for class of Calculations

    In this class, we initialize on using Attributes directly tied into (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes
    ----------
    attr1 : str
        Description of `attr1`.
    attr2 : :obj:`int`, optional
        Description of `attr2`.

    """
    def __init__(self, total_days, results, delay_cost, unit_cost, storage_cost):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note
        ----
        Do not include the `self` parameter in the ``Parameters`` section.

        Parameters
        ----------
        param1 : str
            Description of `param1`.
        param2 : :obj:`list` of :obj:`str`
            Description of `param2`. Multiple
            lines are supported.
        param3 : :obj:`int`, optional
            Description of `param3`.

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
        param1 : int
            The first parameter.
        param2 : :obj:`str`, optional
            The second parameter.
        *args
            Variable length argument list.
        **kwargs
            Arbitrary keyword arguments.

        Returns
        -------
        bool
            True if successful, False otherwise.

            The return type is not optional. The ``Returns`` section may span
            multiple lines and paragraphs. Following lines should be indented to
            match the first line of the description.

            The ``Returns`` section supports any reStructuredText formatting,
            including literal blocks::

                {
                    'param1': param1,
                    'param2': param2
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
