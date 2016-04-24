# pydtw

A lightweight (and hopefully quick) implementation of [dynamic time warping](https://en.wikipedia.org/wiki/Dynamic_time_warping) (and visualizations) in python/numpy/cython (some code ported from [Pierre Rouanet's implementation](https://github.com/pierre-rouanet/dtw)).

## setup
Compile the cython code with
```
python setup.py build_ext --inplace
```
and you should be good to go.  

## example usage
```
import pydtw

x0 = <T_0 x D array>
x1 = <T_1 x D array>
dist, cost, path = pydtw.dtw(x0, x1)
```
where `dist` is the dtw distance, cost is a `T_0 x T_1` matrix of pairwise distances and path is a python list of two numpy arrays that describe the index sets that best align `x0` and `x1`.  

See the [influenza example](https://github.com/andymiller/pydtw/blob/master/example_flu.ipynb) for a more concrete usage. 




