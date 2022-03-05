def excel_dim(nazwa):
    global outputx, outputy
    sentence = nazwa
    small_sentence = sentence.lower()
    tab_location = []
    tab_spaces = []
    amount = 0

    for i in small_sentence:
        if i == "x":
            amount += 1

    for i, x in enumerate(small_sentence):
        if x == "x":
            tab_location.append(i)

    for i, x in enumerate(small_sentence):
        if x == " ":
            tab_spaces.append(i)
    last_x = tab_location[len(tab_location) - 1]
    tab_spaces.append(last_x)
    tab_spaces.sort()
    tab_spaces_with_x = []

    for i, x in enumerate(tab_spaces):
        if x == last_x:
            position_in_tab = i

            tab_spaces_with_x.append(tab_spaces[position_in_tab - 1])
            tab_spaces_with_x.append(tab_spaces[position_in_tab])
            tab_spaces_with_x.append(tab_spaces[position_in_tab + 1])

    tab_spaces_with_x.sort()
    pos_x = tab_spaces_with_x[1]
    pos_start = tab_spaces_with_x[0] + 1
    pos_end = tab_spaces_with_x[2]
    if (small_sentence[pos_x - 1].isdigit() and small_sentence[pos_x + 1].isdigit()):
        for i in range(pos_start, pos_x):
            outputx = small_sentence[i].replace("x", ' ').split()


            print(outputx, end="")

        # print(' ', end="")
        # for j in range(pos_x + 1, pos_end):
        #     outputy = small_sentence[j]
        #     #print(str(outputy), end="")


if __name__ == '__main__':
    excel_dim("CENTRO BOTANICA RETT. 3x25x75 G.1 BC")
