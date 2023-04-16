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
    for day in range(1, days):
        for key, value in payload.items():
            print(key, value)
            execution_results[day].update({key: value})
    print(execution_results)


if __name__ == '__main__':
    input_value_dict = build_data_payload(False)
    start_build(100, input_value_dict)
