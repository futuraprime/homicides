from __future__ import division
import concat, json
from statelist import STATES

data = concat.processData()

out = {}

for state in STATES:
    st_data = [x for x in data if x['state'] == state['abbr']]
    if not len(st_data): continue
    
    homicide_total = sum(x['homicide'] for x in st_data)
    justifiable_total = sum(x['justifiable'] for x in st_data)
    ratio = justifiable_total / homicide_total
    
    syg = True if sum(x['syg'] for x in st_data) > 0 else False
    
    out[state['abbr']] = {
        'state': state['name'],
        'homicide': homicide_total,
        'justifiable': justifiable_total,
        'ratio': ratio,
        'syg': syg,
    }
    
print json.dumps(out, indent=4, sort_keys=True)