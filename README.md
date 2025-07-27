# CHF/PLN Exchange Rate Forecaster

A deep learning-based application for forecasting the Swiss Franc to Polish Zloty (CHF/PLN) exchange rate.

## Overview

This project uses LSTM (Long Short-Term Memory) neural networks to predict future CHF/PLN exchange rates based on
historical data. The application provides a user-friendly interface to forecast exchange rates for any future date.

## Features

- Historical exchange rate data analysis
- Time series forecasting using LSTM neural networks
- Interactive web interface for predictions
- Visualization of forecast results

## Installation

1. Clone the repository

2. Create a virtual environment:

```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

Run the web application:

```
cd src streamlit run app.py
```

The application will open in your browser, allowing you to input a future date and get a predicted CHF/PLN exchange
rate.

## Model Information

- Model type: LSTM (Long Short-Term Memory)
- Training data: Daily CHF/PLN exchange rates
- Sequence length: 30 days
- Training/validation split: 70/30
- Data from 1984-01-02 to 2025-06-26

## Technologies Used

- Python 3.12
- TensorFlow/Keras
- Pandas
- NumPy
- Streamlit
- Plotly
