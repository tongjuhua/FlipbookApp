########################################################################
#
#    Vision Node - Python source code - file generated by vision
#    Monday 26 November 2007 06:48:53 
#    
#       The Scripps Research Institute (TSRI)
#       Molecular Graphics Lab
#       La Jolla, CA 92037, USA
#
# Copyright: Daniel Stoffler, Michel Sanner and TSRI
#   
# revision: Guillaume Vareille
#  
#########################################################################
#
# $Header: /opt/cvs/VisionLibraries/scipylib/signal/wavePlay.py,v 1.3 2007/11/29 19:58:17 vareille Exp $
#
# $Id: wavePlay.py,v 1.3 2007/11/29 19:58:17 vareille Exp $
#
import time, wave, pymedia.audio.sound as sound
import os
# import node's base class node
from NetworkEditor.items import NetworkNode
class wavePlay(NetworkNode):
    mRequiredTypes = {}
    mRequiredSynonyms = [
    ]
    def __init__(self, constrkw = {},  name='wavePlay', **kw):
        kw['constrkw'] = constrkw
        kw['name'] = name
        apply( NetworkNode.__init__, (self,), kw)
        code = """def doit(self, frames, sample_rate, channels):
        format= sound.AFMT_S16_LE
        snd= sound.Output( sample_rate, channels, format )
        snd.play( frames )
        while snd.isPlaying(): time.sleep(0.05)
"""
        self.configure(function=code)
        self.inputPortsDescr.append(
            {'singleConnection': True, 'name': 'frames', 'cast': True, 'datatype': 'string', 'required': True, 'height': 8, 'width': 12, 'shape': 'diamond', 'color': 'white'})
        self.inputPortsDescr.append(
            {'singleConnection': True, 'name': 'sample_rate', 'cast': True, 'datatype': 'None', 'required': True, 'height': 8, 'width': 12, 'shape': 'diamond', 'color': 'white'})
        self.inputPortsDescr.append(
            {'singleConnection': True, 'name': 'channels', 'cast': True, 'datatype': 'None', 'required': True, 'height': 8, 'width': 12, 'shape': 'diamond', 'color': 'white'})


    def beforeAddingToNetwork(self, net):
        try:
            ed = net.getEditor()
        except:
            import traceback; traceback.print_exc()
            print 'Warning! Could not import widgets'
