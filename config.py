from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

with suppress_stdout():
    import sys
    import subprocess
    import pkg_resources

    required = {'yfinance', 'investpy', 'quantstats','fpdf','mplfinance','dataframe_image'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

with suppress_stdout():
    import sys
    import subprocess
    import pkg_resources

    required = {'plotly-orca'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'conda', 'install', *missing], stdout=subprocess.DEVNULL)

import os
import sys
import numpy as np
import pandas as pd
#from datetime import datetime
import datetime
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import yfinance as yf
import investpy
import matplotlib.pyplot as plt
import quantstats as qs
import mplfinance as fplt
import matplotlib.ticker as mtick
import dataframe_image as dfi

import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table 


# estender as funcionalidades da pandas com novas métricas, plots, etc
qs.extend_pandas()
