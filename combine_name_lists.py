'''
Implement the unique_names method.
When passed two list of names, it will return a list containing the names that appear in either or both lists.
The returned list should have no duplicates

For example, calling unique_names(["Ava", "Emma", "Olivia"],["Olivia", "Sophia", "Emma"]) should return a list containg Ava, Emma, Olivia and Sophia in any order'''

def unique_names(names1, names2):
    ls = []
    for i in names1:
        ls.append(i)
    for i in names2:
        ls.append(i)
    my_set = set(ls)
    return list(my_set)

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) 
# should print Ava, Emma, Olivia, Sophia