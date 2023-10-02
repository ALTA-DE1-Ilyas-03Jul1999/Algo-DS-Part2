
def urutin(pair):
    for i in range (len(pair)):
        for j in range(i+1, len(pair)):
            if pair[i] < pair[j]:
                pair[i], pair[j] = pair[j], pair[i]
                
    return pair

def playing_domino(cards, deck):
    kartu_urut = urutin(deck)
    kartu_besar = kartu_urut
    # kartu_suggest = []
    
    for i in cards:
        if i[0] == kartu_besar[0] or i[0] == kartu_besar[1] or i[1] == kartu_besar[0] or i[1] == kartu_besar [1]:
            return i
    return[]

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []