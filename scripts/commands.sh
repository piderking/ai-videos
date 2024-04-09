
# -----------------------------------------------
# Builder 
mkdir build

# OPTIONAL
# How to Make ontop of each, crop both to the wanted portion and then stack them
ffmpeg -i data/input_soundless.mp4 -vf "crop=w='min(min(iw\,ih)\,1080)':h='min(min(iw\,ih)\,1920)',scale=-1:1920,setsar=1" data/cropped.mp4


# Stack Videos
ffmpeg -i data/cropped.mp4 -i data/cropped.mp4 -filter_complex vstack=inputs=2 data/stacked.mp4
# OPTIONAL

# -----
# Download Videos
python3 scripts/sample_pexel.py
# Loop mp4
ffmpeg -stream_loop -1 -i data/s_input.mp4 -t 60s -c copy data/input.mp4

# Remove Sound from MP4
# ffmpeg -i data/input.mp4 -c copy -an data/input_soundless.mp4
ffmpeg -i data/input.mp4 -vf "scale=-1:1920, crop=1080:1920:656.25:0" -an data/input_soundless.mp4


# Generate TTS (Automated Soon)
py scripts/sample_eleven_labs.py 

# Add TTS to Video
ffmpeg -i data/input_soundless.mp4 -i data/tts.mp3 -t 60s -y data/output.mp4


# rm data/input_soundless.mp4
# rm input.mp4
# rm tts.mp3

# Build SRT Subtitles
vosk-transcriber -i data/output.mp4 -t srt -o build/subs.srt

# Transform into .ass
ffmpeg -i build/subs.srt build/subs.ass

# Add Custom Styles
python3 scripts/custom_style.py

# Add Subtiles
ffmpeg -i data/output.mp4 -vf ass=build/subs.ass build/output.mp4

