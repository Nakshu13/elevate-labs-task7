# elevate-labs-task7
🖼️ Image Resizer Tool
🎯 Objective
Automatically resize and convert multiple images in a folder using Python.
This script helps you save time by processing all images at once — ideal for batch resizing before uploads or optimization tasks.

⚙️ Tools & Technologies

Language: Python

📦 Features
✅ Batch resize all images in a folder
✅ Convert images to any desired format (e.g., JPEG, PNG)
✅ Automatically create output folders if missing
✅ Handles different image modes (RGB, RGBA, P, etc.)
✅ Prevents crashes for unsupported formats

Set up your project folder structure:

Image Resizer Tool/
├── Image_resizer.py
├── images_input/        
└── images_resized/      # Resized images will be saved here (auto-created)

🧩 Usage Instructions

Place images (like .jpg, .png, .jpeg, etc.) inside the images_input folder.

🧠 How It Works
Uses os.listdir() to loop through all files in the input directory.
Opens each image with PIL.Image.open().
Resizes it using .resize() and converts the mode if needed.
Saves the processed image in the output folder with the specified format.


🧪 Example Output
✅ Saved resized image: images_resized/dog.jpeg
✅ Saved resized image: images_resized/cat.jpeg

🎉 All images resized and saved successfully!

🪄 Optional Customizations

Change image dimensions:
new_size = (1024, 1024)

Preserve transparency (use PNG format):
output_format = "PNG"

🧑‍💻 Author

Developed by Nithyasri R
For learning automation using Python + Pillow.
