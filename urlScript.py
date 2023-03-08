# Native imports
import sys

# Custom imports
from lib.screen_saver import get_screeshots

# lib
from lib.report_system import report_creator

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
    if len(sys.argv) < 2:
        print(f"Usage: \npython {sys.argv[0]} TARGET")
        print(f"Example: python {sys.argv[0]} google.com")
        sys.exit(1)

    target = sys.argv[1]
    report_creator(target)
    get_screeshots(target)