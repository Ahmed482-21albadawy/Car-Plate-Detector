import os
import xml.etree.ElementTree as ET

def convert_voc_to_yolo(xml_folder, image_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for xml_file in os.listdir(xml_folder):
        if not xml_file.endswith(".xml"):
            continue
        
        tree = ET.parse(os.path.join(xml_folder, xml_file))
        root = tree.getroot()
        
        image_filename = root.find("filename").text
        
        img_width = int(root.find("size/width").text)
        img_height = int(root.find("size/height").text)
        
        yolo_annotations = []
        for obj in root.findall("object"):
            class_name = obj.find("name").text
            if class_name != "licence":
                continue  # Skip if not a number plate
            
            bbox = obj.find("bndbox")
            xmin = int(bbox.find("xmin").text)
            ymin = int(bbox.find("ymin").text)
            xmax = int(bbox.find("xmax").text)
            ymax = int(bbox.find("ymax").text)
            
            # Convert to YOLO format
            x_center = (xmin + xmax) / (2 * img_width)
            y_center = (ymin + ymax) / (2 * img_height)
            bbox_width = (xmax - xmin) / img_width
            bbox_height = (ymax - ymin) / img_height
            
            yolo_annotations.append(f"0 {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}")
        
        # Save YOLO annotations
        txt_filename = os.path.splitext(image_filename)[0] + ".txt"
        with open(os.path.join(output_folder, txt_filename), "w") as f:
            f.write("\n".join(yolo_annotations))

# Define paths
xml_folder = "annotations"  # Update with your actual folder path
image_folder = "images"      # Update if needed
output_folder = "labels"     # New folder for YOLO TXT files

# Run conversion
convert_voc_to_yolo(xml_folder, image_folder, output_folder)
print("Conversion completed! YOLO labels saved in 'labels/' folder.")
