peso = eval(input('Cual es su peso? (kilos): '))
altura = eval(input('Cual es su altura? (metros): '))
imc = round(peso / pow(altura,2),2)
print('Tu índice de masa corportal es: ' + str(imc))