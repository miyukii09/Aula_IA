# Strings fornecidas
nomes = "ANA CLARA NOGUEIRA DE ARAÚJO;ANA LAURA FARIA SANTOS;ANA LAURA FERNANDES DA SILVA;BETÂNIA AMÂNCIO PEREIRA;BRENO ESTORARI DA SILVA;EDUARDO BELLO GALEGO;EDUARDO HENRIQUE DO CARMO;ERIKA DE BRITTO CÔNSOLO;FERNANDA GARCIA FLORIANO;GIUSEPPE FRANCESCO STRACERI IANES BAGGIO;GUSTAVO MEDEIROS DE BARROS;GUSTAVO PEREIRA GARCIA;JOAO PEDRO BILLO LUCIANO;JOAO VICTOR SALOTI ALVES;KAUA DANTAS MARTINS;KEVIN RENAN NOGUEIRA DA SILVEIRA;LAIS CUNHA THEODORO DA SILVA;LAVINIA DAL BELLO E SOUZA;LUIS OTAVIO FLORENCIO BARBOSA;LUIS OTAVIO MORAIS DE SOUZA;LUIZA HELENA TARDELLI MARCULLI ESPINDOLA;MARIA CAROLINA SILVA GARCIA;MARIA CLARA SANTOS MANETA;MARIA FERNANDA GRESPAN BENFEITO;MARIA FERNANDA TOBIAS CHAGAS;MATHEUS CARVALHO FELISBERTO;MURILO ANTONIO BARION;NICOLY GOMES SERRANO;OCTAVIO AUGUSTO ANDREAZZI CHAVES;PEDRO VINICIUS VIEIRA VASCONCELLOS;RAFAEL CREMASCO;RAFAEL LOPES PIRES;RAQUEL MOREIRA FERNANDES CUSTODIO;RENAN HENRIQUE TEIXEIRA;SABRYNA SATORRES BATISTINI;SOPHIA RUEDA GONÇALVES DA RITA;TAYNARA DE MELLO SIQUEIRA;TIFANI SCHIAVON MISSURA;VITORIA CIPRIANO DE JESUS;WESLEY RICARDO SILVA PEREIRA"
notas = "9.33;8.76;6.11;1.09;2.76;2.97;9.04;3.62;3.37;1.76;8.14;2.48;3.27;9.16;9.01;1.55;2.98;3.41;8.45;5.79;0.54;2.01;6.78;1.09;4.75;0.09;7.62;0.53;8.95;6.93;1.04;2.87;7.85;6.65;6.96;9.72;9.42;0.44;6.78;7.54"
faltas = "23;5;14;5;29;20;19;2;23;5;18;27;6;8;28;29;5;7;7;19;6;14;4;21;25;25;17;23;21;13;1;19;27;21;26;27;7;19;5;21"
 
# Transformando as strings em listas
nomes_lista = nomes.split(';')
notas_lista = list(map(float, notas.split(';')))
faltas_lista = list(map(int, faltas.split(';')))
 
# 2) Exibindo uma listagem com o nome, nota e falta dos alunos
print("Listagem de alunos com nota e faltas:")
for i in range(len(nomes_lista)):
    print(f"• Nome: {nomes_lista[i]}")
    print(f"• Nota: {notas_lista[i]}")
    print(f"• Falta: {faltas_lista[i]}")
    print()
 
# 3) Listagem de alunos aprovados (média >= 6)
print("Alunos aprovados (média >= 6.0):")
alunos_aprovados = 0
for i in range(len(nomes_lista)):
    if notas_lista[i] >= 6.0:
        print(f"• Nome: {nomes_lista[i]}")
        alunos_aprovados += 1
print(f"Total de alunos aprovados: {alunos_aprovados}")
print()
 
# 4) Listagem de alunos reprovados por falta (faltas > 20)
print("Alunos reprovados por falta (faltas > 20):")
alunos_reprovados_falta = 0
for i in range(len(nomes_lista)):
    if faltas_lista[i] > 20:
        print(f"• Nome: {nomes_lista[i]}")
        alunos_reprovados_falta += 1
print(f"Total de alunos reprovados por falta: {alunos_reprovados_falta}")
print()
 
# 5) Listagem de alunos com sobrenome SILVA
print("Alunos com o sobrenome SILVA:")
alunos_silva = 0
for i in range(len(nomes_lista)):
    if "SILVA" in nomes_lista[i]:
        print(f"• Nome: {nomes_lista[i]}")
        alunos_silva += 1
print(f"Total de alunos com o sobrenome SILVA: {alunos_silva}")
print()
 
# 6) Listagem dos alunos com nome e sobrenome formatados
print("Alunos com nome e sobrenome formatados:")
for i in range(len(nomes_lista)):
    nome_parts = nomes_lista[i].split()
    nome_formatado = f"{nome_parts[0].capitalize()} {nome_parts[-1].capitalize()}"
    print(f"• {nome_formatado}")
print()
 
# 7) Listagem dos alunos com nome completo abreviado
print("Alunos com nome completo abreviado:")
for i in range(len(nomes_lista)):
    nome_parts = nomes_lista[i].split()
    nome_abreviado = f"{nome_parts[0]} "  # Primeiro nome completo
    for part in nome_parts[1:-1]:  # Abrevia os nomes do meio
        nome_abreviado += part[0] + ". "
    nome_abreviado += nome_parts[-1]  # Sobrenome completo
    print(f"• {nome_abreviado}")
print()
 