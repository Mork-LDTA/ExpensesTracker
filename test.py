while True:
    try:
        value_expense = int(input("\nDigite o valor da despesa: "))
        if value_expense != None or not value_expense == None:
            break
        else:
            value_expense= int(input("\nDigite o valor da despesa: "))
    except ValueError:
        print( "Voce Digitou um valor incorreto!")
        
        