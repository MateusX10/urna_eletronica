from pygame import mixer
from random import randint
from time import sleep



def VerificaEmQuemVotou(vlr):
    global TotVotosCandidato1, TotVotosCandidato2, TotVotosCandidato3, TotVotosCandidato4, TotVotosCandidato5

    if vlr == "A":
        TotVotosCandidato1 += 1
    elif vlr == "B":
        TotVotosCandidato2 += 1

    elif vlr == "C":
        TotVotosCandidato3 += 1

    elif vlr == "D":
        TotVotosCandidato4 += 1

    else: #se o candidato escolhido pelo computador for o candidato 5 (e)
        TotVotosCandidato5 += 1

def line(msg, tam=60):
    print('-=' * tam)
    print(f'\t\033[1;34m{msg}\033[m')
    print('-=' * tam)

def VerificaPorcentualVotos():
    global TotVotosCandidato1, TotVotosCandidato2, TotVotosCandidato3, TotVotosCandidato4, PercentualVotosCandidato1, PercentualVotosCandidato2, PercentualVotosCandidato3, PercentualVotosCandidato4, PercentualVotosCandidato5

    PercentualVotosCandidato1 = (TotVotosCandidato1 * 100) / PopulacaoTotalPais
    PercentualVotosCandidato2 = (TotVotosCandidato2 * 100) / PopulacaoTotalPais
    PercentualVotosCandidato3 = (TotVotosCandidato3 * 100) / PopulacaoTotalPais
    PercentualVotosCandidato4 = (TotVotosCandidato4 * 100) / PopulacaoTotalPais
    PercentualVotosCandidato5 = (TotVotosCandidato5 * 100) / PopulacaoTotalPais

    

mixer.init()


TotVotosCandidato1 = TotVotosCandidato2 = TotVotosCandidato3 = TotVotosCandidato4 = TotVotosCandidato5 =  0
PopulacaoTotalPais = cont = PercentualVotosCandidato1 = PercentualVotosCandidato2 = 0
PercentualVotosCandidato3 = PercentualVotosCandidato4 = PercentualVotosCandidato5 =  0

VotoComputador = ""
opcs = ("A", "B", "C", "D", "E")
VotoUsuario = ""
NomeCandidato1 = "\033[1;34mjava\033[m"
NomeCandidato2 = "\033[1;34mJavaScript\033[m"
NomeCandidato3 = "\033[1;34mPython\033[m"
NomeCandidato4 = "\033[1;34mRuby\033[m"
NomeCandidato5 = "\033[1;34mC++\033[m"
TemaDasEleicoes = "Eleições: Melhor Linguagem de Programação 2022!"

candidatos = {"A": "Java", "B": "JavaScript", "C": "Python", "D": "Ruby", "E": "C++"}

line(TemaDasEleicoes, 30)


while True:
    PopulacaoTotalPais = int(input("\n\033[1mPopulação total do país: (deve ser acima de 100)"))
    if PopulacaoTotalPais >= 100:
        break

while True:
    line(f'Candidatos:\n\033[1;33mA - \033[m{NomeCandidato1} \n\033[1;33mB -\033[m {NomeCandidato2} \n\033[1;33mC - \033[m{NomeCandidato3} \n\033[1;33mD -\033[m {NomeCandidato4} \n\033[1;33mE -\033[m {NomeCandidato5}', 30)
    try:
        VotoUsuario = str(input("\033[1;33mSeu voto: \033[m")).strip().upper()[0]
    except:
      continue
    if VotoUsuario in opcs:
        VerificaEmQuemVotou(VotoUsuario)
        break
print(f'\033[1mVocê votou no candidato {candidatos[VotoUsuario]}')
sound = mixer.Sound("urna_som.mp3")
sound.play()
sleep(3)



while cont < PopulacaoTotalPais:
    cont += 1
    VotoComputador = opcs[randint(0,4)]
    VerificaEmQuemVotou(VotoComputador)


# Verifica a percentual dos votos de cada candidato
VerificaPorcentualVotos()

line(f'''\n\033[1;34mResultado: \n\n{NomeCandidato1}: {PercentualVotosCandidato1:.1f}% ({TotVotosCandidato1})
{NomeCandidato2}: {PercentualVotosCandidato2:.1f}% ({TotVotosCandidato2}) 
{NomeCandidato3}: {PercentualVotosCandidato3:.1f}% ({TotVotosCandidato3})
{NomeCandidato4}: {PercentualVotosCandidato4:.1f}% ({TotVotosCandidato4})
{NomeCandidato5}: {PercentualVotosCandidato5:.1f}% ({TotVotosCandidato5})
''')
    
