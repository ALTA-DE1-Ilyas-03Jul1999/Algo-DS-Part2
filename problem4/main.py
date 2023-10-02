def urut_barang(b):
    return (-b[1], b[0])

def count_item_and_sort(items):
    counts = {}
    for x in items:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
            
    list_items = sorted(counts.items(), key = urut_barang)
    for i in range (len(list_items)):
        for j in range (i+1, len(list_items)):
            if list_items[i][1] > list_items[j][1]:
                list_items[i], list_items[j] = list_items[j], list_items[i]
                
    result = ' '.join([f'{x[0]}->{x[1]}' for x in list_items])
    return result

if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"
