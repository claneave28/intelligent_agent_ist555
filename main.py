import numpy as np
import pandas
from matplotlib import pyplot as plt
import json
import global_classes.data_executor as inputs


def build_data_payload(payload):
    if payload:
        input_values = inputs.DataExecutor().build_data_points()
    else:
        file = open("inputs.json", 'r')
        input_values = json.load(file)
    return input_values


if __name__ == '__main__':
    input_value_dict = build_data_payload(False)
    print(input_value_dict)


