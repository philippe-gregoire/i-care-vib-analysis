# *****************************************************************************
# © Copyright IBM Corp. 2021.  All Rights Reserved.
#
# This program and the accompanying materials
# are made available under the terms of the Apache V2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
#
# *****************************************************************************
# Formatting for I-Care vibration data condition classification
#
# This converts the directory structure with JSON files into a single
# annotated CSV file
#
# Author: Philippe Gregoire - IBM in France
# *****************************************************************************
import sys,logging

logger = logging.getLogger(__name__)

def main(argv):
    import os,io
    import argparse
    from pprint import pprint,pformat

    parser=argparse.ArgumentParser()

    parser.add_argument('-rootFolder',help=f"Root folder where training files are located",default=os.path.join(os.path.dirname(__file__),'..','ConditionData'))
    # parser.add_argument('-attributes',help='Dump attributes',action='store_true')
    # parser.add_argument('-to_csv',help='Dump dataframe to CSV file',action='store_true')
    # parser.add_argument('-to_json',help='Dump raw data JSON file',action='store_true')
    # parser.add_argument('-pathprefix',help='List Elements with this prefix only',default=None)
    # parser.add_argument('-startTime',help='Start time',default=None)

    args=parser.parse_args(argv[1:])

    # scan all the first-level directory
    conditions=[c for c in os.listdir(args.rootFolder)]
    import pandas as pd
    from datetime import datetime 
    df=pd.DataFrame()
    
    print(f"Conditions= {conditions}")
    for condition in conditions:
        # iterate JSON files within the directories
        
        for j in os.listdir(os.path.join(args.rootFolder,condition)):
            if j.endswith('.json'):
                import json
                print(f"Processing {condition}/{j}")
                with io.open(os.path.join(args.rootFolder,condition,j)) as jsonFile:
                    payload=json.load(jsonFile)['payload']
                #print(f"\t{payload.keys()}")
                # iterate the devices
                for device_data in payload.values():
                    device_data=device_data['d']
                    # print(f"{device_data.keys()}")
                    device_attrs={'deviceid':[device_data['bearing']+'_'+device_data['axis']],
                                    'speed':[device_data['rpm']],
                                    'timestamp':[datetime.fromtimestamp(device_data['timestamp'])],
                                    'temperature':[device_data['temperature']],
                                    'condition':[condition]}
                    for o in device_data.keys():
                        if o.startswith('order'):
                            device_attrs[f"{o}_fftv"]=[device_data[o]['fftv']]
                            device_attrs[f"{o}_fftg"]=[device_data[o]['fftg']]
                #print(f"{device_attrs}")
                dfDev=pd.DataFrame.from_dict(device_attrs,orient='columns')
                df=df.append(dfDev)
    # Dump as CSV file
    df.set_index(['deviceid','timestamp'],inplace=True)
    print(df.head(5))
    print(df.tail(5))
    print(f"Dumping {len(df)} rows to {args.rootFolder}.csv")
    df.to_csv(f"{args.rootFolder}.csv")


if __name__=='__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger.setLevel(logging.INFO)
    import sys
    main(sys.argv)
