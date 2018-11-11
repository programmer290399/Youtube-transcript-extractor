import re 
from urllib.parse import urlparse
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import parse_qs
import urllib.request
from bs4 import BeautifulSoup
from call_script import get_links_proxy
from inception import inception_finder






def video_id_extractor(value):

    query = urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    
    return None






fh = open('youtube_data.txt','w+', encoding='utf-8')
with open('urls.txt', 'r', encoding="utf-8") as f:
    for url in f:
        
    
            video_id = video_id_extractor(url)
            print('Retriving :', video_id)
            if video_id is not None :
                try :
                    transcript_dirty  = YouTubeTranscriptApi.get_transcript(video_id)

                    transcript_clean = str()

                    for parts in transcript_dirty :
                        transcript_clean += (" " + parts['text'])
                    print('writing to file ...')
                    fh.write(transcript_clean + '\n')
                except :
                    print('Error on :', url )