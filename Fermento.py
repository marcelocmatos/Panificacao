class Fermento():
    def __init__(self, fermento1):
        self.fermento = int(fermento1)

    def fermento122(self):
        levain_int = int(self)
        farinha1 = levain_int // 2.5
        agua1 = levain_int // 2.5
        levain1 = levain_int // 5

        farinha = levain1 // 2.5
        agua = levain1 // 2.5
        levain = levain1 // 5

        fermento_total1 = farinha1 + agua1 + levain1
        fermento_total = farinha + agua + levain

        return (f'Para ter {fermento_total1} de fermento, no modelo Fermento 122, você precisará de: | '
                f'Para primeira fermentação: | '
                f'* {farinha}g de farinha | '
                f'* {agua}g de água | '
                f'* {levain}g de fermento isca | '
                f'Total de fermento na primeira alimentção: {fermento_total} |  | '
                f'Para a segunda fermentação | '
                f'* {farinha1}g de farinha  | '
                f'* {agua1}g de água | '
                f'* {levain1}g da primeira alimentação')

    def fermento123(self):
        levain_int = int(self)
        farinha1 = levain_int // 2
        agua1 = levain_int // 3
        levain1 = levain_int // 6

        farinha = levain1 // 2
        agua = levain1 // 3
        levain = levain1 // 6

        fermento_total1 = farinha1 + agua1 + levain1
        fermento_total = farinha + agua + levain

        return (f'Para ter {fermento_total1} de fermento, no modelo Fermento 123, você precisará de: | '
                f'Para primeira fermentação: | '
                f'* {farinha}g de farinha | '
                f'* {agua}g de água | '
                f'* {levain}g de fermento isca | '
                f'Total de fermento na primeira alimentção: {fermento_total} |  | '
                f'Para a segunda fermentação | '
                f'* {farinha1}g de farinha  | '
                f'* {agua1}g de água | '
                f'* {levain1}g da primeira alimentação')

if __name__ == '__main__':

    tipo_fermento_str = input('* 123: 1 parte de fermento, 2 de água e 3 de farinha. | '
                              '* 122: 1 parte de fermento, 2 de água e 2 de farinnha. | '
                              'Diga qual o tipo de alimentação quer 1 para tipo 123 e 2 para tipo 122: | '
                              )
    tipo_fermento = int(tipo_fermento_str)

    if tipo_fermento == 1:
        fermento_str = input('Digite a quantia de fermento, em gramas, desejada: ')
        fermento123 = Fermento.fermento123(fermento_str)
        print(fermento123)

    elif tipo_fermento == 2:
        fermento_str = input('Digite a quantia de fermento, em gramas, desejada: ')
        fermento122 = Fermento.fermento122(fermento_str)
        print(fermento122)

    else:
        raise ValueError('Valor digitado está incorreto')


