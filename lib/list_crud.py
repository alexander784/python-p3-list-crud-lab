def create_an_empty_list():
    return []


def create_a_list():
    new_list = [1, "Hello", True, 3.14]
    return new_list

my_list = create_a_list()
print(my_list)


def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

my_list = [1, 2, 3]
result = add_element_to_end_of_list(my_list, 4)
print(result) 


def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

my_list = [2, 3, 4]
result = add_element_to_start_of_list(my_list, 1)
print(result)

def remove_element_from_end_of_list(l):
    if l:
        l.pop()
    return l

my_list = [1, 2, 3, 4]
result = remove_element_from_end_of_list(my_list)
print(result)


def remove_element_from_start_of_list(l):
    if l:
        l.pop(0)
    return l

my_list = [1, 2, 3, 4]
result = remove_element_from_start_of_list(my_list)
print(result)  


def retrieve_first_element_from_list(l):
    if l:
        return l[0]
    return None

my_list = [1, 2, 3, 4]
result = retrieve_first_element_from_list(my_list)
print(result) 


def retrieve_element_from_index(l, index):
    if 0 <= index < len(l):
        return l[index]
    return None

my_list = [1, 2, 3, 4]
result = retrieve_element_from_index(my_list, 2)
print(result)  


def retrieve_last_element_from_list(l):
    if l:
        return l[-1]
    return None

my_list = [1, 2, 3, 4]
result = retrieve_last_element_from_list(my_list)
print(result)  