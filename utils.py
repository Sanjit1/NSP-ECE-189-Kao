import numpy as np
import scipy.sparse
import scipy.io as sio


def window_bin(X, binWidth, binType):
    binX = np.zeros((X.shape[0], int(np.ceil(X.shape[1] / binWidth) if binType == 'first' else int(np.floor(X.shape[1] / binWidth)) )))

    for i in range(binX.shape[1]):
        bin_start = i * binWidth
        bin_end = (i + 1) * binWidth
        if binType == 'sum':
            binX[:, i] = np.nansum(X[:, bin_start:bin_end].todense(), axis=1).flatten() if type(X) == scipy.sparse._csr.csr_matrix else np.sum(X[:, bin_start:bin_end], axis=1).flatten()
        elif binType == 'mean':
            binX[:, i] = np.nanmean(X[:, bin_start:bin_end].todense(), axis=1).flatten() if type(X) == scipy.sparse._csr.csr_matrix else np.mean(X[:, bin_start:bin_end], axis=1).flatten()
        elif binType == 'first':
            binX[:, i] = X[:, bin_start].todense().flatten() if type(X) == scipy.sparse._csr.csr_matrix else X[:, bin_start].flatten()
        elif binType == 'last':
            binX[:, i] = X[:, bin_end - 1].todense().flatten() if type(X) == scipy.sparse._csr.csr_matrix else X[:, bin_end - 1].flatten()
        else:
            raise ValueError('binType must be one of sum, mean, first, or last')

    return np.array(binX)