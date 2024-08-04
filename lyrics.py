from youtube_transcript_api import YouTubeTranscriptApi
srt = YouTubeTranscriptApi.get_transcript("Qc7_zRjH808")
import time
start_time = 0
for index, lyric in enumerate(srt):
    text = lyric['text']
    start = lyric['start']
    # print('Start [given]  : ',start)
    if index == 0:
        print(' \n [Program] : Recognition Completed - Sync set to Automatic \n ')
    start_time = start - start_time
    # print('Sleep time',start_time)
    time.sleep(start_time)
    if text == '[Music]':
        text = 'Music....'
    elif text == '[Applause]':
        text = 'Clapping sound....'
    print(text.replace('♪',''))
    start_time = start











































































































































































#End of code -----














