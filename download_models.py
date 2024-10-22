import os
import requests

# Create the directory if it doesn't exist
save_dir = 'ControlNet\models'
os.makedirs(save_dir, exist_ok=True)

# URL of the .pth file you want to download
url = "https://huggingface.co/lllyasviel/ControlNet/resolve/main/control_sd15_hed.pth"  # replace with the actual URL

# Full path where the file will be saved
output_path = os.path.join(save_dir, "control_sd15_hed.pth")

# Download the file
response = requests.get(url)
with open(output_path, 'wb') as f:
    f.write(response.content)

print(f"Downloaded to {output_path}")
