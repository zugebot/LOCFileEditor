# Jerrin Shirks

from StreamDataWriter import StreamDataWriter
from Encoding import Encoding

def nameof(*args):
    return [name for name in globals() if globals()[name] is args[0]][0]


# https://github.com/PhoenixARC/-PCK-Studio/blob/main/PCK-Studio/Classes/IO/LOC/LOCFileWriter.cs
# https://github.com/PhoenixARC/-PCK-Studio/blob/main/PCK-Studio/Classes/IO/StreamDataWriter.cs

class LOCFileWriter(StreamDataWriter):

    # private LOCFileWriter(LOCFile file) : base(false)
    def __init__(self, _file=None):
        super().__init__(LittleEndian=False)
        self.locFile = _file

    # public static void (Stream, LOCFile, int)
    @staticmethod
    def Write(stream, _file, _type=2):
        LOCFileWriter(_file).WriteToStream(stream, _type)


    # private void (Stream, int)
    def WriteToStream(self, stream, _type):
        if self.locFile is None:
            raise Exception(nameof(self.locFile) + "should not be None.")
        print("Writing Header")
        self.WriteInt(stream, _type)
        self.WriteInt(stream, len(self.locFile.Languages))
        if _type == 2:
            self.WriteLocKeys(stream)
        print("Writing Languages")
        self.WriteLanguages(stream, _type)
        print("Writing Language Entries")
        self.WriteLanguageEntries(stream, _type)
        stream.close()

    # private void (Stream)
    def WriteLocKeys(self, stream):
        # stream.WriteByte(0) # dont use stringIds(ints)
        self.WriteBytes(stream, b'\x01', 1) # dont use stringIds(ints)
        self.WriteInt(stream, len(self.locFile.LocKeys))
        for key in self.locFile.LocKeys.keys():
            self.WriteInt(stream, int(key))

    # private void (Stream, int)
    def WriteLanguages(self, stream, _type):

        for language in self.locFile.Languages:
            self.writeString(stream, language)

            # Calculate the size of the language entry
            size = 0 # int
            size += 4 # sizeof(int) # null long
            size += 1 # sizeof(byte) # null byte
            size += 2 + Encoding.UTF8.GetByteCount(language)  # language name string
            # size += (sizeof(short) + Encoding.UTF8.GetByteCount(language)) # language name string
            size += 4 # sizeof(int) # key count

            for locKey in self.locFile.LocKeys.keys():
                if _type == 0:
                    size += (2 + Encoding.UTF8.GetByteCount(locKey)) # loc key string
                size += (2 + Encoding.UTF8.GetByteCount(self.locFile.LocKeys[locKey][language])) # loc key string

            self.WriteInt(stream, size)

    # private void (Stream, int)
    def WriteLanguageEntries(self, stream, _type):
        for n, language in enumerate(self.locFile.Languages):
            print(n, language)
            self.WriteInt(stream, 1835625333) # :P
            # self.WriteInt(stream, b'\x6D\x69\x6B\x75') # :P
            self.WriteBytes(stream, b'\x00', 1)
            # stream.WriteByte(0) # <- only write when the previous written int was >0

            self.writeString(stream, language)
            self.WriteInt(stream, len(self.locFile.LocKeys.keys()))
            for locKey in self.locFile.LocKeys.keys():
                if _type == 0:
                    self.writeString(stream, locKey)
                self.writeString(stream, self.locFile.LocKeys[locKey][language])

    # private void (Stream, str)
    def writeString(self, stream, s):
        # self.WriteShort(stream, Convert.ToInt16(Encoding.UTF8.GetByteCount(s)));
        # self.WriteShort(stream, Encoding.UTF8.GetByteCount(s))
        self.WriteShort(stream, len(s))
        self.WriteString(stream, s, Encoding.UTF8)
