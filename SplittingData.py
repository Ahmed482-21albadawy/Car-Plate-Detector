import os
import shutil
import glob
from sklearn.model_selection import train_test_split


images_path = "images"
labels_path = "labels"

# Define split folders
output_dirs = {
    "train": "dataset/train",
    "val": "dataset/val",
    "test": "dataset/test"
}

# Create directories for images and labels
for split in output_dirs:
    os.makedirs(os.path.join(output_dirs[split], "images"), exist_ok=True)
    os.makedirs(os.path.join(output_dirs[split], "labels"), exist_ok=True)

# Get all YOLO label files
label_files = glob.glob(os.path.join(labels_path, "*.txt"))

# Filter valid images with labels
valid_image_files = []
valid_label_files = []

for lbl in label_files:
    img_path = os.path.join(images_path, os.path.basename(lbl).replace(".txt", ".png"))
    
    if os.path.exists(img_path):  # Only include if the image exists
        valid_image_files.append(img_path)
        valid_label_files.append(lbl)
    else:
        print(f"⚠️ Warning: Label {os.path.basename(lbl)} has no matching image and will be skipped.")

# Print counts
print(f"✅ Found {len(valid_image_files)} images and {len(valid_label_files)} labels.")

# Split dataset (70% train, 15% val, 15% test)
train_images, temp_images, train_labels, temp_labels = train_test_split(
    valid_image_files, valid_label_files, test_size=0.30, random_state=42
)
val_images, test_images, val_labels, test_labels = train_test_split(
    temp_images, temp_labels, test_size=0.50, random_state=42
)

# Function to move files
def move_files(image_list, label_list, split):
    for img, lbl in zip(image_list, label_list):
        shutil.move(img, os.path.join(output_dirs[split], "images", os.path.basename(img)))
        shutil.move(lbl, os.path.join(output_dirs[split], "labels", os.path.basename(lbl)))

# Move files to corresponding folders
move_files(train_images, train_labels, "train")
move_files(val_images, val_labels, "val")
move_files(test_images, test_labels, "test")

print("✅ Dataset split completed successfully!")
