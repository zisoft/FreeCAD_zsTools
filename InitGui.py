###################################################################################
#
#  InitGui.py
#  
#  FreeCAD zsTools Workbench
#  Copyright (C) 2021 Mario Zimmermann
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#  USA  
#  
###################################################################################

import os

import zsToolsLib

global zsTools_icon
zsTools_path = os.path.dirname( zsToolsLib.__file__ )
zsTools_icon = os.path.join( zsTools_path , 'Resources/icons/zsToolsWorkbench.svg' )


""" Initialize the workbench """
class zsToolsWorkbench(Workbench):

    MenuText = "zsTools"
    ToolTip  = "zsTools workbench"
    Icon     = zsTools_icon

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

        import makeSpreadsheetCmd      # creates the parts list spreadsheet
        import partInfoCmd             # creates the partInfo attribute group
        import exportAllPagesPDFCmd    # exports all TechDraw pages to PDF
        import copyEditableFieldsCmd   # copy editable fields to subsequent pages


        # Commands to appear in the menu 'zsTools'
        self.appendMenu( "&zsTools", self.zsToolsMenuItems() )

        # Commands to appear in the toolbar
        self.appendToolbar( "zsTools", self.zsToolsToolbarItems() )

        FreeCAD.Console.PrintMessage(" done.\n")



    """ zsTools Menu & Toolbar """
    def zsToolsMenuItems(self):
        commandList = [ 
            "zsTools_partInfo",
            "zsTools_makeSpreadsheet",
            "Separator",
            "zsTools_exportAllPagesPDF",
            "zsTools_copyEditableFields"
        ]
        return commandList
        
    def zsToolsToolbarItems(self):
        commandList = [ 
            "zsTools_partInfo",
            "zsTools_makeSpreadsheet",
            "Separator",
            "zsTools_exportAllPagesPDF",
            "zsTools_copyEditableFields"
        ]
        return commandList

    
""" make the workbench """
wb = zsToolsWorkbench()
Gui.addWorkbench(wb)



