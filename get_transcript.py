import re 
from urllib.parse import urlparse
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import parse_qs
import urllib.request
from bs4 import BeautifulSoup
from call_script import get_links_proxy
from inception import inception_finder


api_key = 'AIzaSyBKNbO-5yPTY_elowvKcjADWVQ_g51sE_I'


channel_info = open('channel_list.txt','r+' , encoding="utf-8")


# Generating links from all the channels 
for channel in channel_info :
    link = channel.split('--')[0].strip()
    name = channel.split('--')[1].strip()
    start = inception_finder(link)
    print("Fetching =>","Channel Link:" ,link , "Channel Name:", name ,"Started On:", start)
    print("Please be patient , this may take several minutes to complete ......")
    get_links_proxy(api_key,start,name)










# A function to get video id out of the video url
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





# Reading youtube video URLs from urls.txt to get transcript of each vid and saving it to youtube_data.txt 
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