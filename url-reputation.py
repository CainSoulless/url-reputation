# Native imports
import sys

# lib
from lib.screen_saver import get_screeshots
from lib.report_system import report_creator

# Utils
from lib.utils import open_folder 

# Config
from config.config import config_checker

# Args
from utils.args import args


# TODO: Configuration arg with argparse
"""
Example:
    -c or --config to install the geckoDrickoDriver
"""
# TODO: hashes files option
"""
Example:
    -ho --hashoption with parseargs
""" 

if __name__ == "__main__":
    target = sys.argv[1]

    config_checker()

    args()
    report_creator(target)
    get_screeshots(target)