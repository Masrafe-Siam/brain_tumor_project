import os

# 🔧 Set your folder path
folder_path = r'D:\\Masrafe\\Coding\\Git_Hub_code\\ml_project\\brain_tumor_project\\Dataset\\Training\\pituitary_tumor'  # <-- Change this!

# 🔧 Base name
base_name = "pituitary_tumor"

# 🖼️ Image file extensions to look for
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

# 📂 Get all image files
image_files = [f for f in os.listdir(folder_path)
               if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() in image_extensions]

# 🔢 Sort to keep the order consistent
image_files.sort()

# 🚀 Rename the files
for i, filename in enumerate(image_files, start=1):
    ext = os.path.splitext(filename)[1].lower()
    new_name = f"{base_name}_{i}{ext}"
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    os.rename(src, dst)
    print(f"Renamed: {filename} -> {new_name}")
