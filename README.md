# Binance Futures Trading Bot

A Python CLI-based trading bot that interacts with Binance Futures Testnet.

## Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- Input validation
- Logging of API requests and responses
- Error handling

## Setup
pip install -r requirements.txt

## Run Examples

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 78000

## Notes
- Uses Binance Futures Testnet
- Logs stored in logs/bot.log
