# Importing the libraries
import pandas as pd
import numpy as np
import pygame
import os

# Importing the dataset
dataset = pd.read_csv('details.csv', header=None)
headings = dataset.iloc[:, 0].values.tolist()
explanations = dataset.iloc[:, 1].values

# Abbreviating the headings
abbr_headings = []
for x in headings:
    abbr = ''.join(x)
    abbr = abbr.split(' ')
    abbre = "" 
    for y in abbr:
        if y != '':
            abbre += y[0]
    abbr_headings.append(abbre)

