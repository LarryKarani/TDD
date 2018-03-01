import unittest
from app import Phonebook

class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.contacts = Phonebook()

        #test for the add class method

    def test_add_contacts(self):
        value = self.contacts.add_contacts('larry',123, 'r@gmail.com')

        results= value["name"] in self.contacts.details


        self.assertEqual(results, True )

        #test if it raises an exeption when contact exist


    def test_update_contacts(self):
        #add a contact
        self.contacts.add_contacts("sophi", 456, 'y@gmail')
       
        #update a contact
        self.contacts.update_contacts("sophi", 678, 's@gmail' )
        
        self.assertEqual(self.contacts.details['sophi'], {"name":"sophi", "contacts":678, "email":"s@gmail"})


    def test_delete_contact(self):
         self.contacts.add_contacts("james", 456, 'tyy')
        
         results = self.contacts.delete_contacts("james")


        

         self.assertEqual(results, {})

    def test_view_all_contact(self):
        self.contacts.add_contacts("jame", 456, 'y@gmail')
        self.contacts.add_contacts("sophi", 456, 'y@gmail')
        self.contacts.add_contacts("luli", 456, 'y@gmail')
        self.contacts.add_contacts("lucy", 456, 'y@gmail')
        results = self.contacts.view_all_contacts()

        self.assertEqual(results, {'jame': {'contacts': 456, 'email': 'y@gmail', 'name': 'jame'},
 'lucy': {'contacts': 456, 'email': 'y@gmail', 'name': 'lucy'},
 'luli': {'contacts': 456, 'email': 'y@gmail', 'name': 'luli'},
 'sophi': {'contacts': 456, 'email': 'y@gmail', 'name': 'sophi'}})




if __name__ == '__main__':
    unittest.main()
