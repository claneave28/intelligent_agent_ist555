import csv
import random
import global_classes.computations as calculations
import pandas as pd
from matplotlib import pyplot as plt
import json
import global_classes.data_builder as inputs
import collections
import sys

execution_results_standard = collections.defaultdict(dict)
execution_results_jit = collections.defaultdict(dict)
result_field_headers = ['starting_store', 'starting_warehouse', 'starting_manufacturer', 'customer_demand']


def build_data_payload(payload):
    if payload:
        input_values = inputs.DataExecutor().build_data_points()
    else:
        file = open("inputs.json", 'r')
        input_values = json.load(file)
    return input_values


def start_build(days, payload, model):
    print("Executing testing on variables:\n")
    print(json.dumps(payload, indent=4, sort_keys=True))
    if model == 'standard':
        return build_standard_data(days, payload)
    elif model == 'jit':
        return build_jit_data(days, payload)
    else:
        print("Invalid selection on model, exiting program")
        sys.exit(1)


def build_jit_data(days, payload):
    max_demand = payload['customer_demand']
    reorder_store_quantity = payload['reorder_store_values']
    reorder_manufacture_quantity = payload['reorder_manufacture_values']
    reorder_warehouse_quantity = payload['reorder_warehouse_values']
    shipping_store_days = payload['store_shipping']
    shipping_warehouse_days = payload['warehouse_shipping']
    manufacturing_days = payload['manufacturer_shipping']
    trigger_order_store = 0
    trigger_order_warehouse = 0
    trigger_order_manufacturer = 0

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
                        if value < 1:
                            value = 0
                    execution_results_jit[day].update({key: value})
        else:
            day = day - 1
            for key, value in execution_results_jit[day].items():
                if key in result_field_headers:
                    if key == 'customer_demand':
                        value = random_customer_demand(max_demand)
                    if key == 'starting_store':
                        if value > 1:
                            value = value - execution_results_jit[day]['customer_demand']
                        else:
                            value = 0
                            if trigger_order_store >= shipping_store_days:
                                value += reorder_store_quantity
                                store_order = reorder_store_quantity
                                trigger_order_store = 0
                            else:
                                trigger_order_store += 1
                    if key == 'starting_warehouse':
                        if value > 1:
                            value = value - store_order
                        else:
                            value = 0
                            if trigger_order_warehouse >= shipping_warehouse_days:
                                value += reorder_warehouse_quantity
                                warehouse_order = reorder_warehouse_quantity
                                trigger_order_warehouse = 0
                            else:
                                trigger_order_warehouse += 1
                    if key == 'starting_manufacture':
                        if value > 1:
                            value = value - warehouse_order
                        else:
                            value = 0
                            if trigger_order_manufacturer >= manufacturing_days:
                                value += reorder_manufacture_quantity
                                trigger_order_store = 0
                            else:
                                trigger_order_store += 1
                    if value < 1:
                        value = 0
                    execution_results_jit[day + 1].update({key: value})
    return execution_results_jit


def build_standard_data(days, payload):
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
                        if value < 1:
                            value = 0
                    execution_results_standard[day].update({key: value})
        else:
            day = day - 1
            for key, value in execution_results_standard[day].items():
                if key in result_field_headers:
                    if key == 'customer_demand':
                        value = random_customer_demand(max_demand)
                    if key == 'starting_store':
                        if value > 1:
                            value = value - execution_results_standard[day]['customer_demand']
                        else:
                            value = 0
                        if day % shipping_store_days == 0:
                            value += reorder_store_quantity
                            store_order = reorder_store_quantity
                    if key == 'starting_warehouse':
                        if value > 1:
                            value = value - store_order
                        if day % shipping_warehouse_days == 0:
                            value += reorder_warehouse_quantity
                            warehouse_order = reorder_warehouse_quantity
                    if key == 'starting_manufacture':
                        if value > 1:
                            value = value - warehouse_order
                        if day % manufacturing_days == 0:
                            value += reorder_manufacture_quantity
                    if value < 1:
                        value = 0
                    execution_results_standard[day + 1].update({key: value})
    return execution_results_standard


def inventory_processing(inventory, inventory_removed):
    return inventory - inventory_removed


def random_customer_demand(max_demand):
    return random.randint(0, max_demand)


def build_plot_graph(results, execution_results):
    df = pd.DataFrame.from_dict(results)
    df.describe().to_csv("test_results_"+str(execution_results)+".csv")
    df.style.set_caption('Model Results')
    plt.plot(df)
    plt.show()
    return df
def create_csv_from_plot_data(results, type):
    with open('rawdata_'+str(type)+'.csv', 'w') as csvfile:
        for key in results.keys():
            csvfile.write("%s,%s\n"%(key,results[key]))

if __name__ == '__main__':
    execution_results = 0
    days = 15
    input_value_dict = build_data_payload(True)
    cost_of_delay_per_unit = input_value_dict['cost_delayed']
    cost_of_unit = input_value_dict['cost_unit']
    cost_of_instock_storage = input_value_dict['cost_instock']
    execution_results_standard = start_build(days, input_value_dict, 'standard')
    execution_results_jit = start_build(days, input_value_dict, 'jit')
    create_csv_from_plot_data(execution_results_jit, "jit")
    for execution in execution_results_jit,execution_results_standard:
        plot_graph = build_plot_graph(execution, execution_results)
        execution_results += 1
        print(f"\n{plot_graph}")
        gather_metrics = calculations.Calculations(total_days=days, results=execution,
                                                   delay_cost=cost_of_delay_per_unit, unit_cost=cost_of_unit,
                                                   storage_cost=cost_of_instock_storage).gather_all_metrics()
        print(f"\n{gather_metrics}")
