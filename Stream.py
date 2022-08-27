# Jerrin Shirks


class Stream:

    def __init__(self, filename="", _type=None):

        self.filename = filename
        self.data = []
        self.index = 0

        if _type == "r":
            with open(self.filename, "rb") as file:
                while bit := file.read(1):
                    self.data.append(bit)

            self.dataLength = len(self.data)
        # elif _type == "w":
        #    1

    # for "r"
    def read(self, buffer, n, length):
        count = 0
        while self.index < self.dataLength:
            if count < length:
                buffer[count] = self.data[self.index]
                self.index += 1
                count += 1
            else:
                break
        return buffer

    # for "w"
    def write(self, buffer, n, length):
        count = 0
        while count < len(buffer) and count < length:
            self.data.append(buffer[count:count+1])
            count += 1
            # print(count)

    # for "w"
    def close(self):

        file = open(self.filename, "wb")

        data = b''.join(self.data)

        file.write(data)

        file.close()

