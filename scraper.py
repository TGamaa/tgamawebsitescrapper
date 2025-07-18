import requests
from bs4 import BeautifulSoup

def scrape():
    try:
        # Fetch the webpage
        url = 'https://www.example.com'
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title
        title = soup.find('title').get_text() if soup.find('title') else 'No title found'

        # Extract all paragraphs
        paragraphs = [p.get_text().strip() for p in soup.find_all('p') if p.get_text().strip()]

        # Write to output file
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(f"Title: {title}\n")
            for para in paragraphs:
                f.write(f"Paragraph: {para}\n")

        print("Scraping complete. Check output.txt for results.")

    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
    except Exception as e:
        print(f"Error during scraping: {e}")

if __name__ == '__main__':
    scrape()