########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Friday 13 April 2007 12:48:35 
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
# $Header: /opt/cvs/python/packages/share1.5/Vision/doc/Examples/matplotlib/Figimage_net.py,v 1.4 2009/09/30 21:06:47 vareille Exp $
#
# $Id: Figimage_net.py,v 1.4 2009/09/30 21:06:47 vareille Exp $
#

from traceback import print_exc
## loading libraries ##
from Vision.matplotlibNodes import matplotliblib
masterNet.getEditor().addLibraryInstance(matplotliblib,"Vision.matplotlibNodes", "matplotliblib")

from Vision.StandardNodes import stdlib
masterNet.getEditor().addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

try:
    ## saving node Image.open(in1) ##
    from Vision.StandardNodes import Eval
    Image_open_in1__44 = Eval(constrkw = {}, name='Image.open(in1)', library=stdlib)
    masterNet.addNode(Image_open_in1__44,71,224)
    Image_open_in1__44.inputPortByName['command'].widget.set("Image.open(in1)", run=False)
    code = """def doit(self, command, in1):
    import Image
    if len(command) == 0:
        return
    else:
        if len(command)>15:
            self.rename(command[:15]+'...')
        else:
            self.rename(command)
        # in1 is known in the scope of the eval function
        result = eval(command)
        self.outputData(result=result)
"""
    Image_open_in1__44.configure(function=code)
    apply(Image_open_in1__44.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Eval named Image.open(in1) in network masterNet"
    print_exc()
    Image_open_in1__44=None

try:
    ## saving node File Browser ##
    from Vision.StandardNodes import FileBrowserNE
    File_Browser_45 = FileBrowserNE(constrkw = {}, name='File Browser', library=stdlib)
    masterNet.addNode(File_Browser_45,55,17)
    File_Browser_45.inputPortByName['filename'].widget.set("Data/lena.jpg", run=False)
    apply(File_Browser_45.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore FileBrowserNE named File Browser in network masterNet"
    print_exc()
    File_Browser_45=None

try:
    ## saving node Cast ##
    from Vision.StandardNodes import Cast
    Cast_46 = Cast(constrkw = {}, name='Cast', library=stdlib)
    masterNet.addNode(Cast_46,79,120)
    apply(Cast_46.inputPortByName['newtype'].widget.configure, (), {'choices': ('2Darray', 'MPLAxes', 'MPLDrawArea', 'MPLFigure', 'None', 'NumericArray', 'Old None', 'array', 'boolean', 'colorRGB', 'colorfloat3or4', 'colorsRGB', 'coord2', 'coord3', 'coordinates3D', 'dict', 'faceIndices', 'float', 'image', 'indice2', 'indice2+', 'indice3or4', 'instancemat', 'int', 'list', 'normal3', 'normals3D', 'str', 'string', 'tkcolor', 'triggerIn', 'triggerOut', 'tuple', 'vector')})
    Cast_46.inputPortByName['newtype'].widget.set("str", run=False)
    apply(Cast_46.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Cast named Cast in network masterNet"
    print_exc()
    Cast_46=None

try:
    ## saving node Figimage ##
    from Vision.matplotlibNodes import FigImageNE
    Figimage_47 = FigImageNE(constrkw = {}, name='Figimage', library=matplotliblib)
    masterNet.addNode(Figimage_47,145,337)
    Figimage_47.inputPortByName['origin'].widget.set("lower", run=False)
except:
    print "WARNING: failed to restore FigImageNE named Figimage in network masterNet"
    print_exc()
    Figimage_47=None

masterNet.freeze()

## saving connections for network Figimage ##
if File_Browser_45 is not None and Cast_46 is not None:
    try:
        masterNet.connectNodes(
            File_Browser_45, Cast_46, "filename", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between File_Browser_45 and Cast_46 in network masterNet"
if Cast_46 is not None and Image_open_in1__44 is not None:
    try:
        masterNet.connectNodes(
            Cast_46, Image_open_in1__44, "result", "in1", blocking=True)
    except:
        print "WARNING: failed to restore connection between Cast_46 and Image_open_in1__44 in network masterNet"
if Image_open_in1__44 is not None and Figimage_47 is not None:
    try:
        masterNet.connectNodes(
            Image_open_in1__44, Figimage_47, "result", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between Image_open_in1__44 and Figimage_47 in network masterNet"
masterNet.unfreeze()
#masterNet.run()
