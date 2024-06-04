## NOC Retail Price Data Scraper

This Python script scrapes retail price data from the Nepal Oil Corporation (NOC) website and saves it to a CSV file.

**Requirements:**

* Python 3
* Libraries: requests, bs4, csv, datetime

**Instructions:**

1. Save the script as a Python file (e.g., `noc_retail_price_scraper.py`).
2. Install the required libraries (`pip install requests beautifulsoup4 csv`).
3. Run the script using Python (`python noc_retail_price_scraper.py`).

**Output:**

The script will generate a CSV file named `retail_prices_[timestamp].csv` containing the following columns:

* Product
* Unit
* Price
* Location
* Date (This column might not be present on the website itself)

**How it Works:**

1. The script iterates through pages on the NOC website using pagination (`offset` parameter).
2. For each page, it extracts the table containing retail price data using BeautifulSoup.
3. It processes each row in the table, extracting relevant information (product, unit, price, location).
4. All extracted data is accumulated in a list.
5. Finally, the script writes the accumulated data to a CSV file with a timestamp appended to the filename.

**Note:**

* This script relies on the structure of the NOC website, which may change in the future.
* It's recommended to check the website periodically to ensure the script continues to function correctly.

**Disclaimer:**

This script is provided for educational purposes only. It is recommended to respect the NOC's terms of use when scraping data from their website.
