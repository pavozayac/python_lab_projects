import argparse
import json
from functools import reduce

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, help='Name of the .ipynb file to be cleaned.')

args = parser.parse_args()

def clean(fname: str):
    try:
        with open(fname, 'r') as nb, open(fname.split('.')[0]+'czysty.ipynb', 'w') as clean:
            des = json.loads(nb.read())
        
            cells: list[dict] = des['cells']
        
            cells = list(map(lambda c: c if c['cell_type']!= 'code' else c | {'outputs': []}, cells))

            des['cells'] = cells

            code_blocks = list(reduce(lambda l, c: l[:-1]+[c] if len(l) > 0 and l[-1]['cell_type'] == 'markdown' and c['cell_type'] == 'code' else l[:] + [c] if c['cell_type'] == 'markdown' and c['source'][0].find('# Ćwiczenie') != -1 else l, cells, []))

            for block in code_blocks:
                block |= {'source': []}
        
            clean.write(json.dumps(des))
    except FileNotFoundError:
        print('This file does not exist.')
        
if __name__ == '__main__':
    clean(args.filename)