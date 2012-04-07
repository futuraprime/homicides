import csv, re
from statelist import STATES, getStateAbbr

infile = 'CrimeStateByState.csv'

state_title = re.compile(r'^Estimated crime in ([\w -]+)$')

columnKey = ('year', 'pop', 'violent_all', 'homicide', 'rape', 'robbery', 'assault')
def dataRowToDict(row):
    row = [int(x) for x in row]
    return {x[0]: x[1] for x in zip(columnKey, row) }

def getData(crimefile=infile):
    f = open(crimefile, 'rU')
    reader = csv.reader(f)

    out = {}

    for row in reader:
        # no data, move along
        if len(row) == 0: continue
    
        # possible we have a new state
        state_shift = re.match(state_title, row[0])
        if state_shift:
            state = state_shift.groups()[0]
            state = getStateAbbr(state)
            if state not in out.keys():
                out[state] = []
    
        # other text rows we can ignore
        try:
            int(row[0])
        except ValueError:
            continue
    
        # data!
        rowdata = dataRowToDict(row)
        # for now we only need 2001-2010 so
        if rowdata['year'] < 2001: continue
    
        out[state].append(rowdata)


    f.close()    
    return out

