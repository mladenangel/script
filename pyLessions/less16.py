class Print_ob:
    entero = 1000
    texto = 'LaLAla'
    def imp(self,msg):
        print(msg)
    def imp_todo(self,entero,texto,msg):
        print(msg,entero,texto)

x = Print_ob()


print(x.entero)
print(x.imp('HOLA'))
print(x.texto)
print(x.imp_todo('HOLA','ESTO','ES LOCURA'))


