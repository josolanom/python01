class Humano:
    def __init__(self, edad):
        self.edad = edad   # atributo
        
    
    def hablar (self, mensaje): #Metodo
        print (mensaje)

v_pedro = Humano(25)
v_raul = Humano(45)

v_pedro.hablar('Hola')

print ('Soy Raul y tengo ',v_pedro.edad)