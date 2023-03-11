import sys

from optparse import OptionParser
from config.config import config_arg 

def args():
    parser = OptionParser()

    parser.add_option('-c', "--config", action="callback", 
                      callback=config_arg, 
                      dest="config",
                      help="Configura driver y apis de forma semi-automatica.")

    (options, args) = parser.parse_args()

    if not args:
        parser.print_usage()
        exit()