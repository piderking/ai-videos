


vosk-transcriber -i data/{}.mp4 -t srt -o subs.srt

ffmpeg -i sample_video_ffmpeg.mp4 -vf subtitles=sample_video_subtitle_ffmpeg.srt output_srt.mp4

ffmpeg -i data/input.mp4 -vf subtitles=build/subs.srtsub.srt:force_style='Fontname=DejaVu Serif,PrimaryColour=&HCCFF0000' output_srt.mp4


# Build ASS Subtitles
vosk-transcriber -i data/input.mp4 -t srt -o build/subs.srt

ffmpeg -i build/subs.srt build/subs.ass

ffmpeg -i data/input.mp4 -vf ass=build/subs.ass build/output.mp4
