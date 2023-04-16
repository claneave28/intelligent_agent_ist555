import random

import numpy as np
import pandas
from matplotlib import pyplot as plt
import json
import global_classes.data_builder as inputs
import collections

execution_results = collections.defaultdict(dict)


def build_data_payload(payload):
    if payload:
        input_values = inputs.DataExecutor().build_data_points()
    else:
        file = open("inputs.json", 'r')
        input_values = json.load(file)
    return input_values


def start_build(days, payload):
    max_demand = payload['customer_demand']
    starting_store_inventory = payload['starting_store']
    starting_warehouse_inventory = payload['starting_warehouse']
    starting_manufacturer_inventory = payload['starting_manufacturer']

    for day in range(1, days):
        if day == 1:
            for key, value in payload.items():
                if key == 'customer_demand':
                    value = random_customer_demand(max_demand)
                if key == 'starting_store':
                    value = value - max_demand
                execution_results[day].update({key: value})
        else:
            day = day - 1
            for key, value in execution_results[day].items():
                if key == 'customer_demand':
                    value = random_customer_demand(max_demand)
                if key == 'starting_store':
                    value = value - execution_results[day]['customer_demand']

                execution_results[day+1].update({key: value})
        print(execution_results)


def inventory_processing(inventory, inventory_removed):
    return inventory - inventory_removed


def random_customer_demand(max_demand):
    return random.randint(0, max_demand)


if __name__ == '__main__':
    input_value_dict = build_data_payload(False)
    start_build(5, input_value_dict)
