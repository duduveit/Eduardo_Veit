media = []
alunos = 0
def entrada():
    alunos = int(input('Alunos: '))
    while alunos <= 0:
        print ('NÃO HOUVE PROCESSAMENTO')
def media_al():
    for i in range(alunos):
        x = float(input('Digite a media:'))
        if media_aluno >= 6:
            print('PARABÉNS VOCÊ ESTÁ APROVADO!')
        media.append(x)
        print(media)
def main():
    entrada()
    media_al()
main()
