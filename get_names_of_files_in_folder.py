import os
dirListing = os.listdir('search_strings/')
fileNames = []

for item in dirListing:
    fileNames.append(item.split('.')[0])
