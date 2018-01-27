#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wudizhangzhi
# @Date:   2018-08-24 21:51:57

import logging
from logging.handlers import  RotatingFileHandler

LOG_PATH = 'hupu.log'


def getLogger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    # file output hanlder
    fh = RotatingFileHandler(LOG_PATH,
                             maxBytes=5 * 1024 * 1024,
                             backupCount=1)
    fh.setLevel(logging.DEBUG)

    fh.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s:%(lineno)s: %(message)s'))
    log.addHandler(fh)

    return log