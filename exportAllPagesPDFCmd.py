###################################################################################
#
#  exportAllPagesPDF.py
#  
#  FreeCAD zsTools Workbench
#  Copyright (C) 2024 Mario Zimmermann
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


import FreeCAD as App
import FreeCADGui as Gui
import TechDrawGui
import os

import zsToolsLib as zsToolsLib


class ExportAllPagesPDF:

    def GetResources(self):
        return {
            "Pixmap" : os.path.join( zsToolsLib.iconPath , 'ExportAllPagesPDF.svg'),
            "MenuText": "TechDraw: Export all pages to PDF",
            "ToolTip": "TechDraw: Export all pages to PDF"
        }


    def IsActive(self):
        return len(App.ActiveDocument.findObjects(Type="TechDraw::DrawPage")) > 0


    def Activated(self):
        # Get the current active document to avoid errors if user changes tab
        doc = App.ActiveDocument
        documentPath = os.path.dirname(doc.FileName)
        
        pages = doc.findObjects(Type="TechDraw::DrawPage")

        if len(pages) == 0:
            return

        pages.sort(key = lambda p: p.Label)

        for (pagenum,page) in enumerate(pages):
            filename = documentPath + "/page_%02d.pdf" % (pagenum + 1)

            visible = page.ViewObject.isVisible()

            if not visible:
                page.ViewObject.show()

            TechDrawGui.exportPageAsPdf(page, filename)

            if not visible:
                page.ViewObject.hide()



# add the command to the workbench
Gui.addCommand( 'zsTools_exportAllPagesPDF', ExportAllPagesPDF() )

