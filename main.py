import numpy as np
import pandas
from matplotlib import pyplot as plt
import global_classes.data_executor as inputs


def build_data_payload(payload):
    if payload:
        results = inputs.DataExecutor(random_input=True)
        print(f'{results}')


if __name__ == '__main__':
    build_data_payload(True)


