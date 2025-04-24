def calcular_total_venda(linha):
    partes = linha.strip().split(';')
    if len(partes) != 3:
        raise ValueError("Linha mal formatada: deve conter 3 elementos separados por ponto e vírgula.")
    
    nome = partes[0].strip()
    quantidade = int(partes[1].strip())
    preco_unitario = float(partes[2].strip())
    total = quantidade * preco_unitario
    return nome, total

def main():
    total_geral = 0.0

    try:
        with open('vendas.txt', 'r', encoding='utf-8') as arquivo:
            next(arquivo)  
            for i, linha in enumerate(arquivo, start=2):  
                if not linha.strip():
                    continue
                try:
                    nome, total = calcular_total_venda(linha)
                    print(f'{nome}: R$ {total:.2f}')
                    total_geral += total
                except ValueError as ve:
                    print(f'Erro na linha {i}: {ve}')
                except Exception as e:
                    print(f'Erro inesperado na linha {i}: {e}')

        print(f'\nTotal geral das vendas: R$ {total_geral:.2f}')

    except FileNotFoundError:
        print("Arquivo 'vendas.txt' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o arquivo: {e}")

if __name__ == "__main__":
    main()
