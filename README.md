# I-care Data Analysis

This project handles data collected on the Intelligent Plant Operations (IPO) demonstrator equipped with I-Care vibration sensors.

http://192.168.10.191:1880/ui/#!/3

The data has been collected in two measurement campaigns, and resulted in two separate datasets.

The sensors data are collected by I-Care's WiCare devices, and then fed to an OSIPi server's ModBus connector, and then eventually loaded into Maximo Monitor.

The sensors channels are:
- channel 1: bearing 1 horizontal (`X1`)
- channel 2: bearing 1 vertical (`Y1`)
- channel 3: bearing 2 horizontal (`X2`)

# Labelled condition data
The `ConditionData\` folder contains condition data to be used for supervised learning.
There are 4 condition classes, with corresponding data files held in subfolders per condition:
   * `normal`: no specific condition
   * `SI` : Structural Imbalance
   * `WI`: Wheel Imbalance
   * `SIandWI`: Structural and Wheel Imbalance
There are a collection of JSON files in each of the subfolders, representing the values of the `fftv` and `fftg`, `rpm`, `temperature` attributes.

In order to use this raw data as a supervised learning training set to submit to **AutoAI**, it will need to be realigned in a flat `.csv` file structure.

This is achieved using the code in `AutoAI/build_vib_ML_dataset.py`, which outputs a `ConditionData.csv` file out of the contents of the folder.

A second data set had been collected in the form of flat csv files, running the bench in different conditions (`no_problem`, `structural_imbalance`, `wheel_imbalance` and `Anomaly`). Those files are available in `SPSSModel\` folder.

The `notebooks\Vibration_EDA_Merger.ipynb` notebook is used to display the vibration data under various angles, and collate a merged dataset.