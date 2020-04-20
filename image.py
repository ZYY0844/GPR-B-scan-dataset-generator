from scipy import signal
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
import os
import sys
import numpy as np
from tqdm import tqdm
from tools.plot_Bscan import get_output_data
from generator import Generator
from gprMax.input_cmd_funcs import command
from scipy import signal
import matplotlib.pyplot as plt
from plot_Bscan import mpl_plot, mpl_plot_post, mpl_plot_color,mpl_plot_fre
import argparse
import h5py
from gprMax.exceptions import CmdInputError
from tools.outputfiles_merge import get_output_data
# from generator import _prepare_bscan

filename2='test/final_1_merged.out'

outputdata, dt = get_output_data(filename2, 1, 'Ez')
mpl_plot(filename2, outputdata, dt, 1, 'Ez')

outputdata = outputdata - np.mean(outputdata, axis=1, keepdims=True)
# outputdata=((1-1/np.arange(outputdata.shape[0]))**12).reshape(outputdata.shape[0], 1)
# outputdata = outputdata * (np.arange(outputdata.shape[0])/outputdata.shape[0]).reshape(outputdata.shape[0], 1)

mpl_plot_post(filename2, outputdata, dt, 1, 'Ez')

