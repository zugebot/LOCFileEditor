# Jerrin Shirks

import codecs


def nameof(*args):
    return [name for name in globals() if globals()[name] is args[0]][0]



# internal
class StreamDataWriter:

    # protected (bool)
    def __init__(self, LittleEndian):
        self.useLittleEndian = LittleEndian
        if self.useLittleEndian:
            self.Endian = "little"
        else:
            self.Endian = "big"

    @staticmethod
    def correctUTFEncoding(string):
        return codecs.decode(b''.join([ord(s).to_bytes(1, 'big') for s in string]), 'utf-8')

    def getVal(self, value, byteSize):
        _bytes = value.to_bytes(byteSize, self.Endian)
        #_bytes = [i.to_bytes(1, self.Endian) for i in _bytes]
        # print(_bytes)
        # print([i.to_bytes(1, self.Endian) for i in _bytes])
        # input()
        return _bytes

    # protected static void (Stream, byte[], int)
    def WriteBytes(self, stream, _bytes, count):
        # if not self.useLittleEndian:
        #    _bytes = _bytes[::-1]
        stream.write(_bytes, 0, count)

    # protected static void (Stream, short)
    def WriteShort(self, stream, value):
        _bytes = self.getVal(value, 2) # byte[]
        self.WriteBytes(stream, _bytes, 2)

    # protected static void (stream, int)
    def WriteInt(self, stream, value):
        _bytes = self.getVal(value, 4)  # byte[]
        self.WriteBytes(stream, _bytes, 4)

    # protected static void (Stream, long)
    def WriteLong(self, stream, value):
        _bytes = self.getVal(value, 8)  # byte[]
        self.WriteBytes(stream, _bytes, 8)

    # protected static void (Stream, str, Encoding)
    def WriteString(self, stream, s, encoding):

        # print(type(s))
        stringBytes = encoding.GetBytes(self.correctUTFEncoding(s))
        self.WriteBytes(stream, stringBytes, len(stringBytes))
        # self.WriteBytes(stream, encoding.GetBytes(s), len(encoding.GetBytes(s)))


