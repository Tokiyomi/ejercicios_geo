# Cifrado Caesar
import sys 

def main():
    args = sys.argv[1:]

    if len(args) == 1:

        #Se asume que si hay 1 argumento, es numerico y se asigna a la variable k
        k=int(args[0])

        # Input text
        text = input('plaintext: ')

        cipher_text = ''

        for char in text:

            # Crear formula considerando los caracteres alfabeticos del inglés, el cual tiene 26 letras y sensitivo a mayusculas y minusculas

            if char.isupper():
                
                # Para letras mayusculas, el código ASCII en inglés tiene un rango de [65,90]
                cipher_text += chr((ord(char) -65 + k) % 26 + 65) # convertir caracter a su valor numerico, luego aplicar transformacion, luego convertirlo a caracter de nuevo

            elif char.islower():
                # Para letras minusculas, el código ASCII en inglés tiene un rango de [97,122]
                cipher_text +=  chr((ord(char) -97 + k) % 26 + 97) # convertir caracter a su valor numerico, luego aplicar transformacion, luego convertirlo a caracter de nuevo
            
            else:
                # Si son caracteres especiales, no hacer ningun cambio
                cipher_text += char
            
        # Imprimir nueva cadena con el cifrado
        print('ciphertext:',cipher_text,'\n')
        #print()

    else: 
        # Si el programa tiene mas de 1 argumento o no tiene, imprimir su uso y retornar codigo de error 1
        print('Usage: python caesar.py k')
        return 1
    
if __name__ == '__main__':
    main()