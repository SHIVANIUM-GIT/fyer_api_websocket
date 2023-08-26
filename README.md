# fyer_api_webstock

# fyers_api

# Fyer API WebSocket

![Fyer Logo](https://www.fyer.in/images/logo_blue.svg)

Fyer API WebSocket is a Python-based application that demonstrates the usage of Fyer's API with WebSocket functionality. This project allows you to connect to Fyer's trading API through WebSocket, enabling real-time data streaming and trading automation.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Fyer is a popular online stock trading platform. This project provides a Python script that connects to Fyer's API using the WebSocket protocol. The WebSocket connection allows for efficient real-time data updates and quick execution of trading strategies.

## Features

- **WebSocket Data Streaming:** Utilize WebSocket to receive real-time market data, including live stock prices, order book changes, and trade execution updates.
- **Trading Automation:** Develop and deploy trading algorithms that can execute orders based on real-time market data received via the WebSocket connection.
- **Interactive Data Analysis:** Use streamed data to perform interactive analysis, create visualizations, and make informed trading decisions.
- **Easy Integration:** The project demonstrates how to establish a WebSocket connection with Fyer's API, making it easier to integrate within your own trading strategies or applications.

## Getting Started

### Prerequisites

To run the Fyer API WebSocket application, you'll need:

- [Python](https://www.python.org/downloads/): Make sure you have Python installed on your system.
- Fyer API Credentials: Obtain your API credentials by signing up on the Fyer platform and generating your API keys.

### Installation and Setup

1. Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/SHIVANIUM-GIT/fyer_api_websocket.git
    ```
    

2. Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ``````

  
3. Open the config.py file and replace 'YOUR_API_KEY' and 'YOUR_API_SECRET' with your Fyer API  credentials.

4. Run the Python script:
    ```bash
        python main.py
    ```





# Automatically Generate Access Token for your FYERS API

A Python Script to automatically generate Access Token for your [FYERS API](https://fyers.in?id=XS12141)

## Pre-requisites
* An account with FYERS. If you don't have an account, you can open the same using this [link](https://open-an-account.fyers.in/?id=XS12141)

#INSTALLATION:
*pip install fyers-apiv2

## Requirements
* Python 3
* fyers_api
* python-dotenv

## .env file formate
* client_id=""
* secret_key=""
* redirect_uri=""
