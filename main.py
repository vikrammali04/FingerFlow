import cv2
import mediapipe
from utils import ColorDrawer


def main():
    """
    Runs the main logic for hand detection and drawing on the canvas based on hand gestures.
    Uses the MediaPipe Hands model for hand detection and the ColorDrawer class for drawing functionalities.
    Handles color selection, canvas clearing, button interactions, and drawing lines on the canvas and camera frame.
    """     
    hand_detector = mediapipe.solutions.hands.Hands(model_complexity=1,
                                                    min_detection_confidence=0.3,
                                              min_tracking_confidence=0.6)
    cap = cv2.VideoCapture(0)
    drawer = ColorDrawer()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand_detector.process(frame_rgb)
        hands = result.multi_hand_landmarks

        # Drawing and color selection logic
        if hands:
            landmarks = []
            for hand in hands:
                detected_landmarks = hand.landmark
                for landmark in detected_landmarks:
                    lmx = int(landmark.x * 640)
                    lmy = int(landmark.y * 480)
                    landmarks.append([lmx, lmy])

            fore_finger = (landmarks[8][0], landmarks[8][1])
            thumb = (landmarks[4][0], landmarks[4][1])

            # Draw the fingertip
            cv2.circle(frame, fore_finger, 3,
                       drawer.colors[drawer.colorIndex], -1)

            # Button interaction logic
            if (thumb[1] - fore_finger[1] < 30):
                # Preventing drawing when fore finger is near to thumb.
                drawer.add_next_deques()

            elif fore_finger[1] <= 65:
                # In button mode
                if 40 <= fore_finger[0] <= 140:  # Clear Button
                    drawer.clear_canvas()
                elif 160 <= fore_finger[0] <= 260:
                    drawer.update_color_index(0)  # Blue
                elif 280 <= fore_finger[0] <= 380:
                    drawer.update_color_index(1)  # Green
                elif 400 <= fore_finger[0] <= 500:
                    drawer.update_color_index(2)  # Red
                    
            else:
                drawer.add_point(fore_finger)
        else:
            drawer.add_next_deques()

        # Draw lines of all the colors on the canvas and frame
        points = drawer.get_points()

        for i in range(len(points)):
            for j in range(len(points[i])):
                for k in range(1, len(points[i][j])):
                    if points[i][j][k - 1] is None or points[i][j][k] is None:
                        continue
                    cv2.line(frame, points[i][j][k - 1],
                             points[i][j][k], drawer.colors[i], 4)
                    cv2.line(
                        drawer.paintWindow, points[i][j][k - 1], points[i][j][k], drawer.colors[i], 4)

        cv2.imshow("Canvas", drawer.paintWindow)
        cv2.imshow("Camera", drawer.update_camera_ui(frame=frame))
        if cv2.waitKey(1) == ord('q'):
            # Press 'q' to exit the application. 
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
