import os

from PySide import QtGui, QtCore
import FreeCADGui as Gui
import FreeCAD as App
from FreeCAD import Console as FCC
import Spreadsheet

import zsToolsLib as zsToolsLib


class partInfo:
    def __init__(self):
        super(partInfo,self).__init__()

    def GetResources(self):
        return {"MenuText": "Create Part Info Attribute Group",
                "ToolTip": "Create a Part Info Attribute Group",
                "Pixmap" : os.path.join( zsToolsLib.iconPath , 'PartInfo.svg')
                }


    def IsActive(self):
        return len(Gui.Selection.getSelection()) > 0


    def Activated(self):
        # get the current active document to avoid errors if user changes tab
        self.doc = App.ActiveDocument

        for obj in Gui.Selection.getSelection():
            for info in zsToolsLib.partInfo:
                if not hasattr(obj,info):
                    obj.addProperty( 'App::PropertyString', info, 'PartInfo' )


# add the command to the workbench
Gui.addCommand( 'zsTools_partInfo', partInfo() )
