import pickle


class FileManager :
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        f = open(self.filename, "wb")       # 파일 쓴다.
        pickle.dump(data, f)                # 값 넣는다.
        f.close()                           # 닫는다.

    def load(self):
        try:
            f = open(self.filename, "rb")       # 파일 읽어온다.
            data = pickle.load(f)               # data 에 값을 넣는다.
            f.close()                           # 닫는다.
        except FileNotFoundError:
            raise FileNotFoundError

        return data                         # 리턴한다.