import sys
import time


def slow(all_strings):
    """
    Runs all story strings so it looks like they are printed in real time. 
    """
    for all_letters in all_strings + "\n":
        sys.stdout.write(all_letters)
        sys.stdout.flush()
        time.sleep(1./30)
