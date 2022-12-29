class list_sorter:
    input_to_sort = input("Enter your Values, seperated by whitespaces: ")
    order = input("Enter the asc to sort ascending, desc for descending and leave empty if you dont want the order of values changed \n")
    list1=list(input_to_sort.split())
    list2=list(map(int,list1))
    
    def sorting(list2, order):
        if order == "asc":
            list2.sort()
            return list2
        elif order == "desc":
            list2.sort(reverse=True, )
            return list2
        else: return list2
    print(sorting(list2, order))   