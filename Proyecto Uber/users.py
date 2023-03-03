from account import Account


class Users(Account):
    def __init__(self, id, name, email, identity_document, password, isUser):
        super().__init__(id, name, email, identity_document, password)
        self.isUser = isUser

        if isUser == True:
            print(name, email, identity_document, password)
            print("Es usuario")
            
        
