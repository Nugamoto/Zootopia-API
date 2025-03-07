# Zootopia-API

This Python project allows users to fetch data about a selected animal using the API from API Ninjas (https://api-ninjas.com/). The retrieved data is then used to generate an HTML page with relevant information.

## Installation

1. Ensure Python (version 3.x) is installed on your system.
2. Clone the repository:
   ```sh
   cd zootopia-api
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```sh
   python animals_web_generator.py
   ```
2. Select an animal by entering its name in the console.
3. The program fetches the API data and generates an HTML file with animal details.
4. Open the generated HTML file animals.html in a web browser to view the results.

## API Notes

This project uses the API from API Ninjas to retrieve animal data. Make sure you have a valid API key and store it in a `.env` file:
```env
API_KEY = --> your_api_key <--
```

For more information about the API, visit: [API Ninjas](https://api-ninjas.com/)

## Example Output

After entering an animal name, the script generates an HTML file containing information such as:
- Name
- Location
- Diet
- Additional interesting facts

## Contributing

Pull requests are welcome! If you have ideas or improvements, feel free to create an issue.


---

Let me know if you need any further modifications! 😊

