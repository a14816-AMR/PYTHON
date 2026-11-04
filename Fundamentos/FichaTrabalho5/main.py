import os
#2
products = []


#3
def add(nome_produto, preco, iva = 0.23):
    return {
        "product": nome_produto,
        "price": preco,
        "tax": iva
    }


products.append(add("Computador", 1250, 0.13))
print(products[0])


#4
def update_final_price(produto):
    produto["finalPrice"] = round(produto["price"] * (1 + produto["tax"]),2)


update_final_price(products[0])
print(products[0])


#5
def print_product(produto):
    return f"O produto {produto["product"]} com o preço de {produto["price"]} e o iva de {produto["tax"]*100}% tem preço final de {produto["finalPrice"]}"


print(print_product(products[0]))




#7
resposta = 0


def produtoEspecifico(nomeProduto):
    for produto in products:
        if nomeProduto == produto["product"]:
            print(f"Nome do produto: {produto["product"]}")
            print(f"Preco do produto: {produto["price"]}")
            print(f"IVA do produto: {produto["tax"]}")


def menu(resposta):
    while (resposta != 5):
        print("\n1 - Inserir novo Produto")
        print("2 - Listar os produtos existentes")
        print("3 - Atualizar o preço final de todos os produtos existentes na lista")
        print("4 - Imprimir os dados de um produto específico")
        print("5 - Terminar a aplicação\n")


        resposta = int(input("Escolha uma opção: "))


        match (resposta):
            case 1:
                nomeProduto = input("Nome do produto: ")
                precoProduto = float(input("Preco do produto: "))
                ivaProduto = float(input("Qual o IVA do produto: "))
                products.append(add(nomeProduto,precoProduto,ivaProduto))
            case 2:
                for produto in products:
                    if "finalPrice" not in produto.keys():
                        update_final_price(produto)
                    print(print_product(produto))
                x = input("Prima uma tecla para continuar ...")
            case 3:
                for produto in products:
                    update_final_price(produto)
                print("Feito!")
            case 4:
                nomeProduto = input("Qual o nome do produto: ")
                produtoEspecifico(nomeProduto)
            case 5:
                break
            case _:
                print("Valor Inválido")
                x = input("Prima uma tecla para continuar ...")




menu(resposta)