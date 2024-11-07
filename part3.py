def food_order():
   
    print("Что вы хотите заказать? (шаурма, самсы, пирожки)")
    food = input()
   
    if food == "шаурма":
        print("С какой начинкой? (мясо, курица)")
        inside = input()
        if inside != "мясо" and inside != "курица":
            print("Такой начинки нет")
            return
    
    elif food == "самсы":
        print("С какой начинкой? (мясо, курица, сыр)")
        inside = input()
        if inside == "сыр":
            print("Самсы с сыром закончились, будут через 15 минут. Вы хотите подождать? (да/нет)")
            answer = input()
            if answer == "нет":
                print("Заказ отменён")
                return
        elif inside != "мясо" and inside != "курица":
            print("Такой начинки нет")
            return
    
    elif food == "пирожки":
        print("С какой начинкой? (картошка, капуста)")
        inside = input()
        if inside != "картошка" and inside != "капуста":
            print("Такой начинки нет")
            return
    
    else:
        print("Такого блюда нет")
        return
    

    print("Сколько штук хотите?")
    quantity = input()
    

    print("Нужно ли подогреть? (да/нет)")
    heat = input()
    
    print("Что будете пить? чай, кофе, кола, минералка или ничего?")
    drink = input()

    order = f"Вы заказали: {quantity} {food} с начинкой {inside}"
    
    if heat == "да":
        order = order + ", подогретое"

    if drink != "":
        order = order + ", напиток: " + drink + "."
    else:
        order = order + ". Вы не взяли напиток."

    print(order)


food_order()