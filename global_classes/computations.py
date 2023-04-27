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

        This function builds out the findings from the inputted variables in the agent model

        Parameters
        ----------
        starting_store : int
            The overall current store inventory
        customer_demand : int
            The customer demand value for desired inventory

        Returns
        -------
        dict
            Returns dictionary of calculated results

            The return type is a dictionary that shows the overall findings based on the intelligent agent inputs

            The ``Returns`` section contains dictionary key/pair formatting,
            including literal blocks::

                {
                    'cost_of_storage': int,
                    'units_sold_value': int,
                    'determined_cost_missed_sale': int
                    'total_losses': int,
                    'avg_customer_demand': int,
                    'avg_store_inventory': int,
                    'overall': int,
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
        self._calculated_results['overall_profit'] = self.determine_total_profit()
        return self._calculated_results

    def determine_units_value_sold(self):
        """Module

        This function uses defined init variable of inventory in total made sales to determine inventory * cost

        Parameters
        ----------
         None

        Returns
        -------
        int
            Returns int value of total_sales

            The return type is an int

            The ``Returns`` section contains a singular int value
            including literal blocks::

                {
                    'total_sales': int
                }
                """
        total_sales = 0
        for inventory in self._total_made_sales:
            total_sales += inventory * self._unit_cost
        return total_sales

    def determine_cost_of_storage(self):
        """Module

        This function uses defined init variable of inventory in total cost of storage

        Parameters
        ----------
         None

        Returns
        -------
        int
            Returns int value of total_cost of inventory

            The return type is an int

            The ``Returns`` section contains a singular int value
            including literal blocks::

                {
                    'total_cost': int
                }
                """
        total_cost = 0
        for inventory in self._store_inventory:
            if inventory > 1:
                total_cost += inventory * self._storage_cost
        return total_cost

    def determine_cost_of_missed_sales(self):
        """Module

        This function uses defined init variable of inventory in total cost of missed sales

        Parameters
        ----------
         None

        Returns
        -------
        int
            Returns int value of total_cost of missed sales

            The return type is an int

            The ``Returns`` section contains a singular int value
            including literal blocks::

                {
                    'total_cost': int
                }
                """
        total_cost = 0
        for inventory in self._missed_sales_requests:
            total_cost = inventory * self._delay_cost
        return total_cost

    def determine_total_lost_revenue(self):
        """Module

        This function uses defined init variable of missed sales plus cost of storage

        Parameters
        ----------
         None

        Returns
        -------
        int
            Returns int value of total losses based on missed sales and cost of storage

            The return type is an int

            The ``Returns`` section contains a singular int value
            including literal blocks::

                {
                    'total_missed_revenue': int
                }
                """
        return self._calculated_results['determine_cost_missed_sale'] + self._calculated_results['cost_of_storage']

    def determine_total_profit(self):
        """Module

        This function uses defined init variable of total units sold minus the total losses

        Parameters
        ----------
         None

        Returns
        -------
        int
            Returns int value of total profit after units sold gets subtracted by total losses

            The return type is an int

            The ``Returns`` section contains a singular int value
            including literal blocks::

                {
                    'total_profit': int
                }
                """
        return self._calculated_results['units_sold_value'] - self._calculated_results['total_losses']

    def determine_average_customer_order(self):
        """Module

        This function uses defined init variable of customer demand to find the average demand throughout the test

        Parameters
        ----------
         None

        Returns
        -------
        float
            Returns float value of the average customer order per day of the test

            The return type is a float

            The ``Returns`` section contains a singular float value out to two decimal places
            including literal blocks::

                {
                    'average_customer_order': float
                }
                """
        return round(statistics.mean(self._customer_demand), 2)

    def determine_average_onhand_inventory(self):
        """Module

        This function uses defined init variable of on hand inventory to find the average inventory in store throughout the test

        Parameters
        ----------
         None

        Returns
        -------
        float
            Returns float value of the average customer order per day of the test

            The return type is a float

            The ``Returns`` section contains a singular float value out to two decimal places
            including literal blocks::

                {
                    'average_on_hand_inventory': float
                }
                """
        return round(statistics.mean(self._store_inventory), 2)
