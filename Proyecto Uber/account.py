class Account():
    id = int
    name = str
    email = str
    identity_document = int
    password = str
    
    def __init__(self, id, name, email, identity_document, password):
        self.id = id
        self.name = name
        self.email = email
        self.identity_document = identity_document
        self.password = password

        return (id, name, email, identity_document, password)

        
    
    
