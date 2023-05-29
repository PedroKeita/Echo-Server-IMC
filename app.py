class App:

    # Display the title of the app and generate the header for data input
    def __init__(self):
        App.title("The shape of us!")
        print()
        print("=> Informe alguns dados para começar: ")
        print()
        App.generate_header()

    # Add padding
    @classmethod
    def padding(cls):
        print()
        print()

    # Generate the header with instructions for data input
    @classmethod
    def generate_header(cls):
        print("OBS: O Nivel de atividade varia de 1 (Sedentário) a 4 (Muito Ativo) !")
        print("Ex: {:^8s} {:^22s} {:^14s} {:^20s} {:^10s} ".format("1.70", "70.0", "M", "3", "20"))
        print()

    # Print a row of asterisks
    @classmethod
    def row(cls):
        print('*' * 81)

    # Print a row of hyphens for table formatting
    @classmethod
    def row_table(cls):
        print(f"+{'-' * 25}++{'-' * 25}++{'-' * 25}+")

    # Display a title surrounded by rows of asterisks
    @classmethod
    def title(cls, title):
        App.row()
        print('*{:^79s}*'.format(title))
        App.row()

    #Prompt the user to enter data for analysis
    @classmethod
    def collect_user_data(cls):
        print("{:^16s}".format("Altura (m):"), end="")
        print("{:^18s}".format("Peso (Kg):"), end="")
        print("{:^18s}".format("Sexo (M/F):"), end="")
        print("{:^18s}".format("Nvl de Ativ:"), end="")
        print("{:^16s}".format("Idade :"))

        user_data = input("")
        user_data = user_data.split(" ")
        print()
        App.row()

        return user_data

    # Create a list of user data by filtering out empty values and converting numbers
    @classmethod
    def list_user_data(cls, values):
        my_list = []
        for i in values:
            if i != "":
                if i in "Mm" or i in "Ff":
                    my_list.append(i)
                else:
                    my_list.append(float(i))
        return my_list

    # validade the user data
    @classmethod
    def validate_data(cls, values):
        while True:
            # tries to turn user data into a dict
            try:
                my_list = App.list_user_data(values)
                user_data = App.generate_dict(my_list)

            # returns to collect user data if there are insufficient values
            except IndexError:
                print()
                print('Preencha todos os dados para prosseguir!'.upper())
                print()
                App.generate_header()
                values = App.collect_user_data()

            # returns to collect user data if there are incorrect value types
            except ValueError:
                print()
                print('Valor inválido!'.upper())
                print()
                App.generate_header()
                values = App.collect_user_data()

            # keeps user data in a list type
            else:
                my_list = App.list_user_data(values)
                break

        return my_list

    @classmethod
    # turns a list into a dict
    def generate_dict(cls, my_list):
        dic = {'altura': None, 'peso': None, 'sexo': None, 'nvlAtiv': None, 'idade': None}
        cont = 0
        for k, v in dic.items():
            dic[k] = my_list[cont]
            cont += 1

        return dic

    @classmethod
    # show the calculation result
    def print_result(cls, my_list):
        print()
        App.row()
        print('|{:^25s}||{:^25s}||{:^25s}|'.format(str(my_list[0][0]), str(my_list[0][1]),
                                                   str(my_list[0][2])))
        App.row()

    @classmethod
    # shows the result for IMC
    def creat_table_imc(cls, imc, status):
        content = [['Tabela de IMC', 'Intervalo', ' Status'],
                   ['Menos do que: ', '18,5', 'Abaixo do Peso !'],
                   ['Entre: ', '18,5 e 24,9', 'Peso Normal!'],
                   ['Entre: ', '25,0 e 29,9', 'Sobrepeso!'],
                   ['Entre: ', '30,0 e 34,9', 'Obesidade Grau 1!'],
                   ['Entre: ', '35,0 e 39,9', 'Obesidade Grau 2!'],
                   ['Mais do que: ', '40,0', 'Obesidade Grau 3!'],
                   ]

        # store the result for user IMC
        result = [['SEU IMC: ', str(imc), status]]
        print()
        # shows the IMC reference table
        for row in range(0, len(content)):
            App.row_table()
            print('|{:^25s}||{:^25s}||{:^25s}|'.format(content[row][0], content[row][1],
                                                       content[row][2]))
            # prints the result for user values row == 6
            if row == 6:
                App.row_table()
                App.print_result(result)

    @classmethod

    # shows de reference table for amount of calories
    def create_table_qtd_cal(cls, my_dict):
        content = [
            ["Carboidratos: ", my_dict["carboidratos"], round(float((my_dict["carboidratos"])) / 4.0, 2)],
            ["Proteínas: ", my_dict["proteinas"], round(float((my_dict["proteinas"])) / 4.0, 2)],
            ["Gorduras", my_dict["gorduras"], round(float((my_dict["gorduras"])) / 9.0, 2)]
        ]

        for row in range(0, len(content)):
            App.row_table()
            print('|{:^25}||{:^25}||{:^25}|'.format(str(content[row][0]), str(content[row][1]) + " kcal",
                                                    str(content[row][2]) + " g"))
            App.row_table()

    @classmethod
    # manages the user choices: IMC, TBM, QTD KCAL and QUIT of the app
    def menu(cls, response):
        while True:

            # get the user choice
            App.padding()
            print("=> Selecione uma opção: ")
            print()
            print('{:^16s}{:^18s}{:^18s}{:^18s}{:2s}'.format("1 - IMC", "2 - TMB", "3 -  QTD KCAL", "4 - SAIR", ""),
                  end="\t")
            opt = input()
            App.padding()

            # if opt == 1, the IMC is calculated and displayed
            if opt == "1":
                App.title("IMC")
                print()
                print("{:^81s}".format("O Indice de Massa Corporal (IMC) é um parâmetro"))
                print("{:^81s}".format("utilizado para saber se o peso está de acordo com a altura de um"))
                print(
                    "{:^81s}".format("indivíduo, o que pode interferir diretamente na sua saúde e qualidade de vida!"))
                App.creat_table_imc(response["imc"], response["statusImc"])

            # if opt == 2, the TMB is calculated and displayed
            elif opt == "2":
                App.title("Taxa Metabólica Basal: ")
                print()
                print("{:^81s}".format("A Taxa de Metabolismo Basal (TMB) é a quantidade"))
                print("{:^81s}".format("mínima de energia (calorias) necessária para manter as"))
                print("{:^81s}".format("funções vitais do organismo em repouso. Essa taxa pode variar"))
                print("{:^81s}".format("de acordo com o sexo, peso, altura, idade e nível de atividade física."))

                result = [['RESULTADO :', 'SUA TMB:', str(response['tmb']) + " kcal"]]
                App.print_result(result)

            # if opt == 3, the QTD KCAL is calculated and displayed
            elif opt == "3":
                nut = response["nutrientes"]
                App.title("Quantidade de Calorias: ")
                print()
                print("{:^81s}".format("Calorias são a quantidade de energia que um determinado alimento"))
                print("{:^81s}".format("fornece após ser consumido, contribuindo para as funções essenciais do"))
                print(
                    "{:^81s}".format("organismo, como respiração, produção de hormônios, e funcionamento do cérebro."))

                print()
                print("{:^81s}".format("Você deve consumir aproximadamente: "))
                print()
                App.create_table_qtd_cal(nut)

                result = [['RESULTADO :', 'SUA QTD DE KCAL:', str(response['cal']) + " kcal"]]
                App.print_result(result)

            # if opt == 4, the client side app is closed
            elif opt == "4":
                print('{:^79s}'.format("Obrigado por usar nosso App !"))
                App.padding()
                App.row()
                break

            # if opt is different from all above, displays a alert for user
            else:
                print("Erro: Opção Inválida!")