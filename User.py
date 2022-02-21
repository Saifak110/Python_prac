class User:
    fullname = None
    regno = None
    def setname(self, firstname, lastname):
        self.fullname = firstname+" "+lastname
    
    def getname(self):
        return self.fullname


    def setregno(self, regno):
        self.regno = regno
    
    def getregno(self):
        return self.regno
