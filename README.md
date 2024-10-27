<img src="https://github.com/user-attachments/assets/33fda36c-8414-4e3a-a040-ac1658ba8928" alt="Image description" width="300"/>
   
# MeridianIQ

This project provides a tool to process addresses and retrieve latitude and longitude based on city, state/province, and country information for both Canadian and U.S. addresses while cleaning out message noise. It uses data from postal code CSV files and a language model (`OllamaLLM`) to parse address components.

## Features

- Processes addresses from an input file and determines city, state/province, and country.
- Retrieves latitude and longitude based on city and state/province for Canadian and U.S. addresses using postal code datasets.
- Utilizes a language model (`OllamaLLM`) to extract city and state information from address strings.
- Utilizes Google Search as a backup for finding location.
- Outputs the result in the format: `City / State or Province / Latitude / Longitude`.
- Handles and logs failed lookups for further investigation.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AndrewGordienko/address-cleanup
   cd address-cleanup
   ```

2. **Install the library and dependancies:**
   ```bash
   pip install llama-cleanup
   pip install pandas numpy langchain_ollama langchain_openai unidecode pyspellchecker thefuzz unicodedata
   ```

## Usage

Once everything is set up, you can run the script to process the addresses and retrieve latitude and longitude information.

### Example Usage

Check docs.ipynb

## Configuration Details

The `AddressLookup` class requires the following parameters:

- `canadian_postal_codes_path`: Path to the CSV file containing Canadian postal codes.
- `us_zip_codes_path`: Path to the CSV file containing U.S. postal codes.
- `llama_model`: Name of the model used by `OllamaLLM` for processing addresses.
- `success_output`: Path to the file where successful lookups will be saved.
- `failed_path`: Path to the file where failed lookups will be saved.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
