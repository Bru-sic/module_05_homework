# module_05_homework
Module 5 Financial Planning Simulator

Author: Bruno Ivasic   
Date: 28 September 2023

# Overview
This assignment focuses on Python Requests (apis) to fetch data from trading platforms including:
* [Alternative.me](https://alternative.me/crypto/api/)
* [Alpaca Markets](https://app.alpaca.markets)
* [data.nasdaq.com](https://data.nasdaq.com)

Thanks and gratitude to the above sites for their services and data.

# Briefing
Further details on the assignment briefing are available in [Briefing.md](./Briefing.md)


# Solutions

## Solution 1 - Using original template and MC library
This solution is based completely on original starter code template and the original Monte Carlo simulator library provided with the assignment.

Files associated with this solution:   
* [iPython (Jupyter) Notebook: Starter_Code/financial-planner.ipynb](Starter_Code/financial-planner.ipynb)   
* [Original Monte Carlo Simulator Library: Starter_Code/MCForecastTools.py](Starter_Code/financial-planner.ipynb)   



## Solution 2 - Alternate solution

The base code has been refactored and improved:
1. Duplicate code was moved to a new function `monte_carlo_simulation_analysis`.
2. Introduced use of a dictionary to store stock data and moved away from naming variables with specific stock code (eg. btc_price, agg_value etc).
3. Adopted use of the new Monte Carlo library for significantly faster performance which also resolves the occasional `PerformanceWarning: DataFrame is highly fragmented` warning message.
4. Added functionality to get the most recent data from Alpaca markets, resolving the issue of getting no data if the date selected was not a trading day.


Files associated with this solution:   
* [iPython (Jupyter) Notebook: Starter_Code/financial-planner-NEW.ipynb](Starter_Code/financial-planner.ipynb)   
* [New Forecast Tools: Starter_Code/NewForecastTools.py](Starter_Code/NewForecastTools.py)   


# Pre-requisites

## .env file
The scripts in this project read configuration parameters from a `.env` file, which you need to create and configure in the root folder of this project or a parent folder on your local computer containing the following: 
```
ALPACA_API_KEY = "<VALUE GOES HERE>"
ALPACA_SECRET_KEY = "<VALUE GOES HERE>"
NASDAQ_API_KEY = "<VALUE GOES HERE>"
```

You need to replace `<VALUE GOES HERE>` with the relevant keys obtained from YOUR accounts on the following sites:
* [Alpaca Markets](https://app.alpaca.markets)
* [data.nasdaq.com](https://data.nasdaq.com)


Note: Although the scripts use get_bars for Alpaca Markets, as a precaution, the code has forcibly set the Alpaca Markets api Base URL to the paper trading environment "paper-api.alpaca.markets", to avoid any unintended consequence of using the real live interface.

---


