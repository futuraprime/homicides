import csv
from statelist import STATES, getStateAbbr

infile = 'GuardianJustifiableHomicideData.csv'

def numberize(s):
    val = s
    if s is '': return None
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

    out = {}

    for row in reader:
        for key in ('', 'stateyear', None):
            if key in row.keys(): del row[key]
        row['state'] = getStateAbbr(row['state'])
        row = { k: numberize(v) for k, v in row.iteritems() }
        print row

    f.close()    
    return out