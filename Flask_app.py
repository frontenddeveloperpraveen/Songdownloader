from flask import Flask, render_template, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi
import scrapetube
import pytube
from moviepy.editor import *
import os

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def Home():
    return render_template('base.html')

@app.route('/songs', methods=['GET'])
def Gen():
    name = request.args.get('song')
    file = name.replace(' ', '+') + 'Official+song'
    videos = scrapetube.get_search(file)
    for video in videos:
        link = video['videoId']
        break
    video_url = f'https://www.youtube.com/watch?v={link}'
    yt = pytube.YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_filename = audio_stream.default_filename

    # Define the output filename with the "static" folder path
    output_filename = os.path.join("static", f'{audio_filename.replace(".mp4", ".mp3")}')

    # Download the audio stream and save it to the "static" folder
    audio_stream.download(output_path="static", filename=audio_filename)

    print("Audio saved")
    return render_template('Home.html', filename=f'static/{audio_filename}', linkk=link)

@app.route('/lyrics', methods=['POST'])
def Lyrics():
    data = request.json
    lyrics = data.get('lyrics')
    print(lyrics)
    print('Received connection')
    srt = YouTubeTranscriptApi.get_transcript(lyrics, languages=['en-US','en','auto'])
    # Replace "video_id_here" with the actual video ID
    print(srt)
    return jsonify({'msg': srt})

if __name__ == '__main__':
    app.run(debug=True)
