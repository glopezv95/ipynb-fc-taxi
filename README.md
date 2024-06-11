# NYC Taxi fares. Time series prediction
This project consist of the definition of a time series ARIMAX model from [NYC taxi fares data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page?ref=hackernoon.com) to forecast 100 instants in the future.

> [!CAUTION]
>The taxi data `.parquet` files stored in the `data` directory are **considerably large**. The process of cloning the repository may take some time.

The data has been grouped by day in order to generate a time series index. The **target variable** is the taxi `fare_amount`, and the **exogenous variable** is the `passenger_count`. Initial analysis of the distribution through time shows **inhomogenous variance of the data**, and thus **1 differentiation** step is applied to the model before optimising the autorregresive and moving average orders.

The prediction is made using and optimised **ARIMAX(0, 1, 2) model**.

In order to automate the setup of the project (virtual environment generation, activation, pip upgrade and required packages installation), both a `.bat`  and a `.sh` file have been provided. Thus, to setup the project, run
```
path/to/project/setup.bat
```
in Windows based systems or
```
path/to/project/setup.sh
```
in Linux based systems.