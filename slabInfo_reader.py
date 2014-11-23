__author__ = 'dhana013'

import os


PROC_SLAB_FILE = '/home/dhana013/slabinfo'

#open file

def collect_data():


    if not os.access(PROC_SLAB_FILE, os.R_OK):
        return False

    #open ProcFile
    file = open(PROC_SLAB_FILE, 'r')

    for lines in file:
        if lines.startswith('slabinfo'):
            #print lines
            continue

        if lines.startswith('#'):
            keys = lines.split()[1:]
            print keys
            continue


        data = lines.split()
        #print data

        for key in ['<active_objs>', '<num_objs>', '<objsize>', '<objperslab>', '<pagesperslab>']:
            i = keys.index(key)
            metric_name = data[0] + '.' + key.replace('<','').replace('>','')
            metric_value = int(data[i])
            print metric_name +' '+ str(metric_value)


        for key in ['<limit>', '<batchcount>', '<sharedfactor>']:
            i = keys.index(key)
            metric_name = data[0] + '.tunnable.' + key.replace('<','').replace('>','')
            metric_value = int(data[i])
            print metric_name +' '+ str(metric_value)

        for key in ['<active_slabs>', '<num_slabs>', '<sharedavail>']:
            i = keys.index(key)
            metric_name = data[0] + '.slabdata.' + key.replace('<','').replace('>','')
            metric_value = int(data[i])
            print metric_name +' '+ str(metric_value)


    file.close()



if __name__ == "__main__":
    collect_data()

