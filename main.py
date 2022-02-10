import pandas as pd

df = pd.read_excel('C:/Users/macie/Desktop/nowe1.xlsx')
df_new = df[['Name']]
df_s = df["Name"].str.lower()
print(df_s[85])



print('Size: ', df_s.size)

for m in range(df_s.size):
    #sentence = df_new
    small_sentence = df_s[m]
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

    # print("Amount of 'x' =", amount)
    # print("Locations of 'x' ", tab_location)
    # print("Free spaces", tab_spaces)
    last_x = tab_location[len(tab_location) - 1]
    # print('Last X:' , last_x)
    tab_spaces.append(last_x)
    tab_spaces.sort()
    # print(tab_spaces)

    tab_spaces_with_x = []
    print()
    for i, x in enumerate(tab_spaces):
        if x == last_x:
            position_in_tab = i
            # print(position_in_tab)
            # print(tab_spaces[position_in_tab])
            tab_spaces_with_x.append(tab_spaces[position_in_tab - 1])
            tab_spaces_with_x.append(tab_spaces[position_in_tab])
            tab_spaces_with_x.append(tab_spaces[position_in_tab + 1])

    tab_spaces_with_x.sort()
    # print(tab_spaces_with_x)
    pos_x = tab_spaces_with_x[1]
    # print(pos_x)
    # print(sentence[pos_x-1])
    pos_start = tab_spaces_with_x[0] + 1
    pos_end = tab_spaces_with_x[2]
    # print(pos_start, pos_end)
    print('Wymiary: ',m,' ', end="")
    if (small_sentence[pos_x - 1].isdigit() and small_sentence[pos_x + 1].isdigit()):
        for i in range(pos_start, pos_x):
            output=small_sentence[i].replace("x", ' ')
            print(output, end="")
        print(' ', end="")
        for j in range(pos_x + 1, pos_end):
            print(small_sentence[j], end="")
    else:
        print('To nie są wymiary')
