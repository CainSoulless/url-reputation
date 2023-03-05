# Native imports
import sys

# Custom imports
from lib.browser_executor import webpages_open

if len(sys.argv) < 2:
    print(f"Usage: \npython {sys.argv[0]} TARGET")
    print(f"Example: python {sys.argv[0]} google.com")
    exit(1)

target = sys.argv[1]
webpages_open(target)