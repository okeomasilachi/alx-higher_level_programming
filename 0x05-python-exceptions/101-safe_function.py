#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ok = fct(*args)
        return ok
    except Exception as a:
        sys.stderr.write(f"Exception: {a}\n")
        return None
