# Jerrin Shirks

from LOCFile import LOCFile
from StreamDataReader import StreamDataReader
# import io


def nameof(*args):
    return [name for name in globals() if globals()[name] is args[0]][0]



class LOCFileReader(StreamDataReader):

    class InvalidLanguageException(Exception):
        pass

    # private LOCFileReader() : base(false)
    def __init__(self):
        super().__init__(LittleEndian=False)
        self.locFile = LOCFile() # internal
        # self.writeFile = io.open("loc.text", "w", encoding='utf-16-le') # FILE NONSENSE

    # public static LOCFile (Stream)
    def Read(self, stream):
        return self.ReadFromStream(stream)

    # private LOCFile (stream)
    def ReadFromStream(self, stream):
        loc_type = self.ReadInt(stream)
        # input(loc_type)
        language_count = self.ReadInt(stream)
        print("language count:", language_count)
        lookUpKey = (loc_type == 2) # bool

        if lookUpKey:
            keys = self.ReadKeys(stream) # List<string>
        else:
            keys = None

        for i in range(language_count):
            language = self.readString(stream)
            self.ReadInt(stream)
            self.locFile.Languages.append(language)

        for i in range(language_count):

            if 0 < self.ReadInt(stream):
                self.ReadByte(stream)

            language = self.readString(stream) # str
            if language not in self.locFile.Languages:
                raise Exception(nameof(language) + f": {language} key not found.")

            count = self.ReadInt(stream) # int

            for j in range(count):
                if lookUpKey:
                    key = keys[j] # str
                else:
                    key = self.readString(stream)
                value = self.readString(stream)

                # string = f"{language} {value}\n"
                # self.writeFile.write(self.correctUTFEncoding(string)) # FILE NONSENSE
                # print(key, language, value)
                self.locFile.SetLocEntry(key, language, value)

        # self.writeFile.close()
        return self.locFile

    # private List<string> (Stream)
    def ReadKeys(self, stream):
        useUniqueIds = self.ReadBoolean(stream) # bool
        keyCount = self.ReadInt(stream) # int
        keys = [None] * keyCount # List<string>

        for i in range(keyCount):
            if useUniqueIds:
                key = str(self.ReadInt(stream)).rjust(8, "0")
            else:
                key = self.readString(stream)
            keys[i] = key
        return keys

    # private string (Stream)
    def readString(self, stream):
        length = self.ReadShort(stream) # int
        return self.ReadString(stream, length)
