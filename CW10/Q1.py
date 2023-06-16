class FILE_READER:

    def __init__(self, file_name, method):
        self.file_name = file_name
        self.method = method
        self.f = None

    def __enter__(self):
        self.f = open(self.file_name,self.method)
        
    def __exit__(self):
        self.f.close()

#with FILE_READER("hello.txt","w") as s:
    #s.write("hey this is a python file")
with FILE_READER("hello.txt","r") as p:
    r = p.read()
    print(r)