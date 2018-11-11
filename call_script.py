import subprocess
from subprocess import call
#$ py ./youtubeChannelVideosFinder.py 
#-k ...  # the API key `AIzaSyBKNbO-5yPTY_elowvKcjADWVQ_g51sE_I`
#-c martyzsongs # the channel name 
#--date-from 2014-06-15 # last published videos we care about
#--date-to 2014-01-01 # oldest published videos we care about
#--log-file-path awesome.log # generate a log file
#--output-file-path result.txt # put generated links in that file
#-d # debug -> tell everything you're doing

def get_links_proxy(apikey , inception , channel_name ):
    channel_name = channel_name.replace(" ", "")
    subprocess.call(["python.exe","links_finder.py" , "-k" , apikey , "-c" , channel_name , "-x" , '2018-11-9' , "-y" , inception, "-o" , "urls.txt"])


if __name__ == '__main__' :
    get_links_proxy('AIzaSyBKNbO-5yPTY_elowvKcjADWVQ_g51sE_I', '2012-04-11' ,'LinusTechTips')