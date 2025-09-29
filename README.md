<h1>🪨📄✂️ Rock Paper Scissors Hand Recognition</h1>

<p>This is a simple <b>Computer Vision project</b> that detects whether your hand is showing 
<b>Rock (✊)</b>, <b>Paper (🖐️)</b>, or <b>Scissors (✌️)</b> using <b>Python, OpenCV, and MediaPipe</b>.
It uses <b>hand landmarks detection</b> to count fingers and classify the gesture.</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>Real-time hand tracking with <b>MediaPipe</b></li>
  <li>Finger counting to determine gesture</li>
  <li>Recognizes <b>Rock, Paper, Scissors</b></li>
  <li>Displays the result on the screen</li>
</ul>

<h2>📦 Requirements</h2>
<pre>
pip install opencv-python mediapipe
</pre>

<h2>🛠️ How It Works</h2>
<ol>
  <li>Capture frames from the webcam.</li>
  <li>Use <b>MediaPipe Hands</b> to detect 21 hand landmarks.</li>
  <li>Count open fingers:
    <ul>
      <li>0 fingers → Rock (✊)</li>
      <li>2 fingers (index + middle) → Scissors (✌️)</li>
      <li>5 fingers → Paper (🖐️)</li>
    </ul>
  </li>
  <li>Display the gesture name on the screen.</li>
</ol>

<h2>▶️ Run the Project</h2>
<pre>
python rock_paper_scissors.py
</pre>
<p>Press <b>ESC</b> to exit.</p>

<h2>📸 Demo</h2>
<p>Example output (with landmarks drawn on the hand):</p>
<pre>
Rock ✊ | Scissors ✌️ | Paper 🖐️
</pre>

<h2>📂 Project Structure</h2>
<pre>
.
├── rock_paper_scissors.py   # main code
├── README.md                # project documentation
</pre>

<h2>✨ Future Improvements</h2>
<ul>
  <li>Add support for both hands</li>
  <li>Use a <b>CNN model</b> for more accurate classification</li>
  <li>Create a <b>multiplayer game mode</b></li>
</ul>

<h2>🤝 Contributing</h2>
<p>Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.</p>

<h2>📜 License</h2>
<p>This project is licensed under the <b>MIT License</b>.</p>
