#!/usr/bin/python
# encoding: utf-8
'''
oe1grabber -- shortdesc

oe1grabber is a description

It defines classes_and_methods

@author:     user_name
        
@copyright:  2014 organization_name. All rights reserved.
        
@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os
import urllib2
import json
import subprocess
import time
import re
from datetime import date
from datetime import timedelta

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter


__all__ = []
__version__ = 0.1
__date__ = '2014-01-06'
__updated__ = '2014-01-06'


DEBUG = 0
TESTRUN = 0
PROFILE = 0


OE1_MEDIATHEK_BASE_URL = 'http://oe1.orf.at/programm/konsole/tag/'



def grab(date, target, verbose=True):
    while 1:
        try: 
            if verbose: print OE1_MEDIATHEK_BASE_URL + date
            j = json.loads(urllib2.urlopen(OE1_MEDIATHEK_BASE_URL + date).read())
            break
            
        except: 
            print 'error downloading list, waiting for 10s ...'
            time.sleep(10)
            
    repl = re.compile('\?') #replace that characters in the file name
    
    try:
        proc = []
        for p in j['list']:
            d, m, y = [i.rjust(2, '0') for i in p['day_label'].split('.')]
            title = (y+m+d + ' ' + p['time'].replace(':', '') + ' - ' + p['title']).replace('/','-').encode('utf-8', 'ignore')
    
            local_dir = os.path.join(target, date)
            if verbose: print local_dir
            if not os.path.isdir(local_dir): os.mkdir(local_dir)
            path = os.path.join(local_dir, repl.sub('', title)+'.mp3')
            if verbose: print path
            
            if os.path.exists(path): continue
    
            cli = [
                 '/usr/bin/ffmpeg',
                 '-metadata', 'title='+title+'',
                 '-metadata', 'album=7 Tage OE1',
                 '-metadata', 'year='+p['day_label'][-4:]+'',
                 '-metadata', 'comment='+p['info'].encode('utf8')+'',
                 '-i', p['url_stream'] + '&ua=flash&shoutcast=0',
                 '-acodec','copy',
                 '-f', 'mp3',
                 path
            ]
    
            proc.append({path: subprocess.Popen(cli)})
            
        while True:
            proc_status = [p.values()[0].poll() for p in proc]
                
            if all([x is not None for x in proc_status]): break
            time.sleep(1)
            
        for p in proc:
            print p.values()[0], ': ', p.keys()[0] 

          
    finally:
        for p in proc:
            if p.values()[0] == None:
                print 'terminating "%s"' % (p.values()[0], )
                p.values()[0].terminate()            


def main(argv=None): 
    '''Command line options.'''
    
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by user_name on %s.
  Copyright 2014 organization_name. All rights reserved.
  
  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0
  
  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-t", "--target", default=os.path.dirname(os.path.realpath(__file__)), help="target directory")
        parser.add_argument("-d", "--date", default=None, help="date to grab (format: YYYYMMDD)")
        parser.add_argument("-a", "--all", action='store_true', default=None, help="grab all available dates")
        parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
        parser.add_argument('-V', '--version', action='version', version=program_version_message)
        
        # Process arguments
        args = parser.parse_args()
        verbose = args.verbose

        if verbose > 0:
            print("Verbose mode on")
        
        today = date.today()
        dt = timedelta(days=1)
        dates = [today.strftime('%Y%m%d')]
        
        if args.all: dates.extend([d.strftime('%Y%m%d') for d in [today-dt*i for i in range(1, 7)]])
        elif args.date: dates = [args.date]
        
        for d in dates:
            grab(date=d, target=args.target, verbose=verbose)
        
        return 0
    
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    
    except Exception, e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2


if __name__ == "__main__":
    
    if DEBUG:
        sys.argv.append("-h")
        sys.argv.append("-v")
        sys.argv.append("-r")
    
    if TESTRUN:
        import doctest
        doctest.testmod()
    
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'oe1grabber_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    
    sys.exit(main())