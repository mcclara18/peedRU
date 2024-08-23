
import refeicoesru as ru
presentestotal=reservatotal=prescreme=faltacreme=0
visto=[]
repetido=[]
ID2153=0
for dicionario in ru.data:
    reservatotal+=1
    if dicionario["WASPRESENT"]==1:
        presentestotal+=1
        if dicionario["STUDENT_ID"] in visto:
            repetido.append(dicionario["STUDENT_ID"])
        else:
            visto.append(dicionario["STUDENT_ID"])
        if dicionario["STUDENT_ID"]==2153:
            ID2153+=1
        if dicionario["MENU_ID"]==2421:
            prescreme+=1
    elif dicionario["WASPRESENT"]==0:
        if dicionario["MENU_ID"]==2421:
            faltacreme+=1
porcentagem=round((presentestotal/reservatotal),2)


print(f"""
01) Quantas refeições foram marcadas como presentes no dia 10/04/2024 em todas as refeições?
        Resposta: {presentestotal}
02) Qual a porcentagem de presença geral dos alunos em todas as refeições do dia 2024-04-10?
        Resposta: {porcentagem*100}%
03) Quantos alunos estiveram presentes na refeição que serviu Creme de Galinha no dia 10/04/2024?
        Resposta: {prescreme}
04) Quantos alunos NÃO estiveram presentes na refeição que serviu Creme de Galinha no dia 10/04/2024?)
        Resposta: {faltacreme}
05) Qual aluno registrou presença em mais de um menu no dia 2024-04-10?
        Resposta: """, end="")
for c in range (len(repetido)):
    if c!= (len(repetido)-1):
        print(f"{repetido[c]}, ", end="")
    else:
        print(f"{repetido[c]}.")
print(f"""f) Quantos menus diferentes o aluno com STUDENT_ID 2153 registrou presença no dia 2024-04-10?
       Resposta: {ID2153}""")

        