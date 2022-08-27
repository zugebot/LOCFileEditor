# Jerrin Shirks

import codecs

class StreamDataReader:

    def __init__(self, LittleEndian):
        self.lol = "FORTNITE"
        self.useLittleEndian = LittleEndian
        if LittleEndian:
            self.Endian = "little"
        else:
            self.Endian = "big"
        print(self.Endian)

    @staticmethod
    def correctUTFEncoding(string):
        return codecs.encode(b''.join([ord(s).to_bytes(1, 'big') for s in string]), 'utf-8')

    def getVal(self, byteList):
        return int.from_bytes(b''.join([_bit for _bit in byteList]), self.Endian)

    # static (str, int, Encoding)
    def ReadString(self, stream, length):
        buffer = self.ReadBytes(stream, length)
        string = ""
        for byte in buffer:
            string += chr(int.from_bytes(byte, self.Endian))
        return string # convert buffer to str

    # static byte[] (stream, int)
    def ReadBytes(self, stream, length):
        self.lol = self.lol
        buffer = [None] * length
        stream.read(buffer, 0, length)
        return buffer

    # static byte (stream)
    def ReadByte(self, stream):
        _bytes = self.ReadBytes(stream, 1)
        return self.getVal(_bytes)  # convert bytes to short

    # static short (stream)
    def ReadShort(self, stream):
        _bytes = self.ReadBytes(stream, 2)
        return self.getVal(_bytes)  # convert bytes to short

    # static int (stream)
    def ReadInt(self, stream):
        _bytes = self.ReadBytes(stream, 4)
        # print(type(_bytes), _bytes)
        return self.getVal(_bytes)  # convert bytes to int

    # static long (stream)
    def ReadLong(self, stream):
        _bytes = self.ReadBytes(stream, 8)
        return self.getVal(_bytes)  # convert bytes to long

    # static long (stream)
    def ReadBoolean(self, stream):
        _bytes = self.ReadBytes(stream, 1)
        return 0 != self.getVal(_bytes) # return True or False
