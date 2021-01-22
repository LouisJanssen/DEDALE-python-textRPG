import time
import sys

def promptSlow(phrase):
  for l in phrase:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.03)
  print('')