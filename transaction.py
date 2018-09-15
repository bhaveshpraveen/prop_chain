class Transaction(object):
    def __init__(self, property_from, property_to, prop):
        self.property_from = property_from 
        self.property_to = property_to
        self.property_ = prop
    
    def __str__(self):
        return "{}{}{}".format(
            self.property_from,
            self.property_to,
            self.property_
        )