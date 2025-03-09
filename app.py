import streamlit as st
import speech_recognition as sr
from diffusers import StableDiffusionPipeline
import torch

# Ensure PyTorch is installed properly
try:
    print("Torch Version:", torch.__version__)
except ModuleNotFoundError:
    st.error("❌ PyTorch is not installed. Please install it using 'pip install torch'.")

# Load Stable Diffusion Model (Cached to avoid reloading)
@st.cache_resource
def load_stable_diffusion():
    return StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

sd_model = load_stable_diffusion()

# Title
st.title("🎤 Audio2Art - Generate Art from Voice")

# Voice Input
st.subheader("🎧 Upload or Record Your Voice")
audio_file = st.file_uploader("Upload your voice command (WAV format)", type=["wav"])

if audio_file:
    st.audio(audio_file, format="audio/wav")

    # Save the uploaded file temporarily
    audio_path = "input_audio.wav"
    with open(audio_path, "wb") as f:
        f.write(audio_file.getbuffer())

    st.success("✅ Audio uploaded successfully! Now converting to text...")

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
        st.write("📝 *Transcribed Text:*", transcript_text)

        # Generate image using Stable Diffusion
        def generate_image(prompt):
            try:
                image = sd_model(prompt).images[0]
                image_path = "generated_art.png"
                image.save(image_path)
                return image_path
            except Exception as e:
                st.error(f"❌ Error in Image Generation: {e}")
                return None

        st.write("🖼 *Generating Art...*")
        image_path = generate_image(f"A beautiful artistic interpretation of: {transcript_text}")

        if image_path:
            st.image(image_path, caption="🎨 *Generated Artwork*", use_container_width=True)
