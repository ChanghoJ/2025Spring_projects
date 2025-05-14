'''
IS 597PR Final Project: Data preparation for ai_model_predictions.csv.zip file  
Name: Changho Jung, Prisha Singhania

The following code is referred from ChatGPT and Changho's previous project of IS477 under CC0-1.0 license: https://github.com/ChanghoJ/is477-fall2023-final-project/blob/main/scripts/prepare_data.py.
The purpose of the code is:  
1. Download ai_model_predictions.csv.zip  
2. Download all secondary datasets:  
   - g_inventor_disambiguated.tsv  
   - g_location_disambiguated.tsv  
   - g_assignee_disambiguated.tsv  
   - g_attorney_disambiguated.tsv  
   - 2025-Public-Data-File.xlsx  
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import requests
import zipfile

# Set your desired download directory
download_dir = os.path.abspath("./data")
os.makedirs(download_dir, exist_ok=True)

# Configure headless Chrome
options = Options()
options.headless = True
options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Start Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Download ai_model_predictions.csv.zip via browser (to bypass auto-download restrictions)
zip_url = "https://data.uspto.gov/ui/datasets/products/files/ECOPATAI/2023/ai_model_predictions.csv.zip"
driver.get(zip_url)

# Wait to ensure the download completes
time.sleep(40)
driver.quit()
print("ai_model_predictions.csv.zip download complete.")

# Dictionary of secondary datasets
dict_patent = {
    "data/g_application.tsv": "https://s3.amazonaws.com/data.patentsview.org/download/g_application.tsv.zip",
    "data/g_attorney_disambiguated.tsv": "https://s3.amazonaws.com/data.patentsview.org/download/g_attorney_disambiguated.tsv.zip",
    "data/g_assignee_disambiguated.tsv": "https://s3.amazonaws.com/data.patentsview.org/download/g_assignee_disambiguated.tsv.zip",
    "data/g_location_disambiguated.tsv": "https://s3.amazonaws.com/data.patentsview.org/download/g_location_disambiguated.tsv.zip",
    "data/g_inventor_disambiguated.tsv": "https://s3.amazonaws.com/data.patentsview.org/download/g_inventor_disambiguated.tsv.zip",
    "data/2025-Public-Data-File.xlsx": "https://carnegieclassifications.acenet.edu/wp-content/uploads/2025/04/2025-Public-Data-File.xlsx"
}

# Download each file if it does not already exist
for file_path, file_url in dict_patent.items():
    if not os.path.exists(file_path):
        try:
            response = requests.get(file_url)
            with open(file_path, mode='wb') as f:
                f.write(response.content)
            print(f"Downloaded: {file_path}")
        except Exception as e:
            print(f"Failed to download {file_path}: {e}")
    else:
        print(f"Already exists: {file_path}")

zip_path = os.path.join(download_dir, "ai_model_predictions.csv.zip")
extract_to = download_dir  # or set another path if you want

if os.path.exists(zip_path):
    try:
        with zipfile.ZipFile(zip_path, mode="r") as archive:
            archive.extractall(path=extract_to)
            print("Unzip of ai_model_predictions.csv.zip complete.")
    except Exception as e:
        print(f"Unzip failed: {e}")
else:
    print("Zip file not found. Please check the download path.")