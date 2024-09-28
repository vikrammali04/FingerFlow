# FingerFlow
A touchless drawing app that lets you create art using hand gestures detected through a webcam, powered by MediaPipe and OpenCV.

## Features
1. Real-time hand gesture detection for drawing on a virtual canvas.
2. Three color options: Blue, Green, and Red.
3. Dynamic color switching and canvas clearing with simple hand gestures.
4. Visual feedback on hand tracking with fingertip highlighting.

## How it Works
The app detects your hand using the MediaPipe Hands model and tracks the position of your forefinger. Based on the movement of your finger, you can draw lines on a virtual canvas displayed alongside your webcam feed.

## Basic Setup
1. Clone the repository:
    **git clone https://github.com/vikrammali04/FingerFlow.git**

2. Change directory:
    **cd FingerFlow**

3. Install dependencies:
    **pip install -r requirements.txt**

4. Run the app:
    **python main.py**

## Usage
* Launch the app and position your hand in front of the webcam.
* Use the forefinger to draw on the canvas.
* Bring your thumb closer to the forefinger to avoid drawing canvas while hovering over       webcam. 
* Switch between colors by hovering over the color selection area at the top of the screen.
* Clear the canvas by hovering over the "Clear" button.
* Press 'q' to exit the application.

## Customization
For personalized results, you can modify the parameters of the hand detection model:
You can adjust:

1. *model_complexity*: Affects the accuracy and inference latency of hand detection.
2. *min_detection_confidence*: Controls the minimum threshold for detecting a hand.
3. *min_tracking_confidence*: Affects how well the app tracks hand movements.

## Note
While the app has been thoroughly tested, the accuracy of the drawn points and the smoothness of the experience may vary depending on your webcam's resolution, frame rate, and other factors like lighting conditions. For the best experience, use a webcam with higher resolution and adjust the parameters to suit your camera's performance.