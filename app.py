from flask import Flask, request, render_template, jsonify
import cv2
import pytesseract
import os
from PIL import Image
from ultralytics import YOLO

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Load the trained model correctly
model = YOLO("best.pt")  # Ensure best.pt exists


# Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Read image & process with YOLO model
    image = cv2.imread(file_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert for better OCR
    results = model(image_rgb)  # Ensure correct input format

    plate_text = ""
    for result in results:
        for box in result.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box[:4])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw bounding box

            # Extract plate region & convert to PIL Image for OCR
            roi = image_rgb[y1:y2, x1:x2]
            plate_pil = Image.fromarray(roi)
            plate_text = pytesseract.image_to_string(plate_pil, config='--psm 7').strip()

    # Save processed image
    result_path = os.path.join(RESULT_FOLDER, file.filename)
    cv2.imwrite(result_path, image)

    return render_template("result.html", image_path=result_path, plate_text=plate_text)

if __name__ == '__main__':
    app.run(debug=True)
    