from account import Account

class Driver(Account):
    def __init__(self, id, name, email, identity_document, password, isDriver):
        super().__init__(id, name, email, identity_document, password)
        self.isDriver = isDriver

        if isDriver == True:
            print(name, email, identity_document, password)
            print( name +  " es: " + type(self).__name__)