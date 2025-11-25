# How to make your own WSJT-X announcements - No microphone needed!
## While there is nothing wrong with the spoken audio that you can enable in WSJT-X to announce things like CQ heard or New DXCC on the band, maybe you'd like to have your own custom announcement! And with a really natural sounding Microsoft Edge TTS 'Sonia' British voice. Well now you can! -

### First: Make sure you  have Python 3.x.x installed! If you don't, go figure out how to install it.

### Then create a directory to do all your fancy voice creation work. 
- Any directory will do since all of the files will live there, together...in peace and harmony : )

### Download the needed Files
- Go to [Gyan.dev FFmpeg builds](https://www.gyan.dev/ffmpeg/builds/) Download the file labeled `ffmpeg-git-essentials.7z` (or .zip). Unzip to some temp
folder and in the ./bin directory, look for the files: ffmpeg.exe, ffplay.exe & ffprobe.exe. Copy just those three files into the directory you created 
in the first step.

- Next, from MY repository (the one you're in now), download the Python script `Announce_wav.py` and put it into the same directory.

- Before you run it, install the required Python modules, `pip install pydub` and Microsoft Edge Text-to-Speech `pip install edge-tts`

## So how do you use it? Simple!

- In a CMD window, go to the directory you created and saved the files into.
- Run the script `python Announce_wav.py`
- Here's how it goes:

--- Edge-TTS Neural Announcer (Voice: en-GB-SoniaNeural) ---
Output Format: WAV (48kHz, 16-bit, Mono, 768kbps)
Type 'exit' to quit.

========================================
- Enter the announcement text: New CQ Zone on Band <- Put in any text you want
- Enter filename (e.g. 'alert01'): CQZoneOnBand
- Downloading neural audio for: 'New CQ Zone On Band'...
- Success! Saved as: C:\WSJTX Sounds Project\CQZoneOnBand.wav

It will save to whatever directory you're working in. Then just copy the files to C:\WSJT-X\bin\sounds

## Now you can do over all the WSJT-X announcements to your hearts content

## Have fun!


