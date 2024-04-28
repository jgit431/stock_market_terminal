import yfinance as yf

def fetch_data(ticker_symbol, start_date, end_date):
    """Fetch historical stock data"""
    return yf.download(ticker_symbol, start=start_date, end=end_date)


def get_company_name(ticker):
    try:
        # Create a Ticker object for the given ticker symbol
        ticker_obj = yf.Ticker(ticker)
        
        # Fetch the company name from the Ticker object
        company_name = ticker_obj.info.get('longName', 'Company Name Not Found')
        
        return company_name
    except Exception as e:
        print(f"Error fetching company name: {e}")
        return "Error"
