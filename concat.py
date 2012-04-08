import homicides, justifiable
from statelist import STATES

def processData():
    hom = homicides.getData()
    just = justifiable.getData()

    years = range(2001,2011)

    out = []

    for state in STATES:
        for y in years:
            hdata = filter(lambda x: x['year'] == y and x['state'] == state['abbr'], hom)
            jdata = filter(lambda x: x['year'] == y and x['state'] == state['abbr'], just)
            if not len(hdata) or not len(jdata):
                continue
            hdata = hdata[0]
            jdata = jdata[0]
            out.append(dict(hdata.items() + jdata.items()))
    
    return out


if __name__ == "__main__":
    import json
    print json.dumps(processData(), indent=4, sort_keys=True)