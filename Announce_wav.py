import asyncio
import edge_tts
import io
import os
from pydub import AudioSegment

# WSJT-X announcement maker by ErnieTech
# VOICE SELECTION
# "en-GB-SoniaNeural" is the standard pleasant British female voice.
# "en-GB-LibbyNeural" is another good option if you want a slight variation.
VOICE = "en-GB-SoniaNeural"

async def generate_audio_stream(text):
    """
    Generates MP3 audio bytes using Microsoft Edge's Neural TTS.
    """
    communicate = edge_tts.Communicate(text, VOICE, rate="+5%")
    mp3_data = b""
    
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            mp3_data += chunk["data"]
            
    return mp3_data

def convert_and_save(mp3_bytes, filename):
    """
    Converts MP3 bytes to 768kbps WAV (48kHz, 16-bit, Mono)
    """
    # Load MP3 from memory
    audio = AudioSegment.from_file(io.BytesIO(mp3_bytes), format="mp3")

    # --- Force 768 kbps Parameters ---
    # 1. Force Mono (1 Channel)
    audio = audio.set_channels(1)

    # 2. Set Sample Rate to 48000 Hz
    audio = audio.set_frame_rate(48000)
    
    # 3. Set Bit Depth to 16-bit (2 bytes)
    # Math: 48000 Hz * 16 bits * 1 channel = 768,000 bps (768 kbps)
    audio = audio.set_sample_width(2)

    # Export as PCM Signed 16-bit Little Endian
    audio.export(filename, format="wav", codec="pcm_s16le")
    print(f"Success! Saved as: {os.path.abspath(filename)}")

async def main_loop():
    print(f"--- Edge-TTS Neural Announcer (Voice: {VOICE}) ---")
    print("Output Format: WAV (48kHz, 16-bit, Mono, 768kbps)")
    print("Type 'exit' to quit.")

    while True:
        print("\n" + "="*40)
        
        # 1. Get Text
        text_input = input("Enter the announcement text: ").strip()
        
        if text_input.lower() == 'exit':
            break
        if not text_input:
            continue

        # 2. Get Filename
        filename_input = input("Enter filename (e.g. 'alert01'): ").strip()
        if not filename_input.lower().endswith(".wav"):
            filename_input += ".wav"

        print(f"Downloading neural audio for: '{text_input}'...")

        try:
            # Generate the MP3 data in memory
            mp3_bytes = await generate_audio_stream(text_input)
            
            # Process and Save as WAV
            convert_and_save(mp3_bytes, filename_input)
            
        except Exception as e:
            print(f"Error: {e}")
            print("Note: Ensure FFmpeg is installed for pydub to work.")

if __name__ == "__main__":
    # Standard boilerplate to run async code
    asyncio.run(main_loop())
