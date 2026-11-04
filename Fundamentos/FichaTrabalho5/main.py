from functions import add, update_final_price, print_products, menu
import os


products = []
escolha = menu()


while True:
    match (escolha):
        case "1":
            prd = input("Digite o nome do produto: ")
            pri = float(input("Digite o preço do produto: "))
            iva = float(input("Iva do produto: "))
            products.append(add(prd,pri,iva))
        case "2":
            for product in products:
                print(print_products(product))
        case "3":
            for product in products:
                update_final_price(products[0])
        case "4":
                ...
        case "5":
            break
    # os.system("clear")
    escolha = menu()
    
    

products.append(add("camisa",12.23,0.13))
