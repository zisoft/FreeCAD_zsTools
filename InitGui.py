# -*- coding: utf-8 -*-
###################################################################################
#
#  InitGui.py
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
###################################################################################


import os

import zsToolsLib

global zsTools_icon
zsToolspath = os.path.dirname( zsToolsLib.__file__ )
zsTools_icon = os.path.join( zsToolspath , 'Resources/icons/FreeCAD.svg' )


"""
    Initialize the workbench
"""
class zsToolsWorkbench(Workbench):

    global zsTools_icon
    MenuText = "zsTools"
    ToolTip = "zsTools workbench"
    Icon = zsTools_icon

    def __init__(self):
        "This function is executed when FreeCAD starts"
        pass

    def Activated(self):
        "This function is executed when the workbench is activated"
        FreeCAD.Console.PrintMessage("Activating zsTools WorkBench\n")
        return

    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        selectionFilter.observerDisable()
        FreeCAD.Console.PrintMessage("Leaving zsTools WorkBench\n")
        return 

    def GetClassName(self): 
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"


    def Initialize(self):
        FreeCAD.Console.PrintMessage("zsTools WorkBench initializing...")
        FreeCADGui.updateGui()

        import makeSpreadsheetCmd  # creates the parts list


        # Define Menus
        # commands to appear in the menu 'zsTools'
        self.appendMenu( "&zsTools", self.zsToolsMenuItems() )

        # Define Toolbars
        # commands to appear in the toolbar
        self.appendToolbar( "zsTools", self.zsToolsToolbarItems() )

        FreeCAD.Console.PrintMessage(" done.\n")



    """
        zsTools Menu & Toolbar
    """
    def zsToolsMenuItems(self):
        commandList = [ 
            "zsTools_makeSpreadsheet"
        ]
        return commandList
        
    def zsToolsToolbarItems(self):
        commandList = [ 
            "zsTools_makeSpreadsheet"
        ]
        return commandList



    
"""
    make the workbench
"""
wb = zsToolsWorkbench()
Gui.addWorkbench(wb)



