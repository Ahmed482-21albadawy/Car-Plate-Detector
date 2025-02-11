# Car License Plate Detection using YOLOv8

## 🚀 Project Overview

This project is a **Car License Plate Detection System** using **YOLOv8** and **Flask**. The model detects and extracts license plate numbers from images and displays the results through a web interface.

## 📌 Features

- **License Plate Detection** using YOLOv8.
- **OCR (Optical Character Recognition)** to extract plate numbers.
- **Web Interface** for easy image upload and result visualization.
- **End-to-End Workflow** from dataset preparation to model deployment.
- **Model Training, Validation, and Testing** included.
- **Evaluation Metrics:** Accuracy, Loss (Training & Validation), and Confusion Matrix.
- **Testing on External Images** is supported.

## 💂️ Project Structure

```
📺 Car-Plate-Detection
├── 📁 static
│   ├── 📁 uploads        # Uploaded images
│   ├── 📁 results        # Processed images with detected plates
├── 📁 templates          # HTML files (index.html, result.html)
├── 📁 dataset            # Training and validation images
├── 📁 TESTING            # Testing images folder
├── SplittingData.py    # Script for dataset splitting
├── ModelTraining.py    # Model training, validation, and evaluation script
├── convert.py          # Converts XML annotations to YOLO format
├── app.py              # Flask application
├── best.pt             # Trained YOLOv8 model weights
├── requirements.txt    # Required dependencies
├── README.md           # Project documentation
```

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Car-Plate-Detection.git
   cd Car-Plate-Detection
   ```
2. **Create a virtual environment & Install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   pip install -r requirements.txt
   ```
3. **Download the Trained Model**\
   Place the trained **best.pt** file in the project directory.

## 🔥 Running the Project

1. **Start the Flask App:**
   ```bash
   python app.py
   ```
2. Open your browser and go to **`http://127.0.0.1:5000/`**.

## 🧪 Training & Evaluation

1. **Run Model Training:**
   ```bash
   python ModelTraining.py
   ```
2. **Metrics Tracked:**
   - Training & Validation Accuracy
   - Training & Validation Loss
   - Confusion Matrix
   - Precision, Recall, and mAP

## 🧪 Testing the Model

1. **On a Testing Dataset:**
   ```bash
   python ModelTraining.py --test
   ```
   - This will evaluate the model on the testing images and return performance metrics.

2. **On an External Image:**
   ```python
   from ultralytics import YOLO
   import cv2
   import matplotlib.pyplot as plt
   
   # Load trained model
   model = YOLO("best.pt")  # Update path if needed
   
   # Provide the path to an external image
   image_path = "TESTING/sample_image.jpg"  # Replace with your image path
   
   # Run inference
   results = model(image_path)
   
   # Display the image with detections
   img = cv2.imread(image_path)
   img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   plt.imshow(img)
   plt.axis("off")
   plt.show()
   ```

## 📊 Model Performance

| Metric     | Value |
| ---------- | ----- |
| Precision  | 0.896 |
| Recall     | 0.884 |
| mAP@50    | 0.893 |
| mAP@50-95 | 0.52  |


## 🤖 Technologies Used

- **Python** (Flask, OpenCV, PyTorch, NumPy)
- **YOLOv8** for object detection
- **Tesseract OCR** for text extraction

## 🎓 Credits

- Developed by **Ahmed** as part of an **NTI & Huawei AI Course Project**.
- Dataset: [Kaggle - Car Plate Detection](https://www.kaggle.com/datasets/andrewmvd/car-plate-detection)

## 🏁 Future Improvements

- Add real-time video detection.
- Improve OCR accuracy with preprocessing techniques.
- Deploy as a web service using **Heroku** or **AWS**.

---

💡 **Feel free to contribute or improve the project!** 🚀

