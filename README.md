🪨📄✂️ Rock Paper Scissors Hand Recognition

This is a simple Computer Vision project that detects whether your hand is showing Rock (✊), Paper (🖐️), or Scissors (✌️) using Python, OpenCV, and MediaPipe.
It uses hand landmarks detection to count fingers and classify the gesture.

🚀 Features

Real-time hand tracking with MediaPipe

Finger counting to determine gesture

Recognizes Rock, Paper, Scissors

Displays the result on the screen

📦 Requirements

Install the required Python libraries:

pip install opencv-python mediapipe

🛠️ How It Works

Capture frames from the webcam.

Use MediaPipe Hands to detect 21 hand landmarks.

Count open fingers:

0 fingers → Rock (✊)

2 fingers (index + middle) → Scissors (✌️)

5 fingers → Paper (🖐️)

Display the gesture name on the screen.

▶️ Run the Project
python rock_paper_scissors.py


Press ESC to exit.

📸 Demo

Example output (with landmarks drawn on the hand):

Rock ✊ | Scissors ✌️ | Paper 🖐️

📂 Project Structure
.
├── rock_paper_scissors.py   # main code
├── README.md                # project documentation

✨ Future Improvements

Add support for both hands

Use a CNN model for more accurate classification

Create a multiplayer game mode

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📜 License

This project is licensed under the MIT License.
