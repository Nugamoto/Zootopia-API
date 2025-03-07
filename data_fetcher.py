import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """
    Fetch information about an animal from the API.

    This function sends a GET request to the API Ninjas endpoint to retrieve
    details about a specific animal. The request includes an API key for authentication.

    Args:
        animal_name (str): The name of the animal to look up.

    Returns:
        dict | bool: The API response as a dictionary if successful.
                     Returns False and prints an error message if the request fails.
    """
    api_url = "https://api.api-ninjas.com/v1/animals?name={}".format(animal_name)
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return False


def load_html_file(file_path):
    """
    Load an HTML file as a string with error handling.

    Args:
        file_path (str): The path to the HTML file.

    Returns:
        str: The content of the HTML file if successful, otherwise None.

    Raises:
        ValueError: If the file is empty.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            content = handle.read()
            if not content.strip():
                raise ValueError(f"Error: The file '{file_path}' is empty.")
            print(f"✅ HTML_document '{file_path}' loaded successfully!")
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{file_path}'.")
    except UnicodeDecodeError:
        print(f"Error: Failed to decode '{file_path}'. Check the file encoding.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None
