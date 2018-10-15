#Customer choose product from the list and price of the product is shown.

def get_data():
    return [
    {'item':'rice', 'quantity':22, 'price':1.20},
    {'item':'milk', 'quantity':15, 'price':7.10},
    {'item':'bread', 'quantity':21, 'price':6.20},
    {'item':'water', 'quantity':30, 'price':6.40},
    {'item':'cheese', 'quantity':66, 'price':14.20},
    {'item':'ham', 'quantity':14, 'price':16.20},
    {'item':'chocolate', 'quantity':30, 'price':8.00},
    {'item':'eggs', 'quantity':66, 'price':9.50},
    {'item':'yoghurt', 'quantity':66, 'price':2.20},
    ]

def main():
    basket = get_data()
    sum = 0
    quantity =0

    for i in basket:
        print (i['item'])

    tab=[]
    x = raw_input ("Choose item: ")
    tab.append(x)
    for s in basket:
        if s['item'] == tab[0]:
            print ('Price for ' + s['item']+ ' = ' + str(s['price']))


if __name__ == "__main__":
    main()
