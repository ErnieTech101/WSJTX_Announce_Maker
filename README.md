## How to make your own WSJT-X announcements - No microphone needed!

### Make sure you  have Python 3.x.x installed! If you don't, go figure out how to install it.

### First, create a directory to do all your fancy voice creation work. 
- Any directory will do since all of the files will live there, together...in peace and harmony : )

### Download the needed Files
- Go to [Gyan.dev FFmpeg builds](https://www.gyan.dev/ffmpeg/builds/) Download the file labeled `ffmpeg-git-essentials.7z` (or .zip). Unzip to some temp
folder and in the ./bin directory, look for the files: ffmpeg.exe, ffplay.exe & ffprobe.exe. Copy just those three files into the directory you created 
in the first step.

- Next, from this repository, download the Python script `Announce_wav.py` into the same directory.

- Before you run it, install the required Python modules, `pip install pydub` and Google Translate `pip install edge-tts`

### So how do you use it? Simple!

- In a CMD window, go to the directory you created and saved the files into.
- Run the script `python Announce_wav.py`
- Here's how it goes:
- 
--- Edge-TTS Neural Announcer (Voice: en-GB-SoniaNeural) ---
Output Format: WAV (48kHz, 16-bit, Mono, 768kbps)
Type 'exit' to quit.

========================================
Enter the announcement text: New CQ Zone on Band
Enter filename (e.g. 'alert01'): CQZoneOnBand
Downloading neural audio for: 'New CQ Zone On Band'...
Success! Saved as: C:\WSJTX Sounds Project\CQZoneOnBand.wav

- Now you can do over all the WSJT-X announcements located in ./bin/sounds to your hearts content

Have fun!
