import requests
from bs4 import BeautifulSoup


class DataCollector:
    def __init__(self):
        pass

    def fetch_webpage_content(self, url):
        """
        Fetches content from a given URL using requests and BeautifulSoup.

        Args:
        - url (str): The webpage URL.

        Returns:
        - content (str): The textual content from the webpage.
        """
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("Failed to fetch the webpage content.")

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = " ".join([para.text for para in paragraphs])
        return content

    def collect_from_source(self, source_name, source_url):
        """
        Collects data from a given source.

        Args:
        - source_name (str): The name of the source (e.g., "Wikipedia", "TechCrunch").
        - source_url (str): The URL of the data source.

        Returns:
        - content (str): The collected content.
        """
        if source_name == "webpage":
            return self.fetch_webpage_content(source_url)
        # You can add more sources here in the future as needed.
        else:
            raise ValueError(f"Unknown source: {source_name}")

    def format_data(self, content):
        """
        Formats the collected data for training.

        Args:
        - content (str): The raw content.

        Returns:
        - formatted_content (str): The content formatted for training.
        """
        # Here, you can implement any formatting or pre-processing you want.
        # For this example, I'm just returning the content as-is.
        return content

    def collect_and_format(self, source_name, source_url):
        """
        Collects and formats data from a given source.

        Args:
        - source_name (str): The name of the source.
        - source_url (str): The URL of the data source.

        Returns:
        - formatted_content (str): The content formatted for training.
        """
        content = self.collect_from_source(source_name, source_url)
        return self.format_data(content)
