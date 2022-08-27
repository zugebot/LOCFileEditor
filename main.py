# Jerrin Shirks

from Stream import Stream
from LOCFileReader import LOCFileReader
from LOCFileWriter import LOCFileWriter

import random

# E:\New folder\Emulator Folders\cemu_1.25.6\mlc01\usr\title\0005000e\101d9d00\content\Common\Media

if __name__ == "__main__":

    # opens a loc file and creates the locFile object
    readStream = Stream("languages.loc", "r")
    readLoc = LOCFileReader()
    readLoc.Read(readStream)

    # an example where the code randomizes all english values between keys.
    print("randomizing text...")
    englishItems = [None] * len(readLoc.locFile.LocKeys)
    for n, i in enumerate(readLoc.locFile.LocKeys):
        englishItems[n] = readLoc.locFile.LocKeys[i]["en-EN"]

    random.shuffle(englishItems)
    for n, i in enumerate(readLoc.locFile.LocKeys.keys()):
        readLoc.locFile.LocKeys[i]["en-EN"] = englishItems[n]


    # writes the locFile object back into an output file.
    writeStream = Stream("languages_output.loc", "w")
    writeLoc = LOCFileWriter()
    writeLoc.Write(writeStream, readLoc.locFile, 2)





