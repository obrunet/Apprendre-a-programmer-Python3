# Écrivez une fonction permettant de trier une liste. Cette fonction ne pourra pas utiliser la méthode intégrée sort() de Python : 
# vous devez donc définir vous-même l’algorithme de tri. 

def bubble_sort(list):
    swapping = True
    passing = 0
    while swapping == True:
        swapping = False
        passing = passing + 1
        for current in range(0, len(list) - passing):
            if list[current] > list[current + 1]:
                swapping = True
                # swapping the 2 elts
                list[current], list[current + 1] = \
                list[current + 1], list[current]
    return list

# Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, 
# compares adjacent pairs and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. 
# https://en.wikipedia.org/wiki/Bubble_sort


if __name__ == "__main__":
    unsortedlist = [4, 2, 8, 1, 7, 5, 3, 6]
    print(unsortedlist)
    print(bubble_sort(unsortedlist))