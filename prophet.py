import numpy as np
import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plot
import os
import scipy.io
import multiprocessing

##traverse
def traverse(f):
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f,f1)
        if not os.path.isdir(tmp_path):
            po.apply_async(prophet,args=(tmp_path,))
        else:
            traverse(tmp_path)


##prophet builds
def prophet(ways):
    file_path=ways
    mm = file_path+'.mat'
    ff = file_path+'.jpg'  
    fft = file_path+'component.jpg'
    tt=open(ways)
    df = pd.read_csv(tt)
    m = Prophet()
    m.add_seasonality('quarterly', period=91.25, fourier_order=8, mode='additive')
    m.add_seasonality('monthly', period=30.5, fourier_order=8, mode='additive')
    m.fit(df)
    future = m.make_future_dataframe(periods=1)
    forecast = m.predict(future)
    m.plot(forecast)
    plot.savefig(ff)
    m.plot_components(forecast)
    plot.savefig(fft)
    matrix1 = np.transpose([forecast.trend,forecast.yearly,forecast.quarterly,forecast.monthly,forecast.weekly,forecast.daily])
    scipy.io.savemat(mm,{'matrix1':matrix1,})

    ##multiprocess
if __name__ == "__main__":
        po = multiprocessing.Pool(32)
        traverse('')


        po.close()
        po.join()