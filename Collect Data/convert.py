import csv
import json
import pandas

def flattenjson( b, delim ):
    val = {}
    for i in b.keys():
        if isinstance( b[i], dict ):
            get = flattenjson( b[i], delim )
            for j in get.keys():
                val[ i + delim + j ] = get[j]
        else:
            val[i] = b[i]

    return val

# change this to json file name
f = open('apple.json')
data = json.load(f)
f.close()

input = map( lambda x: flattenjson( x, "__" ), data )
columns = [ x for row in input for x in row.keys() ]
columns = list( set( columns ) )

with open( 'data.csv', 'wb' ) as out_file:
    csv_w = csv.writer( out_file )
    csv_w.writerow( columns )

    for i_r in input:
        csv_w.writerow( map( lambda x: i_r.get( x, "" ), columns ) )
