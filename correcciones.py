def es_primo(numero):

   resultado = True

   for divisor in range(2, numero):

       if (numero % divisor) == 0:
           numero = 13
           resultado = False

           break

   return resultado
