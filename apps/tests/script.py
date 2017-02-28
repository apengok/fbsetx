import nose
import sys

from flask_script import Command


class RunTests(Command):
    """ Run the unittests"""
    def run(self,*args,**kwargs):
        nose.run(argv=[sys.argv[0]])
