# Meme-Me

**Meme-Me** is an AI-powered meme generator that combines voice transcription, natural language processing, and image generation to create funny and personalized memes. This project utilizes cutting-edge AI models like Whisper for transcription and OpenAI's DALL-E for generating meme images.

## Features

- **Audio Transcription**:
  - Transcribe voice recordings into text using OpenAI's Whisper model.
  
- **AI-Generated Meme Captions**:
  - Generate humorous meme captions based on transcribed audio.

- **AI-Generated Meme Images**:
  - Use OpenAI's DALL-E model to create meme images from the generated captions.

- **Interactive Web Application**:
  - Developed with Streamlit for an intuitive and user-friendly interface.

## How It Works

1. **Upload or Record Audio**:
   - Upload an audio file (MP3 or WAV format) or record your voice directly in the app.

2. **Transcription**:
   - The audio is transcribed into text using Whisper, an advanced speech-to-text model.

3. **Caption Generation**:
   - A prompt is created based on the transcribed text, which is then passed to DALL-E to generate meme captions and images.

4. **Meme Creation**:
   - The generated meme image is displayed along with the caption for download.

## Technologies Used

- **Streamlit**:
  - For creating the web-based user interface.
- **Whisper**:
  - OpenAI's speech-to-text model for audio transcription.
- **OpenAI DALL-E**:
  - For generating humorous meme images.
- **Pillow**:
  - For processing and displaying images.
- **Pydub**:
  - For audio format conversion.
- **Tempfile**:
  - For managing temporary files during processing.
- **Requests**:
  - For downloading generated images.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/talibraath/Meme-Me.git
   cd Meme-Me
