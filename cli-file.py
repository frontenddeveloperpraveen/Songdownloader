import scrapetube
import pytube
import ffmpeg

file = input('Enter search: ').replace(' ', '+')
videos = scrapetube.get_search(file)

for video in videos:
    link = video['videoId']
    break

video_url = f'https://music.youtube.com/watch?v=rVqcPUQ2YXI'
yt = pytube.YouTube(video_url)

audio_stream = yt.streams.filter(only_audio=True).first()
audio_filename = audio_stream.default_filename

# Download the audio file
audio_stream.download()
aud = audio_filename.replace('.mp4','')

# Convert the downloaded video file to an audio file
ffmpeg.input(filename=audio_filename).output(f'{aud}.mp3', acodec='libmp3lame').run()

print("Audio saved")
