# *****************************************************************************
# © Copyright IBM Corp. 2021.  All Rights Reserved.
#
# This program and the accompanying materials
# are made available under the terms of the Apache V2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
#
# *****************************************************************************
# Test the vibration condition prediction pipeline
#
# The pipeline has been generated using AutoAI and pickled
#
# We will apply the unpickled pipeline to test data
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

    parser.add_argument('-autoAIPipeline',help=f"Pickled Pipeline from AutoAI",default=os.path.join(os.path.dirname(__file__),'VibConditionPrediction_P3.pickle'))
    parser.add_argument('-testCSV',help=f"CSV file for testing the pipeline",default=os.path.join(os.path.dirname(__file__),'..','ICareData.csv'))

    args=parser.parse_args(argv[1:])

    try:
        import autoai_libs
        print(f"Could import autoai_libs {autoai_libs.__version__}")
    except:
        print("Could not import autoai_libs, try pip install -U autoai-libs==1.12.6")
    try:
        import sklearn
        print(f"Could import sklearn {sklearn.__version__}")
    except:
        print("Could not import sklearn, try pip install -U scikit-learn==0.23.2")

    print(f"Loading {args.autoAIPipeline}")
    with io.open(args.autoAIPipeline,'rb') as f:
        import pickle
        pipeline=pickle.load(f)

    import pandas as pd
    # Keep columns of interest plus 
    df=pd.read_csv(args.testCSV)[['timestamp','condition','deviceid', 'order1_fftv', 'order1_fftg', 'order2_fftv', 'order2_fftg', 'order3_fftv', 'order3_fftg']]
    print(df.describe(include='all'))
    cols=[c for c in df.columns[2:]]
    print(f"Keeping {','.join(cols)} columns")

    conditions=pipeline.predict(df[cols].to_numpy())
    print(conditions)
    df['predicted']=conditions
    print(df)

if __name__=='__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger.setLevel(logging.INFO)
    import sys
    main(sys.argv)
