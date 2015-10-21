import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np


def plot_alignment(x0, x1, path, cost, figsize=(10,10), show_xaxes=False):
    """Plots the alignment of two (one-d) time series given a DTW cost and path

    Note that plot alignment creates its own figure!

    ARGS:
        x0    : 1-d time series
        x1    : 1-d time series
        paths : a list of two paths (output from pydtw.dtw)
        cost  : the 2-d cost matrix for both paths (output from pydtw.dtw(x0, x1))

    """
    # create figure and grid it into an uneven 2x2
    fig = plt.figure(figsize=figsize)
    gs = gridspec.GridSpec(2, 2, width_ratios=[1, 5], height_ratios=[5, 1])

    # plot the second time series vertically 
    ax0 = plt.subplot(gs[0,0])
    ax0.plot(x1, np.arange(len(x1)))
    ax0.set_xlim(ax0.get_xlim()[::-1]) # reverse the x axis for this horizontal one
    ax0.set_ylim((0, len(x1)))
    ax0.get_yaxis().set_visible(show_xaxes)

    # plot the second time series horizontally 
    ax1 = plt.subplot(gs[1, 1])
    ax1.plot(np.arange(len(x0)), x0)
    ax1.get_xaxis().set_visible(show_xaxes)
    ax1.set_xlim((0, len(x0)))

    # plot the paths overlaid on the cost
    ax2 = plt.subplot(gs[0, 1])
    ax2.imshow(cost.T, origin='lower', interpolation='none')
    # red color for path
    path_color = (0.7686274509803922, 0.3058823529411765, 0.3215686274509804)
    ax2.plot(path[0], path[1], c=path_color)
    ax2.set_xlim((-0.5, cost.shape[0]-0.5))
    ax2.set_ylim((-0.5, cost.shape[1]-0.5))
    plt.tight_layout()

