import requests  # Library for making HTTP requests
from bs4 import BeautifulSoup  # Library for parsing HTML content
import csv  # Library for working with CSV files
from datetime import datetime  # Library for working with date and time

def extract_table_data(url):
  """
  Extracts table data from a given URL.

  Args:
      url (str): The URL of the webpage containing the table.

  Yields:
      list: A list containing rows of data extracted from the table. Each row is a list of cell values.
  """
  response = requests.get(url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    if table:
      rows = table.find_all('tr')
      for row in rows[1:]:  # Skip header row
        cells = row.find_all('td')
        data = [cell.text.strip() for cell in cells]
        yield data  # Generator expression to yield data row by row
    else:
      print("No table found on the page.")
  else:
    print("Failed to fetch the page.")

if __name__ == "__main__":
  base_url = "https://noc.org.np/retailprice?offset={offset}&max=10"
  offset = 0
  all_data = []

  # Fetching all data using pagination
  while True:
    url = base_url.format(offset=offset)
    print("Fetching data from:", url)
    data = extract_table_data(url)
    for row in data:
      all_data.append(row)
    offset += 10
    if offset > 100:
      break

  # Generate a timestamp for the filename
  current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

  # Writing extracted data to CSV file with timestamp suffix
  filename = f'retail_prices_{current_datetime}.csv'
  with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product', 'Unit', 'Price', 'Location', 'Date'])
    writer.writerows(all_data)

  print("Data saved to", filename)
