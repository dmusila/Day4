def find_missing (number1,number2):
    first_list = number1
    second_list2 = number2

    if first_list and second_list2 is 0:
        msg = 0
    elif second_list2 == first_list:
        msg =  0
    elif first_list is not  second_list2:
        newlist = set(second_list2)-set(first_list)
        popoutnumber = newlist.pop()

    return popoutnumber

