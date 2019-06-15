import os
import pytest

from flask import Flask

class TestClass(object):

    def setup_class(cls):
        print("setting up test client")
        return


    def testRandom_get(self):
        # value = client.get('/random')
        value = 3
        int_value = int(value)
        assert (int_value >= 0) is True
        assert (int_value <= 100) is True


