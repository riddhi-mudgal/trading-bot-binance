# Binance Futures Testnet Trading Bot

## Overview
This project is a simple Python trading bot that interacts with the Binance Futures Testnet.  
It allows users to place MARKET and LIMIT orders using a command-line interface (CLI).

The bot demonstrates:
- API integration
- CLI input handling
- input validation
- structured logging
- modular Python project structure


## Project Structure
```
trading_bot/
|
├── bot/
|   ├── __init__.py
│   ├── client.py
│   ├── validators.py
│   ├── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore
```


## Installation

1. Clone the repository

- git clone REPLACE_WITH_YOUR_GITHUB_LINK

- cd trading_bot


2. Install dependencies

- pip install -r requirements.txt


## API Configuration

Create a file named **config.py** in the project folder and add your Binance Futures Testnet API keys.

Example:

- API_KEY = "your_api_key_here"
- API_SECRET = "your_api_secret_here"



## Running the Bot

Run a MARKET order:

- python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002


Run a LIMIT order:

- python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 68000


## Logging

All API requests and responses are saved in:

logs/trading.log


## Assumptions

- Binance Futures Testnet API is used
- Valid trading symbol is provided
- Quantity follows Binance minimum order requirements