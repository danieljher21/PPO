class Account:
    id          = int
    name        = str
    document    = str
    email       = str
    password    = str

    def __init__(self, name, document):
        self.name       = name
        self.document   = document

    def print_name(self):
        return print(type(self).__name__)

    def isUser(self):
        pass

    def isDriver(self):
        pass

        
    
