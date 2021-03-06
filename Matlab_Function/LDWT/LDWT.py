#!/usr/bin/env python
# -*- coding = utf-8 -*-

"""
 @ Create Time: 2018/3/7
 @ Author: songpo.zhang
 @ Target:
"""

import numpy as np

def LDWT(inputs, DecLevel, WaveRemain, Fs, Flag):

    Si = inputs
    N = len(inputs)

    a = -1.586134342
    b = -0.052980118
    c = 0.882911075
    d = 0.443506852
    e = 1.230174105

    # S = [] # 需要初始化S，不能为空List
    S = np.zeros(N)

    for jj in range(DecLevel):
        N = int(N / 2) # 取整

        for ii in range(N):
            """
            matlab中下标从1开始，python中是从0开始
            S(ii)=Si(2*(ii-1)+1);
            S(ii+N)=Si(2*ii);
            """
            S[ii] = Si[2 * ii]
            S[ii + N] = Si[2 * ii + 1]

        for ii in range(N):
            if ii == (N - 1):
                S[ii + N] = S[ii + N] + a * (S[ii] + S[ii] + S[ii] - S[ii - 1])
            else:
                S[ii + N] = S[ii + N] + a * (S[ii] + S[ii + 1])

        for ii in range(N):
            if ii == 0:
                S[ii] = S[ii] + b * (S[ii + N] + S[ii + N] + S[ii + N] - S[ii + 1 + N])
            else:
                S[ii] = S[ii] + b * (S[ii + N] + S[ii - 1 + N])

        for ii in range(N):
            if ii == (N - 1):
                S[ii + N] = S[ii + N] + c * (S[ii] + S[ii] + S[ii] - S[ii - 1])
            else:
                S[ii + N] = S[ii + N] + c * (S[ii] + S[ii + 1])

        for ii in range(N):
            if ii == 0:
                S[ii] = S[ii] + d * (S[ii + N] + S[ii + N] + S[ii + N] - S[ii + 1 + N])
            else:
                S[ii] = S[ii] + d * (S[ii + N] + S[ii - 1 + N])

        for ii in range(N):
            S[ii + N] = S[ii + N] / e
            S[ii] = S[ii] * e
            Si[ii] = S[ii]

        if (jj != (WaveRemain-1)):
            S[N : 2*N] = np.zeros(N)

        if Flag == 0:
            if jj == (DecLevel - 1):
                Si[:N] = np.zeros(N)

    for jj in range(DecLevel):

        for ii in range(N):
            S[ii] = Si[ii]
            S[ii] = S[ii] / e
            S[ii + N] = S[ii + N] * e

        for ii in range(N):
            if ii == 0:
                S[ii] = S[ii] - d * (S[ii + N] + S[ii + N] + S[ii + N] - S[ii + 1 + N])
            else:
                S[ii] = S[ii] - d * (S[ii + N] + S[ii - 1 + N])

        for ii in range(N):
            if ii == (N - 1):
                S[ii + N] = S[ii + N] - c * (S[ii] + S[ii] + S[ii] - S[ii - 1])
            else:
                S[ii + N] = S[ii + N] - c * (S[ii] + S[ii + 1])

        for ii in range(N):
            if ii == 0:
                S[ii] = S[ii] - b * (S[ii + N] + S[ii + N] + S[ii + N] - S[ii + 1 + N])
            else:
                S[ii] = S[ii] - b * (S[ii + N] + S[ii - 1 + N])

        for ii in range(N):
            if ii == (N - 1):
                S[ii + N] = S[ii + N] - a * (S[ii] + S[ii] + S[ii] - S[ii - 1])
            else:
                S[ii + N] = S[ii + N] - a * (S[ii] + S[ii + 1])

        for ii in range(N):
            Si[2 * ii] = S[ii]
            Si[2 * ii + 1] = S[ii + N]

        N = N * 2

    return Si
