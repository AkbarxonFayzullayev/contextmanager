class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self,name,nnn,mmm):
        if self.file:
            self.file.close()
        return False

with FileManager("example.txt", "w") as f:
    f.write("Hello, World!")
