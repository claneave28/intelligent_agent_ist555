
# IST 555 - Intelligent Agents  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

In this project, the team works to run against multiple agent simulations to determine which method of store inventory  and selling makes the most sense.  
Included in this project is the evaluation of JIT (Just in time) vs Repeatable static order patterns.  The variance and model also includes distribution to shipping, random customer demand and cost associations to both lost customers or too much stock.
The code itself will print out the results of the executions as well as provide a CSV at the root level with the data. 

Users can also view plot modeling on execution using the python library pandas and matplotlib.



## Authors

- [Carl Laneave](https://www.github.com/claneave28)
- Stephen Gregory Carras
- Michael Chee


## Environment Variables

To run this project, you have two options for declarative constructs as far as options.

`Build_data_payload` - This boolean determines if you want to dynamically create the variables or define your own.

* True (boolean) - The script will build out the payload of data for you dynamically

* False (boolean) - The script will use a json file to determine your payload of data for the agent.

`inputs.json [optional]`  - The inputs.json file will have all the required keys and value pairs in a dictionary form for the experiments being executed.



## Inputs.json Example File
```yaml
{
  "cost_delayed": 2,
  "cost_instock": 4,
  "cost_unit": 5,
  "store_shipping": 5,
  "warehouse_shipping": 10,
  "manufacturer_shipping": 20,
  "starting_store": 100,
  "starting_warehouse": 490,
  "starting_manufacturer": 5066,
  "reorder_store": 39,
  "reorder_warehouse": 224,
  "reorder_store_values": 100,
  "reorder_warehouse_values": 200,
  "reorder_manufacture_values": 1000,
  "shipping_failure": 1,
  "customer_demand": 98
}

```


## Executing Locally

Clone the project

```bash
  git clone https://github.com/claneave28/intelligent_agent_ist555
```

Go to the project directory

```bash
  cd intelligent_agent_ist555
```

Install dependencies

```bash
  pip3 install requirements.txt
```

Execute the Script

```bash
  python ./main.py
```


## Wiki Generation

To build out the wiki for docstring documentation, Sphinx must be installed on your local environment.

Sphinx Installation:
https://www.sphinx-doc.org/en/master/usage/installation.html


After installation, follow the following steps to generate new wikis.

```bash
  cd intelligent_agent_ist555
```

```bash
  make clean
```

```bash
  make html
```

```bash
  cd build/html
```

```bash
  open index.html
```

#### Important!
 If you do not install sphinx, you can still view the report as its already generated and lives within the repository!
## Appendix

Made using python3, pip3, and packages including pandas and matplotlib.  If wanting to view the plot outputs, ensure you are using an IDE that supports such functionality. 

* Pycharm
* VSCode

If you want to generate a new wiki, Sphinx is required.

All execution was done inside virtual environment using python3.9 and does not support python 2.x