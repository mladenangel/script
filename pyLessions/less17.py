# My firs class

class Profiles:
    
    def __init__(self,profil):
        self.profil = profil
    def nombre(self,name):
        print(name)
    def tu_email(self,email):
        print(email)
    def tu_passwd(self,passwd):
        print(passwd)
 
        
a=[]
b=[]    
employe1 = Profiles()
employe2 = Profiles()
a.append(employe1.nombre('Pedro'))
a.append(employe1.tu_email('pedro@pedro.com'))
a.append(employe1.tu_passwd('123456'))
print(a)

b.append(employe2.nombre('Delwin'))
b.append(employe2.tu_email('delwin@delwin.com'))
b.append(employe2.tu_passwd('123456'))
print(b)
employe3 = Profiles()
name = employe3.nombre('Ivan')
email = employe3.tu_email('ivan@ivan.com')
passwd = employe3.tu_passwd('pass')

c = dict(name=str(name),email=str(email),passwd=str(passwd))
print(c)




 
