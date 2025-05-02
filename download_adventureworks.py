import os
import requests
import zipfile
import shutil

def download_adventureworks():
    # Create data directory if it doesn't exist
    data_dir = 'adventureworks_data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Download AdventureWorks data
    url = "https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorks-oltp-install-script.zip"
    zip_path = os.path.join(data_dir, "adventureworks.zip")
    
    print("Downloading AdventureWorks data...")
    response = requests.get(url, stream=True)
    with open(zip_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    # Extract the zip file
    print("Extracting files...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(data_dir)

    # Clean up zip file
    os.remove(zip_path)
    print("Download and extraction complete!")

if __name__ == "__main__":
    download_adventureworks()
