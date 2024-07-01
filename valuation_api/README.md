# This is a flask api that helps performing valuation
# Application to fetch and store the B/S, I/S and cash-flow statement using the financialmodellingprep api and postgres. The application will also be able to compare the companies with a graphical control interface.

# Api usage
# Adjust .env
API_KEY= financialmodellingprep api key
DB_URL= your_db_url
BASE_URL= 'https://financialmodelingprep.com/api/v3/'
YEARS= years to fetch (5 recommendeed)
# Run the application:
brew services start postgresql
flask run


# Endpoint to fetch the basic company data and add the company to the database : POST - http://127.0.0.1:5000/add_company

Body:
{
  "symbol": "AAPL",
  "cik": "0000320193"
}
## cik can be found at the SEC website or using a scraper

# Endpoint to fetch and store the financial statement data: POST - http://127.0.0.1:5000/api/fetch_and_store 

Body:
{
  "company_id": 1,
  "symbol": "AAPL"
}


# Endpoint to calculate the latest ratios and store them: POST - http://127.0.0.1:5000/api/calculate_ratios

Body:

{
  "company_id": 1
}

