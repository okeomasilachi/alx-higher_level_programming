#!/usr/bin/python3

import os

def create_files(num_files):
  for i in range(num_files):
    filename = f"{i}-answer.txt"
    os.open(filename, os.O_CREAT)

if __name__ == "__main__":
  num_files = 29
  create_files(num_files)
