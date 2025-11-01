import os
from PIL import Image

# --- Configuration ---
input_folder = "images_input"       # Folder containing original images
output_folder = "images_resized"    # Folder to save resized images
new_size = (800, 800)               # Desired size (width, height)
output_format = "JPEG"              # Output format (e.g., "JPEG", "PNG")

# --- Ensure output folder exists ---
os.makedirs(output_folder, exist_ok=True)

# --- Process each image ---
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # Resize image
        img_resized = img.resize(new_size)
        
        # Convert filename and save
        base_name = os.path.splitext(filename)[0]
        save_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
        
        img_resized.save(save_path, output_format)
        print(f"Saved resized image: {save_path}")

print("\n All images resized and saved successfully!")
