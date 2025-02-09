import streamlit as st
import whisper
import tempfile
import os
from dotenv import load_dotenv
from pydub import AudioSegment
import openai
from PIL import Image, ImageDraw, ImageFont
import requests

load_dotenv()
# Set your OpenAI API key (replace with your actual key or set via your .env file)
openai.api_key = os.getenv("OPENAI_API_KEY")



# Streamlit app layout
st.logo(
    "logo.png",
    size="medium",
    link="https://github.com/talibraath",
)

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("meme_template.jpg", "wb") as f:
            f.write(response.content)
        print("Image downloaded successfully.")
    else:
        print("Failed to download image. Status code:", response.status_code)





@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")

model = load_whisper_model()



# Function to transcribe speech to text using Whisper
def transcribe_audio(audio_file):
    # Convert the uploaded file to a format Whisper can understand (wav)
    audio = AudioSegment.from_file(audio_file)
    
    # Save the audio as a temporary WAV file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        audio.export(tmp_file, format="wav")
        tmp_file_path = tmp_file.name

    # Load the audio into Whisper
    audio_array = whisper.load_audio(tmp_file_path)
    
    # Transcribe the audio
    result = model.transcribe(audio_array)
    
    # Cleanup: Delete the temporary file after processing
    os.remove(tmp_file_path)
    
    return result['text']



st.title("AI Voice Meme Generator")
st.write("Record or upload an audio clip, let AI generate a funny meme caption, and create your meme!")
audio_file = st.file_uploader("Upload your voice recording (in mp3 or wav format)", type=['mp3', 'wav'])

transcription = None

if audio_file:
    transcription = transcribe_audio(audio_file) 
    st.write("Transcription:",transcription)
# Process recorded audio input using st.audio_input
st.write("OR")
audio_value = st.audio_input("Record a voice message to transcribe", key="audio_input_1")
if audio_value:
    # Write the uploaded audio to a temporary file and then pass its path to model.transcribe
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_value.read())
        temp_audio_path = temp_audio.name
    result = model.transcribe(temp_audio_path)
    transcription = result["text"]
    st.write(transcription)
    os.remove(temp_audio_path)
st.write("OR")

# Get the user's meme caption
transcription = st.text_input("Enter your meme caption:")


if transcription:
    if st.button("Generate Meme Caption"):
        prompt = f"Generate a funny meme caption for the following text:\n\n{transcription}\n\nMeme Caption:"
        with st.spinner("Generating Image..."):
            response = openai.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            caption = response.data[0].url
        download_image(caption)
        image = Image.open("meme_template.jpg")
        st.subheader("Meme")
        st.image(image, caption="Your AI-Generated Meme", use_container_width=True)
