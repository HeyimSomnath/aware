# A.W.A.R.E. - AI Wakefulness and Alertness Recognition Engine.

🛌 Real-Time Drowsiness Detection System With OpenCV & Dlib

Alright, here’s the lowdown. I cooked up a drowsiness detection setup that actually works in real-time, using good ol’ OpenCV, Dlib, and a sprinkle of facial landmark wizardry. Basically, it watches your eyeballs and figures out if you’re awake, getting sleepy, or straight-up about to faceplant into your keyboard. Super handy for drivers, night owls, or anyone who just can’t keep their eyes open but needs to.

📌 What’s cool about it?

👁️ Checks your blink ratio using all 68 facial landmarks (yeah, it’s that precise).

🟢 Real-time video—you see yourself as the code sees you. Spooky, but useful.

💤 Actually figures out if you’re dozing off or just zoning out.

🔊 Hits you with a beep if you’re nodding off (it’s not subtle, trust me).

🧠 Leaning on Dlib’s shape_predictor_68_face_landmarks.dat, ‘cause who wants to train that from scratch?

📈 Shows live FPS so you know if your potato PC is keeping up.

🧠 How it Actually Does Its Thing

So, it does some math magic—calculates the Eye Aspect Ratio (EAR) for both your eyes. If you close your eyes for a few frames in a row? Boom, it throws an alert. If your eyes are wide open, you’re good. Simple.

📂 What You’ll Need

- Python 3.x (don’t even try this with 2.x, you’ll just cry)
- OpenCV
- Dlib
- imutils
- NumPy
- winsound (if you’re on Windows and want those sweet, sweet beeps)

📦 How to Get it Running

Just hit:

```pip install opencv-python dlib imutils numpy```

Then grab the shape predictor (shape_predictor_68_face_landmarks.dat), unzip it, and toss it in your project folder. Easy.

▶️ Fire It Up

```python drowsiness_detector.py```

Want out? Smash the ESC key.

🚨 Heads Up

Those EAR thresholds? (like 0.25 for awake, 0.21 for snoozing) You might need to tweak ‘em, especially if you have dramatic eyelashes or weird lighting. Not kidding. 

On Linux or macOS and the beep won’t work? Try pygame or playsound. Sorry, Windows-only for winsound.

So, there you go. Plug it in, stay awake, and don’t forget to blink.
