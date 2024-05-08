#!/usr/bin/python3
#import os

#if __name__ == "__main__":
#    for (root,dirs,files) in os.walk('.', topdown=True):
#        print(root)
#        print(dirs)
#        print(files)
#        print('-----------------------------------------')

#import time

#def recursive_function(iteration):
#    iteration += 1
#    print(iteration)
#    time.sleep(1)
#    recursive_function(iteration)

#recursive_function(0)

import os

for root, dirs, files in os.walk(".", topdown=False):
    for file in files:
        print(os.path.join(root, file))
    for dir in dirs:
        print(os.path.join(root, dir))