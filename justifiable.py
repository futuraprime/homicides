import csv, json
from statelist import STATES, getStateAbbr

infile = 'GuardianJustifiableHomicideData.csv'

def numberize(s):
    val = s
    if s is '': return 0
    try:
        val = int(s)
    except ValueError:
        try:
            val = float(s)
        except ValueError:
            pass
    return val

def getData(crimefile=infile):
    f = open(crimefile, 'rU')
    reader = csv.DictReader(f)

    out = []

    for row in reader:
        for key in ('', 'stateyear', None):
            if key in row.keys(): del row[key]
        row['state'] = getStateAbbr(row['state'])
        row = { k: numberize(v) for k, v in row.iteritems() }
        out.append(row)

    f.close()
    return out

if __name__ == "__main__":
    print json.dumps(getData(), indent=4, sort_keys=True)
