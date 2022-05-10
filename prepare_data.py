import json
import os

from tqdm import tqdm
from dict_reader import DictReader
from format_ph import *

_target_dir = './dicts/'
_origin_file = './dicts/cmu.dict'


# Convert json dictionary to double space delimited dictionary
def convert_json_to_dict(origin_file, target_dir):
    # Read the origin file
    with open(origin_file, 'r') as f:
        origin_dict = json.load(f)
        # Get the data dictionary
        data_dict = origin_dict['data']
    # Build new dictionary
    for word in data_dict.keys():
        res = data_dict[word]['arpabet']
        data_dict[word] = res
    # Save the new dictionary
    with open(os.path.join(target_dir, 'new.dict'), 'w') as f:
        for word in data_dict.keys():
            f.write(f'{word}  {to_sds(data_dict[word])}\n')

# Main
def main():
    # First read the origin file
    origin_dict = DictReader(_origin_file).dict
    updated_dict = origin_dict.copy()
    origin_original_len = len(origin_dict)
    origin_cur_len = len(origin_dict)
    origin_additions = 0
    # Record a set of words that are added (delta)
    added_words = set()
    # Scan all files in the directory
    for file in tqdm(sorted(os.listdir(_target_dir)), position=0):
        if file.endswith('.dict') and file != 'cmu.dict':
            # Read the file
            target = DictReader(os.path.join(_target_dir, file)).dict
            # Record the additions
            set_additions = set(target.keys()) - set(origin_dict.keys())
            set_true_adds = set(target.keys()) - set(updated_dict.keys())
            # Record diff
            added_words |= set_additions
            # Add the new words to the origin dictionary
            updated_dict.update(target)
            # Report
            print(f'{file}: {len(set_additions)}/{len(target)} delta from original')
            print(f'{file}: {len(set_true_adds)}/{len(target)} added to current update')
            print('-' * 3)
            for word in set_additions:
                print(f'{word}  {to_sds(target[word])}')
    # Print the result
    print('-' * 5)
    print(f'Origin words: {origin_original_len}')
    print(f'Total additions: {len(added_words)}')
    print(f'Total words: {len(origin_dict)}')


if __name__ == '__main__':
    # main()
    origin_f = './dicts/rb-f4.json'
    target_d = './dicts/'
    convert_json_to_dict(origin_f, target_d)
    print('-' * 5)
    print('Finished')
