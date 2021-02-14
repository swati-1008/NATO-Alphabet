import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
# print(nato_df)

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
# print(nato_dict)

word = input("Enter a word: ").upper()
nato_list = [nato_dict[letter] for letter in word]
print(nato_list)

