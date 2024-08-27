import streamlit as st
import yfinance as yf

st.write("""
# Indian Stock Price Web App
##### A Detailed Exploration of Closing Price Trends, Trading Volume, and Real-Time Live Prices in the Indian Stock Market
""")

# Dropdown menu for ticker selection
all_ticker_symbols = [
    'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJFINANCE.NS', 'CIPLA.NS', 'HINDUNILVR.NS', 
    'HDFC.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'INFY.NS', 'ITC.NS',
    'KOTAKBANK.NS', 'LT.NS', 'MARUTI.NS', 'ONGC.NS', 'POWERGRID.NS', 
    'RELIANCE.NS', 'SBIN.NS', 'TATASTEEL.NS', 'TCS.NS', 'WIPRO.NS'

]
tickerSymbol = st.selectbox('Select Any Stock', all_ticker_symbols)


#Duration of the graph
all_ticker_duration = [
'5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y'
]
duration = st.selectbox('Select The Time Period', all_ticker_duration)






# Ticker ke data ko fetch karein
tickerdata = yf.Ticker(tickerSymbol)
tickerdf = tickerdata.history(period=duration)





# Line chart for live price
st.write("""
## Live Price Chart:""",tickerdf["Close"])
st.line_chart(tickerdf["Close"])

# Closing price 
st.write("""
## Closing Price:""",tickerdf.Close)
st.line_chart(tickerdf.Close)

# Volume 
st.write("""
## Volume Price:""",tickerdf.Volume)
st.line_chart(tickerdf.Volume)



