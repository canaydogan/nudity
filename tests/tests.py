#!/usr/bin/env python
import imp
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../') ))
from nudity import Nudity

if __name__ == '__main__':
    nudity = Nudity();
    base_path = os.path.dirname(os.path.abspath(__file__))
    none_samples = os.path.abspath(base_path + "/samples/none")
    nude_samples = os.path.abspath(base_path + "/samples/nude")
    for sample in os.listdir(none_samples):
        file_name = os.path.abspath(none_samples + "/" + sample)
        if False != nudity.has(file_name):
            print("Error: " + file_name)
        else:
            print("Success: " + file_name)

    for sample in os.listdir(nude_samples):
        file_name = os.path.abspath(nude_samples + "/" + sample)
        if False == nudity.has(file_name):
            print("Error: " + file_name)
        else:
            print("Success: " + file_name)
