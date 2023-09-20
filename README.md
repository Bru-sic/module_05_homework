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

Further details of the assignment are available [here in Briefing.md](./Briefing.md)

# Pre-requisites

## .env file
The scripts in this project read configuration parameters from a `.env` file, which you need to create and configure in the root folder of this project or a parent folder on your local computer containing the following: 
```
ALPACA_API_KEY = "<VALUE GOES HERE>"
ALPACA_SECRET_KEY = "<VALUE GOES HERE>"
NASDAQ_API_KEY = "<VALUE GOES HERE>"
```

You need to replace `<VALUE GOES HERE>` with the relevant keys obtained from YOUR accounts on the following site:
* [Alpaca Markets](https://app.alpaca.markets)
* [data.nasdaq.com](https://data.nasdaq.com)

Note: the scripts in this project force the Alpaca Markets api base url to the paper trading environment "paper-api.alpaca.markets".
---


