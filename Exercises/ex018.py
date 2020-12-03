#Faca um program que leia um angulo qualquer e mostre na tela o valor do
#seno, cosseno e tangente desse angulo.
import math
ângulo = float(input('Digite um angulo qualquer: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('O angulo de {} tem o SENO de {:.2f}.'.format(ângulo, seno))
print('O angulo de {} tem o COSSENO de {:.2f}.'.format(ângulo, cosseno))
print('O angulod e {} tem a TANGENTE de {:.2f}.'.format(ângulo, tangente))
