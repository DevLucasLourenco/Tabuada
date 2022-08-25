from beautifultable import BeautifulTable
table = BeautifulTable()
table.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
table.columns.header.separator = '='

 
def lista_calculo(x: int, y: int, *args):
    """args: 'lista' ou 'calculo'"""
    
    lista = []
    if 'lista' in args:
        for y2 in range(y + 1):
            resul = x * y2
            lista.append(resul)
    
    return lista

if __name__ == "__main__":
    zero_dez = [n for n in range(11)]
    table.columns.header = ['x2','x3','x4','x5','x6','x7','x8','x9','x10','x']
    
    armazenar = []
    for e, numero in enumerate(zero_dez):
        armazenar = lista_calculo(numero, 10 ,'lista')
        m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10 = armazenar
        table.rows.append([m2,m3,m4,m5,m6,m7,m8,m9,m10, f'x{e}'])

    print(table)

