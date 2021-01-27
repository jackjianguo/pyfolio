import os
import sys
import pandas as pd
import pyfolio as pf
from pyfolio import plotting

# silence warnings
import warnings
warnings.filterwarnings('ignore')


def sharpe():
    df = pd.read_csv('demo/test.csv')
    df['date'] = pd.to_datetime(df['period_close'])
    df = df.set_index('date')
    # pf.create_returns_tear_sheet(df['returns'], live_start_date='2015-12-1')
    # perf_stats, header_show = pf.create_returns_tear_sheet(df['returns'])
    """[plotting.show_perf_stats]
    perf_stats: pd.DataFrame
    =========================================================================
    perf_stats                      Backtest
    Annual return                   19848.041%
    Cumulative returns              23.386%
    Annual volatility               160.629%
    Sharpe ratio                    4.02151
    Calmar ratio                    1145.31
    Stability                       0.695536
    Max drawdown                    -17.33%
    Omega ratio                     2.25969
    Sortino ratio                   8.91307
    Skew                            0.480471
    Kurtosis                        -0.460014
    Tail ratio                      2.01356
    Daily value at risk             -17.674%

    header_show
    =========================================================================
    header_show OrderedDict([('Start date', '2020-01-01'), ('End date', '2020-01-10'), ('Total months', 0)])

    header_show['Start date']
    header_show['End date']
    header_show['Total months']
    """
    perf_stats, header_show = plotting.show_perf_stats(df['returns'])
    print('perf_stats', perf_stats)
    print('header_show', header_show)
    return perf_stats, header_show

if __name__ == '__main__':
    sharpe()
    pass
