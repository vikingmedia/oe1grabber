#!/usr/bin/python
# encoding: utf-8
'''
Created on May 7, 2017

@author: zking

'''

import datetime
import time
import json
import urllib2
import re
import dateutil.parser
import os
from argparse import ArgumentParser
import subprocess
import logging

   

        

def cleanhtml(raw_html):
    if raw_html == None: return ''
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext    
    

    

if __name__ == '__main__':
    
    parser = ArgumentParser()
    parser.add_argument("-t", "--target", default=os.path.dirname(os.path.realpath(__file__)), help="target directory")
    parser.add_argument("-d", "--date", default=datetime.datetime.now().date().strftime('%Y%m%d'), help="date to grab (format: YYYYMMDD) or today or yesterday")
    parser.add_argument("-a", "--all", action='store_true', default=None, help="grab all available dates")

    
    # Process arguments
    args = parser.parse_args()

    replace_characters = re.compile('\?')
    
    current_time = time.time()
    url = 'https://audioapi.orf.at/oe1/api/json/current/broadcasts?_s=%i' % (current_time * 1000, )
    
    logging.info('downloading 7Tage OE1 info from %s', url)
    
    response = urllib2.urlopen(url)
    days = json.loads(response.read())
    
    for day in days:
        
        year = str(day['day'])[:4]
        
        if not args.all and args.date != str(day['day']):
            continue
               
        for broadcast_teaser in day['broadcasts']:
            
            ffmpeg_processes = []
            
            response = urllib2.urlopen(broadcast_teaser['href'])
            broadcast = json.loads(response.read())
            
            start = dateutil.parser.parse(broadcast['niceTimeISO'])
            title = ' '.join((start.strftime('%Y%m%d %H%M%S'), '-', broadcast['title'].replace('/', '-'))).encode('utf-8', 'ignore')
            subtitle = cleanhtml(broadcast['subtitle'])
            description = cleanhtml(broadcast['description'])
            
            local_dir = os.path.join(args.target, str(day['day']))
            
            if not os.path.isdir(local_dir): 
                os.mkdir(local_dir)
                
            of = os.path.join(local_dir, replace_characters.sub('', title) + '.mp3')

            if os.path.exists(of): continue
    
            cli = [
                 '/usr/bin/ffmpeg',
                 '-i', 'http://loopstream01.apa.at/?channel=oe1&shoutcast=0&id=%s&offset=0' % (broadcast['streams'][0]['loopStreamId'],),
                 '-metadata', 'title='+title+'',
                 '-metadata', 'album=7 Tage OE1',
                 '-metadata', 'year='+year+'',
                 '-metadata', 'comment='+description.encode('utf8')+'',
                 '-acodec','copy',
                 '-f', 'mp3',
                 of
            ]
            
            ffmpeg_processes.append({of: subprocess.Popen(cli)})
        
            
        while True:
            proc_status = [p.values()[0].poll() for p in ffmpeg_processes]
                
            if all([x is not None for x in proc_status]): break
            time.sleep(1)
            
        for p in ffmpeg_processes:
            print p.values()[0], ': ', p.keys()[0] 
            
            
             
