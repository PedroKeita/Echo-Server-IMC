# server.py
import socket
import json

# create a socket object
print('ECHO SERVER para cálculo do IMC')
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get a local machine name
host = '127.0.0.1'
port = 9999

# bind to the port
serverSocket.bind((host, port))

#start listening requests
serverSocket.listen()
print('Serviço rodando na porta {}.'.format(port))

while True:
    # establish a connection
    clientSocket, addr = serverSocket.accept()
    print('Conectado a {}'.format(str(addr)))

    # recive client data
    received = clientSocket.recv(1024).decode()

    print('Os dados recebidos do cliente são: {}'.format(received))

    # server processing
    received = json.loads(received)

    # IMC (Indice de Massa Corporal)
    def generate_imc(my_dict):
        h = my_dict['altura']
        p = my_dict['peso']
        return round(float(p / (h * h)), 2)

    # adding the imc to data sent by the user
    received['imc'] = generate_imc(received)

    # Status IMC
    def analyse_imc(imc):
        if 0 < imc < 18.5:
            status = "Abaixo do Peso!"
        elif imc <= 24.9:
            status = "Peso normal!"
        elif imc <= 29.9:
            status = "Sobrepeso!"
        elif imc <= 34.9:
            status = "Obesidade Grau 1!"
        elif imc <= 39.9:
            status = "Obesidade Grau 2!"
        elif imc <= 40.0:
            status = "Obesidade Grau 1!"
        else:
            status = "Valores inválidos"
        return status

    # adding the status of the imc to data sent by the user
    received['statusImc'] = analyse_imc(received['imc'])

    # TMB (Taxa Metabólica Basal)
    def generate_tmb(my_dict):
        sex = my_dict['sexo']

        if sex in 'Mm':
            tmb = 5 + (10 * my_dict['peso']) + (6.25 * (my_dict['altura'] * 100)) - (5 * my_dict['idade'])

        else:
            tmb = (10 * my_dict['peso']) + (6.25 * (my_dict['altura'] * 100)) - (5 * my_dict['idade']) - 5

        return tmb

    # adding the tmb to data sent by the user
    received['tmb'] = generate_tmb(received)

    def generate_cal(my_dict):
        if my_dict['nvlAtiv'] == 1:
            fator_ativ = 1.2

        elif my_dict['nvlAtiv'] == 2:
            fator_ativ = 1.375

        elif my_dict['nvlAtiv'] == 3:
            fator_ativ = 1.725

        else:
            fator_ativ = 1.9

        return round((my_dict['tmb'] * fator_ativ), 2)

    # adding the cal to data sent by the user
    received['cal'] = generate_cal(received)

    def generate_nutrients(my_dict):
        carb = str(round((my_dict['cal'] * 0.45), 2))
        prot = str(round((my_dict['cal'] * 0.3), 2))
        fat = str(round((my_dict['cal'] * 0.25), 2))

        return {"carboidratos": carb, "proteinas": prot, "gorduras": fat}

    # adding the nutrients to data sent by the user
    received["nutrientes"] = generate_nutrients(received)
    print('O resultado do processamento é {}'.format(received))

    # serialising
    result = json.dumps(received)

    # send a result
    clientSocket.send(result.encode('ascii'))
    print('Os dados do cliente foram enviados com sucesso!')

    # finish a connection
    clientSocket.close()