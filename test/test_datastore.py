import sys

sys.path.append('..')

import unittest
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


from noodles import datastore as ds


##########################################################
###############      Test models here     ################
##########################################################

class Date(ds.Model):
    month = ds.Value(int)
    day = ds.Value(int)
    year = ds.Value(int)
    
class Deposit(ds.Model):
    amount = ds.Value(float)
    cdate = ds.Node(Date)

class User(ds.Model):
    name = ds.Value(str)
    email = ds.Value(str)
    age = ds.Value(int)
    deposit = ds.Node(Deposit)

class Game(ds.Model):
    appid = ds.Value(int)
    name = ds.Value(str)
    
class DataStoreTest(unittest.TestCase):
    def test_structure(self):
        user = User()
        print 'Structure:', user.get_structure()
        user2 = User()
        print "Collection name: ", user2.get_collection_name()
        self.assertEqual(user2.name, None)
        user.name = 'Niko'
        self.assertEqual(user.name, 'Niko')
        user2.name = 'Mike'
        self.assertEqual(user2.name, 'Mike')
        self.assertEqual(user2.get_collection_name(), 'users')
        
    def test_node(self):
        user = User()
        user.deposit.amount = 100
        self.assertEqual(user.deposit.amount, 100)
        
        user.deposit.amount += 100        
        self.assertEqual(user.deposit.amount, 200)
        
        user2 = User()
        user2.deposit.amount = 50
        self.assertEqual(user2.deposit.amount, 50)
        self.assertEqual(user.deposit.amount, 200)
        
        user2.deposit.amount = 50
        
        # Test full creation of the new User model with kwargs
        niko = User(name="Niko", 
                email="nskrypnik@gmail.com", 
                age=24, 
                deposit=Deposit(amount=100, 
                                cdate = Date(year=2011, month=5, day=12)))
        print niko.__instdict__
        
        guy = User(name="Guy", 
                email="guyromm@gmail.com", 
                age=28, 
                deposit=Deposit(amount=200, 
                                cdate = Date(year=2011, month=6, day=22)))
        
        self.assertEqual(guy.deposit.cdate.year, 2011)
        self.assertEqual(guy.deposit.cdate.month, 6)
        self.assertEqual(guy.deposit.cdate.day, 22)
        
        self.assertEqual(niko.deposit.cdate.year, 2011)
        self.assertEqual(niko.deposit.cdate.month, 5)
        self.assertEqual(niko.deposit.cdate.day, 12)
              

    def test_typing(self):
       user = User()
       user.name = 10
       self.assertEqual(user.name, '10')
    
    
if __name__ == '__main__':
    unittest.main()
