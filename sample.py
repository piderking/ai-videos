import whisper
from whisper.utils import get_writer 

audio = './data/0/tts.mp3'
model = whisper.load_model('base')
result = model.transcribe(audio=audio, language='en', word_timestamps=True, task="transcribe")

# Set VTT Line and words width
word_options = {
    "highlight_words": False,
    "max_line_count": 1,
    "max_line_width": 42
}
vtt_writer = get_writer(output_format='srt', output_dir='./data/0/')
vtt_writer(result, audio, word_options)