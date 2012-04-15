from __future__ import division
import concat, json
from statelist import STATES

def processData():
    data = concat.processData()

    out = []

    for state in STATES:
        st_data = [x for x in data if x['state'] == state['abbr']]
        if not len(st_data): continue
    
        homicide_total = sum(x['homicide'] for x in st_data)
        justifiable_total = sum(x['justifiable'] for x in st_data)
        average_murder_rate = homicide_total / (sum(x['population'] for x in st_data)/100000)
        ratio = justifiable_total / homicide_total
    
        syg = True if sum(x['syg'] for x in st_data) > 0 else False
    
        out.append({
            'state': state['name'],
            'abbr' : state['abbr'],
            'homicide': homicide_total,
            'justifiable': justifiable_total,
            'avg_murder_rate': average_murder_rate,
            'ratio': ratio,
            'syg': syg,
        })
    
    return out
    
if __name__ == "__main__":
    print json.dumps(processData(), indent=4, sort_keys=True)