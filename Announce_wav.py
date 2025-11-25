import os
import io
from gtts import gTTS
from pydub import AudioSegment

def create_768k_wav():
    print("Using female British Announcer Voice. WSJT-X seems to want .wav at 16-bit/48kHz/768kbps")
    print("Type 'exit' to quit.")

    while True:
        print("\n" + "="*40)
        
        # 1. Get the announcement text
        text_input = input("Enter the announcement text: ").strip()
        
        if text_input.lower() == 'exit':
            break
        
        if not text_input:
            continue

        # 2. Get the filename...without the .wav extension
        filename_input = input("Enter filename to save (e.g. 'NewGridOnBand'): ").strip()
        if not filename_input.lower().endswith(".wav"):
            filename_input += ".wav"

        print(f"Generating 768kbps .WAV for: '{text_input}'...")

        try:
            # --- Generate Speech .mp3 first ---
            mp3_fp = io.BytesIO()
            # 'tld=co.uk' forces the British accent, because it's cool - change here
            tts = gTTS(text=text_input, lang='en', tld='co.uk', slow=False)
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)

            # --- Convert from mp3 using Pydub ---
            audio = AudioSegment.from_file(mp3_fp, format="mp3")

            # Make it Mono (1 Channel)
            audio = audio.set_channels(1)

            # Set Sample Rate to 48000 Hz
            audio = audio.set_frame_rate(48000)
            
            # Set Bit Depth to 16-bit (2 bytes) so 48000 Hz * 16 bits * 1 channel = 768,000 bps (768 kbps)
            audio = audio.set_sample_width(2)

            # Export pcm_s16le = PCM Signed 16-bit Little Endian .wav file
            audio.export(filename_input, format="wav", codec="pcm_s16le")
            
            print(f"Tada! Saved as: {os.path.abspath(filename_input)}")
            
        except Exception as e:
            print(f"Error: {e}")
            print("Note: Ensure FFmpeg file are in the dir with this .py file.")

if __name__ == "__main__":
    create_768k_wav()