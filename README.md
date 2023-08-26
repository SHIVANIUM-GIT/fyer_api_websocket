

# Fyer API WebSocket

![Fyer Logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAb1BMVEX///9DavU2YvWyv/o5ZPWbrPlAaPVXePaEmvhKcPUyYPX5+v+MofgqW/QuXfSvvfra4P319/67x/vs7/6WqfnR2fweVfSrufrM1fxqhvfn7P6Tpvl6kvfx8/6fr/nBy/thf/bf5P2Al/hOcvVzjfcfSKh/AAADdUlEQVR4nO3d23aiMBhA4YBMPIJVq632aO37P2NntMtChmpC/khg7e+il6zs4sI0BKoUAAAAAAAAAAAAAAAAAAAAAPTO/P6PiPv18XBrqcPNxQrvNpmI/DSkeS5zuM2dWKEaZYmEdHA82iAVOVo2kgtUi4mWGJNooZ4sBAvVg8igRAvTB8lApcYSJ1GyUI9lA9VjITAqycLiUbhQbQVOomCh3koHql0eVWG+Ey9UT/7jkitMn+QD1TTz/pyKFepsGqBQDSbRFE4GIQKVGvqeRKlCPQwTqO58LzZShbnghLTq2fMkChXq51CB6sXzJAoV5i/BCtWr39hkCtPXcIFK+X1MZQp1yED15jU9FSks3oIWqnefsyhRqN/DBqq9z8VGojDfBy70WtAQKBRduqi3KBzWioyP9C+F2uGIhejSRb3lx8jWLNEWhTqZWR/xYxk+0MnQqjDULPMWKKQwfhRSGD8KKYwfhRTGj8LYC7fjKw5JYlGYJIcrx0mC3IexsNs4Lks1XMUo2vuz13WBuFlh8NW1Sxz3LzQrDL+6dsHabW2xUeENVtcucVtbbFKo07YuMydut76bFIa63Wtt6XIjo0FhBF+WLvtsGhSGu91rbeVwsXEvzMLd7rXn8KXoXniLRfzrDtafU+dC6f2HDdlv0XAtFN9/2JT1l6JrYS6+/7ChaaBC/dly2A/bu/uOhfmq5a6Sbepzh/S330fQXSWOVqNZnaexzd/4f2dmtbKWo6zYrmJM67Q8djtdX6e5jkIK40chhfGjkML4UUhh/CikMH4UUhg/CimMH4UUxo9CCuNHIYXxo5DC+FFIYfzsCg8tj9KHsVmqvjDIm8luprqD+Jdz2PIY/VR3ENcWhn7fTGiVHcR1hQFegHhj5Zd/1BUWEW1AbKb8WtCawqg2IDb0qS8URrPP2cequFCYr1senYifdxD/V5h9tDw2IefHFcxC4dc5t+f8DJ9Z2PpTW2Kes9rCTk+5qxaFrits9eFQYfNJTWG3Z9ym08WmWtjtGbfp9GxUpbDrM27T8dmocmH3Z9yG439XKBfG9MiPjH/vyi4V9mHGbRrqUmEvZtymfV4q7MeM2zTLzoV9mXEbpum5sC8zbtNy81246c2M2zT8/m9IXV4Cvmx/evj8of33JASzK/0EAAAAAAAAAAAAAAAAAAAAANT5AsfJP0fKWhRFAAAAAElFTkSuQmCC)

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
