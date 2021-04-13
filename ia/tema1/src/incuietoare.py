class Incuietoare:
    def __init__(self,nr_incuieri):
        self.nr_incuieri = nr_incuieri
    
    def __repr__(self):
        status = ''
        if self.nr_incuieri > 0:
            status = "i"
        else:
            status = "d"
        return "inc({0},{1})".format(status,self.nr_incuieri)
    
    def __eq__(self, other):
        return self.nr_incuieri == other.nr_incuieri
    def update(self, valoare):
        self.nr_incuieri += valoare
    
    def get(self):
        return self.nr_incuieri