import random


class Calculations(object):

    def __init__(self, total_days, results, delay_cost, unit_cost, storage_cost):
        self._result_payload = results
        self._total_days = total_days
        self._store_inventory = []
        self._customer_demand = []
        self._delay_cost = delay_cost
        self._unit_cost = unit_cost
        self._storage_cost = storage_cost
        self._calculated_results = {}

    def gather_all_metrics(self):
        for key, value in self._result_payload.items():
            for key_name in value:
                if key_name == "starting_store":
                    self._store_inventory.append(value[key_name])
                elif key_name == "customer_demand":
                    self._customer_demand.append(value[key_name])
        self._calculated_results['cost_of_storage'] = self.determine_cost_of_storage()
        return self._calculated_results

    def determine_units_value_sold(self):
        print("asdf")

    def determine_cost_of_storage(self):
        total_cost = 0
        for inventory in self._store_inventory:
            if inventory > 1:
                total_cost += inventory * self._storage_cost
        return total_cost

    def determine_cost_of_missed_sales(self):
        print("asdfasdf")

    def determine_total_lost_revenue(self):
        print("asdfasdf")

    def determine_total_profit(self):
        print("asdfasdf")

    def determine_average_customer_order(self):
        print("asdf")

    def determine_average_onhand_inventory(self):
        print("asdf")
