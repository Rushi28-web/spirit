# spirit

Colored Sketch Generator using OpenCV
This project converts a normal image into a colored sketch effect using Python and OpenCV. It applies edge detection, smoothing filters, and blending techniques to create a visually appealing animated sketch transformation.

🚀 Features
Convert image to sketch (edge detection)
Smooth color filtering using bilateral filter
Blend sketch and original image
Animated transition effect
Simple and beginner-friendly implementation

🛠️ Technologies Used
Python
OpenCV (cv2)
NumPy

📸 Output Preview
Sketch Effect (Edge Detection)
Colored Sketch Blend
Smooth Transition Animation

<img width="675" height="748" alt="image" src="https://github.com/user-attachments/assets/df76e516-7625-4edf-9e47-ffa55b848982" />
<img width="940" height="500" alt="image" src="https://github.com/user-attachments/assets/c7d87eff-c042-425f-852c-342a58f14440" />
<img width="940" height="479" alt="image" src="https://github.com/user-attachments/assets/0a969835-a1d7-4f9c-b68f-4e7285fd417f" />

📂 Project Structure
📁 spirit
 ┣ 📄 spirit.py
 ┣ 📄 image.jpeg

 ⚙️ Installation & Setup
Clone the repository:

git clone https://github.com/your-username/colored-sketch-generator.git
cd colored-sketch-generator

Install dependencies:
pip install opencv-python numpy

Run the project:
python main.py
 
🧠 How It Works
Load and resize the image
Convert to grayscale
Apply Gaussian blur
Detect edges using Canny
Invert edges to create sketch
Apply bilateral filter for smooth colors
Blend sketch and color image
Animate the transition effect

💡Code Snippet
edges = cv2.Canny(blur, 50, 150)
sketch = cv2.bitwise_not(edges)
color = cv2.bilateralFilter(img, d=9, sigmaColor=200, sigmaSpace=200)
blended = cv2.addWeighted(color, alpha, sketch_color, 1 - alpha, 0)

📌 Future Improvements
Add GUI using Tkinter or PyQt
Support video sketch conversion
Add multiple sketch styles
Save output as image/video
