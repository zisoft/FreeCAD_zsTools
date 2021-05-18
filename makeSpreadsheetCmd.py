# -*- coding: utf-8 -*-
###################################################################################
#
#  makeSpreadsheetCmd.py
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

import FreeCADGui as Gui
import FreeCAD as App
import Spreadsheet

import zsToolsLib

from collections import Counter


class makeSpreadsheet:

    def GetResources(self):
        return {
            "Pixmap" : os.path.join( zsToolsLib.iconPath , 'PartsList.svg'),
            "MenuText": "Create Part List Spreadsheet",
            "ToolTip": "Create a Part List Spreadsheet from the selected objects"
        }


    def IsActive(self):
        return len(Gui.Selection.getSelection()) > 0


    def Activated(self):
        # get the current active document to avoid errors if user changes tab
        self.doc = App.ActiveDocument

        self.objectList = Counter()

        for obj in Gui.Selection.getSelection():
            self.processParts(obj)

        # ---------------------------------------------------------------------------
        # Create the Spreadsheet
        self.sheet = self.doc.addObject("Spreadsheet::Sheet", "PartsList")
        self.sheet.Label = "PartsList"
        self.sheet.set('A1', 'Pos')
        self.sheet.set('B1', 'Count')
        self.sheet.set('C1', 'Name')
        self.sheet.set('D1', 'Material')
        self.sheet.set('E1', 'Description')
        self.sheet.set('F1', 'Length')
        self.sheet.set('G1', 'Width')
        self.sheet.set('H1', 'Height')

        self.sheet.setStyle('A1:H1', 'bold', 'add')

        rowNum = 1
        for name in self.objectList:
            obj = self.doc.getObject(name)

            sRowNum = str(rowNum+1)
            self.sheet.set('A' + sRowNum, str(rowNum))
            self.sheet.set('B' + sRowNum, str(self.objectList[name]))
            self.sheet.set('C' + sRowNum, obj.Label)

            if hasattr(obj,'Material') and obj.getGroupOfProperty('Material') == 'PartInfo':
                self.sheet.set('D' + sRowNum, obj.getPropertyByName('Material'))

            if hasattr(obj,'Description') and obj.getGroupOfProperty('Description') == 'PartInfo':
                self.sheet.set('E' + sRowNum, obj.getPropertyByName('Description'))
                
            if hasattr(obj,'Shape') and obj.Shape.BoundBox.isValid():
                bb = obj.Shape.BoundBox
                if abs(max(bb.XLength,bb.YLength,bb.ZLength)) < 1e+10:
                    Xsize = str(int((bb.XLength * 10)+0.099)/10)
                    Ysize = str(int((bb.YLength * 10)+0.099)/10)
                    Zsize = str(int((bb.ZLength * 10)+0.099)/10)
            self.sheet.set('F' + sRowNum, str(Xsize))
            self.sheet.set('G' + sRowNum, str(Ysize))
            self.sheet.set('H' + sRowNum, str(Zsize))

                

            rowNum += 1

        # Center columns A and B
        self.sheet.setAlignment('A1:B'+str(rowNum), 'center', 'keep')
        # ---------------------------------------------------------------------------

        self.sheet.recompute()
        self.doc.recompute()
        


    def processParts( self, obj ):

        # recursively add the subojects
        if obj.TypeId=='App::Part':
            self.objectList[obj.Name] += 1
            for objname in obj.getSubObjects():
                subobj = obj.Document.getObject( objname[0:-1] )
                self.processParts( subobj )

        # if its a link, look for the linked object
        elif obj.TypeId=='App::Link':
            self.processParts(obj.LinkedObject)

        elif obj.TypeId=='PartDesign::Body':
            self.objectList[obj.Name] += 1
        
        # everything else except datum objects
        elif obj.TypeId not in zsToolsLib.datumTypes:
            self.objectList[obj.Name] += 1

        return



# add the command to the workbench
Gui.addCommand( 'zsTools_makeSpreadsheet', makeSpreadsheet() )
