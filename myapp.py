import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Set Streamlit app title
st.title('Simple Stock App')

# User input for stock ticker symbol
ticker_symbol = st.text_input('Enter Stock Ticker Symbol (e.g., AAPL):', 'AAPL')

# Fetch stock data
stock_data = yf.download(ticker_symbol, start='2022-01-01', end='2023-01-01')

# Display stock data
if not stock_data.empty:
    st.subheader('Stock Data:')
    st.write(stock_data)

    # Plot closing prices
    st.subheader('Closing Prices:')
    plt.plot(stock_data['Close'])
    plt.title(f'{ticker_symbol} Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    st.pyplot(plt)

else:
    st.write(f'Error: No data found for {ticker_symbol}')
