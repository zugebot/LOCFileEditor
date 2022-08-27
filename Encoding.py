# Jerrin Shirks

class Encoding:

    @staticmethod
    def GetBytes(s): # str
        return s.encode('utf-8') # byte list

    class UTF8:

        @staticmethod
        def GetByteCount(s): # str
            return len(s.encode('utf-8')) # int

        @staticmethod
        def GetBytes(s):  # str
            return s.encode('utf-8') # byte list
