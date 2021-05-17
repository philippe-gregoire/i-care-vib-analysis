# I-care Simulator

http://192.168.10.191:1880/ui/#!/3

ibm / ibmwatson

- channel 1: bearing 1 horizontal
- channel 2: bearing 1 vertical
- channel 3: bearing 2 horizontal

# Labelled condition data
The `ConditionData\` folder contains condition data to be used for supervised learning.
There are 4 condition classes, with corresponding data files held in subfolders per condition:
   * `normal`: no specific condition
   * `SI`: Structural Imbalance
   * `WI`: Wheel Imbalance
   * `SIandWI`: Structural and Wheel Imbalance
There are a collection of JSON files in each of the subfolders, representing the values of the `fftv` and `fftg`, `rpm`, `temperature` attributes.

In order to use this raw data as a supervised learning training set to submit to **AutoAI**, it will need to be realigned in a flat `.csv` file structure.

This is achieved using the code in 
The code in
