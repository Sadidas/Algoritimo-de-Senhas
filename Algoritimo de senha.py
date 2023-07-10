# REGRAS:
# 1°_PELOMENOS 12 CARACTERES
# 2°_MISTURA DE LETRAS MAIUSCULAS, MINUSCULAS, SIMBOLOS E NUMEROS
# 3°_PRECISA SER ESCRITO EM ALGUM LUGAR PARA NÃO SER ESQUECIDO


def main():

    import random
    import string

    Deus = True

    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbolos = ['!', '@', '#', '$', '%', '&', '*', '=', '+', '/', '_', ';']
    letras = string.ascii_letters

    while Deus:
        senha = []
        caracteres = random.randint(12, 30)

        for i in range(caracteres):
            decizao = random.randint(1, 6)
            if decizao == 1 or decizao == 2 or decizao == 3:
                al_letras = random.choice(letras)
                al_letras = str(al_letras)
                senha.append(al_letras)
            elif decizao == 4 or decizao == 5:
                al_letras = random.choice(numeros)
                senha.append(al_letras)
            else:
                al_letras = random.choice(simbolos)
                senha.append(al_letras)

        stringador = ' '
        for x in senha:
            stringador += '' + x
        print(f'Senha gerada:{stringador}')

        escrever = int(input(f"Deseja salvar esta senha? (1 para sim, 0 para não)\n"))
        if escrever == 1:
            nome = input(f"Com que nome você deseja salvar esta senha?\n")
            with open("Senhas.txt", "a") as arq:
                arq.writelines('\n')
                arq.writelines(f'{nome}: {stringador}')
                arq.close()
            print(f'Senha salva com o nome {nome}')
            print("==================================================================")

        else:
            rodar = int(input(f"Deseja rodar o algoritimo novamente? (1 para sim, 0 para não)\n"))
            if rodar == 0:
                Deus = False

if __name__ == '__main__':
    main()
