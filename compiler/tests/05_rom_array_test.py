#!/usr/bin/env python3
# See LICENSE for licensing information.
#
# Copyright (c) 2016-2021 Regents of the University of California and The Board
# of Regents for the Oklahoma Agricultural and Mechanical College
# (acting for and on behalf of Oklahoma State University)
# All rights reserved.
#
import unittest
from testutils import *
import sys, os

import globals
from globals import OPTS
from sram_factory import factory
import debug


class rom_array_test(openram_test):

    def runTest(self):
        config_file = "{}/tests/configs/config".format(os.getenv("OPENRAM_HOME"))
        globals.init_openram(config_file)

        debug.info(2, "Testing 4x4 array for rom cell")


        data = [[1, 0, 0, 0, 0, 1, 0, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 0, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 0, 1, 1, 0, 0, 1]]

        a = factory.create(module_type="rom_base_array", cols=9, rows=8, bitmap=data, strap_spacing=4)
        self.local_check(a)
        globals.end_openram()

# run the test from the command line
if __name__ == "__main__":
    (OPTS, args) = globals.parse_args()
    del sys.argv[1:]
    header(__file__, OPTS.tech_name)
    unittest.main(testRunner=debugTestRunner())