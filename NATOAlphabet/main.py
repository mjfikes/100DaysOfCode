import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row['letter']:row['code'] for index,row in nato_df.iterrows()}

trans = input('Enter a word to translate: ').upper()

translation = [nato_dict.get(c) for c in trans if c in nato_dict.keys()]

print(translation)