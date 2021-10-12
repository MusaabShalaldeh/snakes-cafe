with open("../assets/start_message.txt") as f:
    print(f.read())

ordersList = [
    ["Wings", 0],
    ["Cookies", 0],
    ["Spring Rolls", 0],
    ["Salmon",0],
    ["Steak",0],
    ["Meat Tornado",0],
    ["A Literal Garden",0],
    ["Ice Cream",0],
    ["Cake",0],
    ["Pie",0],
    ["Coffee",0],
    ["Tea",0],
    ["Unicorn Tears",0]
]

def check_if_item_exists_in_nested_list(_list,item):
    """
    Check if item exists in a nested list
    The item we want to look at must sit a 0 in the nested list
    """
    for i in range(0,len(_list)):
        if _list[i][0] == item:
            return True
    
    return False

inputMessage = ""


while(inputMessage != "quit"):

    inputMessage = input("")

    if check_if_item_exists_in_nested_list(ordersList,inputMessage):
        for i in range(0,len(ordersList)):
            if ordersList[i][0] == inputMessage:
                ordersList[i][1] += 1 
                message = f"** {ordersList[i][1]} order of {ordersList[i][0]} have been added to your meal **"
                print(message)
                break
            else:
                continue
    else:
        message = f"**The item you ordered doesn't exist on our menu! but worry not, we can put it on to-add list!**"
        print(message)