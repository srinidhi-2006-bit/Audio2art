import streamlit as st
import speech_recognition as sr
from diffusers import StableDiffusionPipeline
import torch

# Ensure PyTorch is installed properly
try:
    print("Torch Version:", torch.__version__)  # ✅ Corrected PyTorch version check
except ModuleNotFoundError:
    st.error("❌ PyTorch is not installed. Please install it using 'pip install torch'.")

# Load Stable Diffusion Model (Cached to avoid reloading)
@st.cache_resource
def load_stable_diffusion():
    return StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

sd_model = load_stable_diffusion()

# ✅ Apply Background Image Fix
page_bg_img = '''
<style>
    .stApp {
        background: url("https://github.com/NANDHIKA080/image/blob/main/Screenshot%20(440).png?raw=true") no-repeat center fixed;
        background-size: cover;
    }
    h1, h3, .stMarkdown, label {
        color: black !important;
        font-weight: bold !important;
    }
    .stTextInput>div>div>input, .stFileUploader>div {
        color: black !important;
        font-weight: bold !important;
    }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# 🎤 Title Section with Styled Text
st.markdown('<h1 style="text-align:center; color:black; font-weight:bold;">🎤 Audio2Art</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align:center; color:black; font-weight:bold;">Transform Your Voice into Art with AI</h3>', unsafe_allow_html=True)
st.markdown('<h2 style="color:black; font-weight:bold;">🎧 Upload or Record Your Voice</h2>', unsafe_allow_html=True)

col1, = st.columns(1)  # ✅ Corrected unpacking

with col1:
    audio_file = st.file_uploader("Upload your voice command (WAV format)", type=["wav"])


if audio_file:
    st.markdown('''
    <div style="
        background-color: #cce5ff; 
        color: black; 
        font-weight: bold; 
        padding: 10px; 
        border-radius: 5px;
        border-left: 5px solid #007bff;">
        🎵 Uploaded Audio File:

    </div>
''', unsafe_allow_html=True)
    st.audio(audio_file, format="audio/wav")

    # Save the uploaded file temporarily
    audio_path = "input_audio.wav"
    with open(audio_path, "wb") as f:
        f.write(audio_file.getbuffer())

    st.markdown('''
    <div style="
        background-color: #d4edda; 
        color: black; 
        font-weight: bold; 
        padding: 10px; 
        border-radius: 5px;
        border-left: 5px solid #28a745;">
        ✅ Audio uploaded successfully! Now converting to text...
    </div>
''', unsafe_allow_html=True)


    # Speech-to-Text Function
    def speech_to_text(file_path):
        recognizer = sr.Recognizer()
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            st.error("❌ Could not understand the audio.")
        except sr.RequestError:
            st.error("❌ Could not request results from Google Speech Recognition service.")
        return None
    transcript_text = speech_to_text(audio_path)

    if transcript_text:
        st.markdown('<h2 style="color:black; font-weight:bold;">📝 Transcribed Text:</h2>', unsafe_allow_html=True)
        st.write(f"{transcript_text}")

        # Generate image using Stable Diffusion
        def generate_image(prompt):
            try:
                with st.spinner("🎨 Generating Art... Please wait"):
                    image = sd_model(prompt).images[0]
                    image_path = "generated_art.png"
                    image.save(image_path)
                    return image_path
            except Exception as e:
                st.error(f"❌ Error in Image Generation: {e}")
                return None

        image_path = generate_image(f"A beautiful artistic interpretation of: {transcript_text}")

        if image_path:
            st.image(image_path, caption="🎨 Generated Artwork", use_container_width=True)
