#!/usr/bin/env python
# encoding: utf-8

"""
Phoenix Parser
Defines the parser class which can be used to perform the parsing work using Phoenix.

Created by Bo Yu on 2009-12-11.
"""

__author__ = 'byu@ist.psu.edu (Bo Yu)'

from ctypes import *
import os
import sys

class PhoenixParser():
    """Models a single instance for Phoenix parser.
    """

    def __init__(self, config):
        """Inits the parser.

        Args:
            config: the config file
        """
        #self.grammarDir = grammarDir
        #self.grammarFile = grammarFile
        self.dictFile = "base.dic"
        self.framesFile = "frames"
        self.priorityFile = "NET_PRIORITIES"
        self.config = config
        modulePath = os.path.abspath(os.path.dirname(sys.modules[self.__module__].__file__))
        #self.libParse = cdll.LoadLibrary(os.getcwd() + '/libPhoenix.dylib')
        self.libParse = cdll.LoadLibrary(modulePath + '/libPhoenix.dylib')
        
        argn = 3
        argsList = c_char_p * argn
        argv = argsList(c_char_p("parser"), c_char_p("-config"), c_char_p(config)) 
        self.libParse.config(argn, byref(argv))
        # read grammar, initialize parser, malloc space, etc
        #self.libParse.init_parse(self.grammarDir, self.dictFile, self.grammarFile, self.framesFile, self.priorityFile)
        
    def parse(self, message):
        """parse the incoming message."""
        result = {"frame": "", "phrases":[]}
        self.libParse.init_parse()
        flag = self.libParse.parse(c_char_p(message))
        if flag == -1:
            return result    
        s = create_string_buffer('\000' * 10000)
        self.libParse.print_parse(0, byref(s))
        
        parse = repr(s.value).replace("\'","").replace(" \\n", ":").split(":")
        print parse
        result["frame"] = parse[0]
        phrases = parse[1].lower().split("].")
        newPhrases = []
        for phrase in phrases:
            newPhrases.extend(phrase.split("["))
        for phrase in newPhrases:
            if phrase != "" and not phrase in result["phrases"]:
                result["phrases"].append(phrase.rstrip())
        print "Parsing: [%s]" % ", ".join(result["phrases"])
        return result
        
    def __getstate__(self):
        odict = self.__dict__.copy() # copy the dict since we change it
        del odict['libParse']              # remove filehandle entry
        return odict

    def __setstate__(self, dict):
        self.__dict__.update(dict)   # update attributes
        if self.config:
            modulePath = os.path.abspath(os.path.dirname(sys.modules[self.__module__].__file__))
            self.libParse = cdll.LoadLibrary(modulePath + '/libPhoenix.dylib')
            argn = 3
            argsList = c_char_p * argn
            argv = argsList(c_char_p("parser"), c_char_p("-config"), c_char_p(self.config)) 
            self.libParse.config(argn, byref(argv))
        
def main():
    parser = PhoenixParser("config")
    #print (parser.libParse.gram)
    #print parser.parse("there is a nuclear release and we need to plan evacuation")


if __name__ == '__main__':
    main()



