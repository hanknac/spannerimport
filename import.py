#
# This application imports a csv file into a Google Cloud Spanner table
#

import argparse
import csv
import numbers
import base64

from google.cloud import spanner

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False
    
def isinteger(value):
	try:
		int(value)
		return True
	except ValueError:
		return False
		
def insert_data(instance_id, database_id, table_id, batchsize, data_file, format_file):
    """Inserts sample data into the given database.

    The database and table must already exist and can be created using
    `create_database`.
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    
    fmtfile = open(format_file, 'r')
    fmtreader = csv.reader(fmtfile)
    collist = []
    typelist = []
    icols = 0
    for col in fmtreader:
    	collist.append(col[1])
    	typelist.append(col[2])
    	icols = icols + 1
    	
    numcols = len(collist)
    
    ifile  = open(data_file, "r")
    reader = csv.reader(ifile,delimiter=',')
    alist = []
    irows = 0

    for row in reader:
        for x in range(0,numcols):
                if typelist[x] == 'integer':
                        row[x] = int(row[x])
                if typelist[x] == 'float':
                	row[x] = float(row[x])
                if typelist[x] == 'bytes':
                	row[x] = base64.b64encode(row[x])
        alist.append(row)
        irows = irows + 1
  		    		
    ifile.close()
    rowpos = 0
    batchrows = int(batchsize)
    while rowpos < irows:

            with database.batch() as batch:
                batch.insert(
                    table=table_id,
                    columns=collist,
                    values=alist[rowpos:rowpos+batchrows]
                    )

    		rowpos = rowpos + batchrows
    print 'inserted {0} rows'.format(rowpos)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--instance_id', help='Your Cloud Spanner instance ID.')
    parser.add_argument(
        '--database_id', help='Your Cloud Spanner database ID.',
        default='example_db')
    parser.add_argument(
    	'--table_id', help='your table name')
    parser.add_argument(
		'--batchsize', help='the number of rows to insert in a batch')
    parser.add_argument(
		'--data_file', help='the csv input data file')
    parser.add_argument('--format_file', help='the format file describing the input data file')
		
    args = parser.parse_args()

    insert_data(args.instance_id, args.database_id, args.table_id, args.batchsize, args.data_file, args.format_file)
