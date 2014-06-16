#!/usr/bin/python
# encoding: utf-8
'''
zeitgrabber -- shortdesc

zeitgrabber is a description

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
import BeautifulSoup
import dateutil.parser

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

#########################################################################################################
# CONSTANTS
#########################################################################################################

__all__ = []
__version__ = 0.1
__date__ = '2014-01-06'
__updated__ = '2014-01-06'


DEBUG = 0
TESTRUN = 0
PROFILE = 0

ZEIT_FEED_URL = 'https://premium.zeit.de/itunes/feed'
USERNAME = 'efellows1'
PASSWORD = 'efellows'


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
        parser.add_argument("-a", "--all", action='store_true', default=None, help="grab all available dates")
        parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
        parser.add_argument('-V', '--version', action='version', version=program_version_message)
        
        # Process arguments
        args = parser.parse_args()
        verbose = args.verbose

        if verbose > 0:
            print("Verbose mode on")
            
        # set up password manager
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        top_level_url = "https://premium.zeit.de"
        password_mgr.add_password(None, top_level_url, USERNAME, PASSWORD)
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        
        #download itunes feed
        if verbose: print 'Getting feed from %s' % (ZEIT_FEED_URL, )
        soup = BeautifulSoup.BeautifulStoneSoup(urllib2.urlopen(ZEIT_FEED_URL).read())
        
        # iterate through item
        for item in soup.findAll('item'):
            clean_title = "".join([c if c.isalnum() else '_' for c in item.title.text]).rstrip()
            timestamp = dateutil.parser.parse(item.pubdate.text)
            file_name = timestamp.strftime('%Y%m%d_%H%M') + '_' + clean_title + '.mp3'
            if verbose: print file_name
            
            target_path = os.path.join(args.target, timestamp.strftime('%Y%m%d'))
            if not os.path.isdir(target_path): os.mkdir(target_path) 
            
            file_path = os.path.join(target_path, file_name)
            if verbose: print '%s --> %s' % (item.enclosure['url'], file_path)
            
            with open(file_path, 'wb') as f:
                f.write(opener.open(item.enclosure['url']).read())
        
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