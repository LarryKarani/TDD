class Phonebook(object):

    def __init__(self):

       self.details = { }

     
    

    def add_contacts (self, name, contacts, email):
        if name in self.details:
            raise ValueError
        
        else:
            instance = {
                "name":name,
                "contacts":contacts,
                "email": email
            }

            self.details[name] = instance

            return instance
             
            
    def update_contacts (self, name, contacts, email):
        if name not in self.details:
            raise ValueError("contact does not exist")


        else:
            instance = {
                "name": name,
                "contacts": contacts,
                "email": email
            }
        self.details[name] = instance
            
        return instance

    def delete_contacts (self, name):
        if name not in self.details:
            raise ValueError("contact does not exist")
        
        else:
           del self.details[name]

        return self.details

    def view_all_contacts(self,):

        return self.details