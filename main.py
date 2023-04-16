import random

import numpy as np
import pandas
from matplotlib import pyplot as plt
import json
import global_classes.data_builder as inputs
import collections

execution_results = collections.defaultdict(dict)
result_field_headers = ['starting_store','starting_warehouse','starting_manufacturer','customer_demand']

def build_data_payload(payload):
    if payload:
        input_values = inputs.DataExecutor().build_data_points()
    else:
        file = open("inputs.json", 'r')
        input_values = json.load(file)
    return input_values


def start_build(days, payload):
    max_demand = payload['customer_demand']
    reorder_store_quantity = payload['reorder_store_values']
    reorder_manufacture_quantity = payload['reorder_manufacture_values']
    reorder_warehouse_quantity = payload['reorder_warehouse_values']
    shipping_store_days = payload['store_shipping']
    shipping_warehouse_days = payload['warehouse_shipping']
    manufacturing_days = payload['manufacturer_shipping']

    for day in range(1, days):
        store_order = 0
        warehouse_order = 0
        if day == 1:
            for key, value in payload.items():
                if key in result_field_headers:
                    if key == 'customer_demand':
                        value = random_customer_demand(max_demand)
                    if key == 'starting_store':
                        value = value - max_demand
                    execution_results[day].update({key: value})
        else:
            day = day - 1
            for key, value in execution_results[day].items():
                if key in result_field_headers:
                    if key == 'customer_demand':
                        value = random_customer_demand(max_demand)
                    if key == 'starting_store':
                        value = value - execution_results[day]['customer_demand']
                        if day % shipping_store_days:
                            value += reorder_store_quantity
                            store_order = reorder_store_quantity
                    if key == 'starting_warehouse':
                        value = value - store_order
                        if day % shipping_warehouse_days:
                            value += reorder_warehouse_quantity
                            warehouse_order = reorder_warehouse_quantity
                    if key == 'starting_manufacture':
                        value = value - warehouse_order
                        if day % manufacturing_days:
                            value += reorder_manufacture_quantity
                    execution_results[day+1].update({key: value})
    print(execution_results)


def inventory_processing(inventory, inventory_removed):
    return inventory - inventory_removed


def random_customer_demand(max_demand):
    return random.randint(0, max_demand)


if __name__ == '__main__':
    input_value_dict = build_data_payload(False)
    start_build(15, input_value_dict)
