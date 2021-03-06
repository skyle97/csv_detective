from os.path import dirname, join
from csv_detective.process_text import _process_text
import re

PROPORTION = 1

def _is(val):
    '''Renvoie True si val peut être un code FANTOIR/RIVOLI, False sinon'''

    regex = r'^[0-9A-Z][0-9]{3}[ABCDEFGHJKLMNPRSTUVWXYZ]$'
    if not bool(re.match(regex, val)):
        return False

    f = open(join(dirname(__file__), 'code_fantoir.txt'), 'r')
    liste = f.read().split('\n')
    f.close()
    return val[:4] in liste
