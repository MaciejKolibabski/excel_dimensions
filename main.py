import pandas as pd


# 'C:/Users/macie/Desktop/DiffPgCo.xlsx.xlsx'

def excel_dim(path):
    global outputx, outputy
    df = pd.read_excel(path)
    df_new = df[['Name']]
    df_s = df["Name"].str.lower()
    tabliczka=[]
    for m in range(df_s.size):
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

        last_x = tab_location[len(tab_location) - 1]
        tab_spaces.append(last_x)
        tab_spaces.sort()

        tab_spaces_with_x = []
        print()
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
            wyjscie=''
            for i in range(pos_start, pos_end):
                outputx = small_sentence[i].replace("\n", "")
                wyjscie += outputx
            wyjscie2=wyjscie.replace('x',' ').split()
            print(wyjscie2[1], end="")

    return outputx


if __name__ == '__main__':
    (excel_dim('C:/Users/macie/Desktop/DiffPgCo.xlsx'))
