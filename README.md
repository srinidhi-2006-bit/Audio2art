---md
# 🎤 Audio2Art – Transform Voice into AI Art

Audio2Art is a Streamlit-based AI application that converts **spoken audio commands into artistic images** using **Speech Recognition** and **Stable Diffusion**.  
Users upload a voice recording, which is transcribed into text and then transformed into AI-generated artwork.

---

## 🚀 Features

- 🎧 Upload audio (WAV format)
- 📝 Convert speech to text using Google Speech Recognition
- 🎨 Generate images from text using Stable Diffusion
- 🖼️ Display generated artwork instantly
- 🌈 Custom background and styled UI
- ⚡ Cached model loading for better performance

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit** – Web UI
- **SpeechRecognition** – Audio to text
- **PyTorch** – Deep learning backend
- **Diffusers** – Stable Diffusion image generation
- **Transformers**
- **SoundFile**

---

## 📁 Project Structure

```

Audio2art/
│── app.py
│── requirements.txt
│── README.md
│── input_audio.wav        # temporary (auto-generated)
│── generated_art.png      # output image

```

---

## 📦 Installation (Without Virtual Environment)

### 1️⃣ Upgrade pip
```

python -m pip install --upgrade pip

```

### 2️⃣ Install dependencies
```

pip install -r requirements.txt

```

If needed, install manually:
```

pip install streamlit torch torchaudio diffusers transformers soundfile SpeechRecognition

```

---

## ▶️ Run the Application

```

streamlit run app.py

```

After running, open:
```

[http://localhost:8501](http://localhost:8501)

```

---

## 📌 Usage Instructions

1. Open the web app
2. Upload a **WAV audio file**
3. The app converts speech to text
4. The text is used as a prompt
5. AI generates and displays artwork

---

## ⚠️ Important Notes

- Stable Diffusion works best with **GPU**
- On CPU, image generation may be slow
- Internet is required for Google Speech Recognition
- Only WAV audio format is supported

---

## 🎓 Academic Use

This project is suitable for:
- Mini Project
- AI / ML Lab
- Data Science Portfolio
- Hackathons
- Final Year Project Prototype

---

## ✨ Future Enhancements

- 🎙️ Live microphone recording
- 🖌️ Style selection (realistic, anime, sketch)
- ☁️ Cloud deployment (Streamlit Cloud)
- 💾 Download generated images
- ⚡ Faster CPU-optimized models

---
