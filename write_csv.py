import numpy as np
import pandas as pd
import xlwt

def nominal_metric(a, b):
    return a != b


def interval_metric(a, b):
    return (a-b)**2


def ratio_metric(a, b):
    return ((a-b)/(a+b))**2


def krippendorff_alpha(data, metric=interval_metric, force_vecmath=False, convert_items=float, missing_items=None):
    '''
    Calculate Krippendorff's alpha (inter-rater reliability):
    
    data is in the format
    [
        {unit1:value, unit2:value, ...},  # coder 1
        {unit1:value, unit3:value, ...},   # coder 2
        ...                            # more coders
    ]
    or 
    it is a sequence of (masked) sequences (list, numpy.array, numpy.ma.array, e.g.) with rows corresponding to coders and columns to items
    
    metric: function calculating the pairwise distance
    force_vecmath: force vector math for custom metrics (numpy required)
    convert_items: function for the type conversion of items (default: float)
    missing_items: indicator for missing items (default: None)
    '''
    
    # number of coders
    m = len(data)
    
    # set of constants identifying missing values
    if missing_items is None:
        maskitems = []
    else:
        maskitems = list(missing_items)
    if np is not None:
        maskitems.append(np.ma.masked_singleton)
    
    # convert input data to a dict of items
    units = {}
    for d in data:
        try:
            # try if d behaves as a dict
            diter = d.items()
        except AttributeError:
            # sequence assumed for d
            diter = enumerate(d)
            
        for it, g in diter:
            if g not in maskitems:
                try:
                    its = units[it]
                except KeyError:
                    its = []
                    units[it] = its
                its.append(convert_items(g))


    units = dict((it, d) for it, d in units.items() if len(d) > 1)  # units with pairable values
    n = sum(len(pv) for pv in units.values())  # number of pairable values
    
    if n == 0:
        raise ValueError("No items to compare.")
    
    np_metric = (np is not None) and ((metric in (interval_metric, nominal_metric, ratio_metric)) or force_vecmath)
    
    Do = 0.
    for grades in units.values():
        if np_metric:
            gr = np.asarray(grades)
            Du = sum(np.sum(metric(gr, gri)) for gri in gr)
        else:
            Du = sum(metric(gi, gj) for gi in grades for gj in grades)
        Do += Du/float(len(grades)-1)
    Do /= float(n)

    if Do == 0:
        return 1.

    De = 0.
    for g1 in units.values():
        if np_metric:
            d1 = np.asarray(g1)
            for g2 in units.values():
                De += sum(np.sum(metric(d1, gj)) for gj in g2)
        else:
            for g2 in units.values():
                De += sum(metric(gi, gj) for gi in g1 for gj in g2)
    De /= float(n*(n-1))

    return 1.-Do/De if (Do and De) else 1.

path = r'./data.xls'
data_r = pd.read_excel(path)
data = data_r.values

data = data.T
data = data[:,:15].astype(int)
rows, cols = data.shape

p = './result.xls'
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('results')
j = 0
t = 0

def amount(a,b):
    amount = 0
    for i in range(15):
        if a[i] == b[i]:
            amount += 1
    return amount

for i in range(57):
    one = data[i*3,:]
    two = data[i*3+1,:]
    three = data[i*3+2,:]
    data_piece = np.array([one,two,three])
    # pac1 = len(set(one.tolist()) & set(two.tolist())) / 15
    # pac2 = len(set(one.tolist()) & set(three.tolist())) / 15
    # pac3 = len(set(two.tolist()) & set(three.tolist())) / 15
    pac1 = amount(one,two) / 15
    pac2 = amount(one,three) /15
    pac3 = amount(two,three)/15
    pac = (pac1 + pac2 + pac3) / 3
    k_alpha =krippendorff_alpha(data_piece,nominal_metric)

    sheet.write(0,i*3,'average pairwise percent agreement')
    sheet.write(1,i*3,'pairwise agreement cols 1 & 3')
    sheet.write(2,i*3,'pairwise agreement cols 1 & 2')
    sheet.write(3,i*3,'pairwise agreement cols 2 & 3')
    sheet.write(4,i*3,'krippendorffs alpha')
    sheet.write(0,i*3+1,pac)
    sheet.write(1,i*3+1,pac2)
    sheet.write(2,i*3+1,pac1)
    sheet.write(3,i*3+1,pac3)
    sheet.write(4,i*3+1,k_alpha)

workbook.save(p)



