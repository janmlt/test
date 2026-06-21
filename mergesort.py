import matplotlib.pyplot as plt

def mergeSort(list): # sortiert das gegebene Array mithilfe von MergeSort Rekursiv aufsteigend
    if len(list) <= 1:  # Abbruchbedingung 
        return
    
    #Array teilen
    mid = len(list) // 2      
    left = list[:mid]
    right = list[mid:]

    #rekursiver Aufruf
    mergeSort(left)       #sortiert links vollständig   
    mergeSort(right)      #sortiert rechts vollständig

    #indices setzen
    left_index = 0
    right_index = 0
    merge_index = 0

    #Merge Verfahren
    while left_index < len(left) and right_index < len(right): # solange keins von beiden Teilen vollständig durchlaufen wurde

        if left[left_index] <= right[right_index]: # wenn linkes Element kleiner oder gleich rechtes Element wird linkes Element an der Stelle des merge_index gesetzt
            list[merge_index] = left[left_index]
            left_index += 1
        else:                                      # wenn rechts größer als links
            list[merge_index] = right[right_index]
            right_index += 1

        merge_index += 1

    # falls ein Teil vollständig durchlaufen kann der Rest angehangen werden
    while left_index < len(left):
        list[merge_index] = left[left_index]
        left_index += 1
        merge_index += 1

    while right_index < len(right):
        list[merge_index] = right[right_index]
        right_index += 1
        merge_index += 1


# Funktion legt Beschriftungen und Layout des Plots fest
def plot_values(list,title):

    x_values = range(len(list))

    plt.figure()
    plt.plot(x_values, list)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Wert")
    plt.grid(True)
    plt.show()


#Testfall
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

plot_values(my_list, "unsortiertes Array")

mergeSort(my_list)

plot_values(my_list, "sortiertes Array")

