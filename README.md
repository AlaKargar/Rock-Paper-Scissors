<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Rock Paper Scissors Hand Recognition — README</title>
  <style>
    :root{
      --bg:#0f1724; --card:#0b1220; --muted:#9aa4b2; --accent:#7dd3fc;
      --accent-2:#60a5fa; --text:#e6eef8;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    html,body{height:100%; margin:0; background:linear-gradient(180deg,#071024 0%, #0b1320 100%); color:var(--text);}
    .wrap{max-width:900px;margin:36px auto;padding:28px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); border-radius:12px; box-shadow:0 8px 30px rgba(2,6,23,0.6);}
    h1{font-size:28px;margin:0 0 8px;}
    p.lead{color:var(--muted); margin-top:0;}
    section{margin:18px 0;padding-top:6px;border-top:1px dashed rgba(255,255,255,0.03);}
    ul{margin:8px 0 0 20px;color:var(--muted);}
    pre{background:#071627;padding:14px;border-radius:8px;overflow:auto;color:var(--text);font-size:13px;}
    code{font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", "Courier New", monospace;}
    .pill{display:inline-block;background:linear-gradient(90deg,var(--accent),var(--accent-2)); color:#001b2e; padding:6px 10px;border-radius:999px;font-weight:600;margin-left:6px;}
    .small{font-size:13px;color:var(--muted);}
    .footer{margin-top:22px;font-size:13px;color:var(--muted);}
  </style>
</head>
<body>
  <div class="wrap">
    <h1>🪨📄✂️ Rock Paper Scissors Hand Recognition</h1>
    <p class="lead">A simple Computer Vision project that detects <strong>Rock (✊), Paper (🖐️), or Scissors (✌️)</strong> gestures in real-time using <strong>Python, OpenCV, and MediaPipe</strong>.</p>

    <section>
      <h2>🚀 Features <span class="pill">Lightweight</span></h2>
      <ul>
        <li>Real-time hand tracking with <strong>MediaPipe</strong></li>
        <li>Finger counting to determine gesture</li>
        <li>Recognizes <em>Rock</em>, <em>Paper</em>, <em>Scissors</em></li>
        <li>Displays result directly on the webcam feed</li>
      </ul>
    </section>

    <section>
      <h2>📦 Requirements</h2>
      <p class="small">Install required Python packages:</p>
      <pre><code>pip install opencv-python mediapipe</code></pre>
    </section>

    <section>
      <h2>🛠️ How it works</h2>
      <ol>
        <li>Capture frames from the webcam.</li>
        <li>Use <strong>MediaPipe Hands</strong> to detect 21 hand landmarks.</li>
        <li>Count open fingers (thumb + 4 fingers) to determine gesture:
          <ul>
            <li><strong>0 fingers → Rock (✊)</strong></li>
            <li><strong>2 fingers (index + middle) → Scissors (✌️)</strong></li>
            <li><strong>5 fingers → Paper (🖐️)</strong></li>
          </ul>
        </li>
        <li>Render the gesture name on the image using OpenCV.</li>
      </ol>
    </section>

    <section>
      <h2>▶️ Run the project</h2>
      <p class="small">Save your script (for example <code>rock_paper_scissors.py</code>) and run:</p>
      <pre><code>python rock_paper_scissors.py</code></pre>
      <p class="small">Press <strong>ESC</strong> to exit.</p>
    </section>

    <section>
      <h2>📸 Demo</h2>
      <p class="small">Example output shows the detected gesture name on the webcam with hand landmarks drawn (points & connections):</p>
      <pre><code>Rock ✊ | Scissors ✌️ | Paper 🖐️</code></pre>
    </section>

    <section>
      <h2>📂 Project structure</h2>
      <pre><code>.
├── rock_paper_scissors.py   # main code
├── README.html              # this HTML README
└── LICENSE                  # MIT License (recommended)
</code></pre>
    </section>

    <section>
      <h2>✨ Future improvements</h2>
      <ul>
        <li>Add support for detecting gestures from <strong>both hands</strong></li>
        <li>Train a lightweight <strong>CNN</strong> for more robust classification</li>
        <li>Build a multiplayer game mode or scoreboard</li>
        <li>Improve robustness for different lighting and backgrounds</li>
      </ul>
    </section>

    <section>
      <h2>🤝 Contributing</h2>
      <p class="small">Pull requests are welcome! For major changes, please open an issue first to discuss.</p>
    </section>

    <section>
      <h2>📜 License</h2>
      <p class="small">This project is licensed under the <strong>MIT License</strong>.</p>
    </section>

    <div class="footer">Made with ❤️ — Rock Paper Scissors Hand Recognition</div>
  </div>
</body>
</html>
