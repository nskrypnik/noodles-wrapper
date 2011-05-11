import sys

sys.path.append('..')

import unittest
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


from noodles import datastore as ds


##########################################################
###############      Test models here     ################
##########################################################

class User(ds.Model):
    name = ds.Value()
    email = ds.Value()


class DataStoreTest(unittest.TestCase):
    def test_structure(self):
        user = User()
        print user.__structure__
        user2 = User()
        print user2.__structure__
        self.assertEqual(user2.name, None)
        user.name = 'Niko'
        self.assertEqual(user.name, 'Niko')
        user2.name = 'Mike'
        self.assertEqual(user2.name, 'Mike')
    
    
if __name__ == '__main__':
    unittest.main()
