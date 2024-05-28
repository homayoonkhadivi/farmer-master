import os
import wget

# Function to download the dataset if not already present
def download_dataset(url, filename):
    if not os.path.exists(filename):
        print("Downloading dataset...")
        wget.download(url, filename)
        print("Dataset downloaded successfully.")
    else:
        print("Dataset already exists. Skipping download.")

# URL of the dataset
url = "https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/383116/rawdata_new.csv?sequence=1&isAllowed=y"
# Local filename
filename = "data_raw.csv"

# Download the dataset if not already present
download_dataset(url, filename)

