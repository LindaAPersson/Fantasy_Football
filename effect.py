import sys
import time


def slow(all_strings):
    """
    Runs all story strings in story.py on slow
    """
    for all_letters in all_strings + "\n":
        sys.stdout.write(all_letters)
        sys.stdout.flush()
        time.sleep(1./30)
