###############################################
# The MIT License (MIT)
# Copyright (c) 2017 Kevin Walchko
# see LICENSE for full details
##############################################
import os

class Base(object):
    def __init__(self, name=None):
        if bool(os.environ.get('FAKE_RPI_SUPRESS_MSG', '')) == False:
            print('<<< WARNING: using fake raspberry pi interfaces >>>')
            if name:
                print('<<< Using: {} >>>'.format(name))
