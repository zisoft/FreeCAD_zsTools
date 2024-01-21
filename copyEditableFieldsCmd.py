###################################################################################
#
#  copyEditableFields.py
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

import os

import FreeCAD as App
import FreeCADGui as Gui

import zsToolsLib as zsToolsLib


class CopyEditableFields:

    def GetResources(self):
        return {
            "Pixmap" : os.path.join( zsToolsLib.iconPath , 'CopyFields.svg'),
            "MenuText": "TechDraw: Copy Editable Fields",
            "ToolTip": "TechDraw: Copy editable fields to subsequent pages"
        }


    def IsActive(self):
        return len(App.ActiveDocument.findObjects(Type="TechDraw::DrawPage")) > 0


    def Activated(self):
        # Get the current active document to avoid errors if user changes tab
        doc = App.ActiveDocument

        pages = doc.findObjects(Type="TechDraw::DrawPage")
        pageCount = len(pages)

        if pageCount == 0:
            # nothing to do
            return

        pages.sort(key = lambda p: p.Label)

        # Get the common edit field values from the first page
        template = pages[0].Template
        title  = template.getEditFieldContent("DRAWING_TITLE")
        date   = template.getEditFieldContent("DATE")
        author = template.getEditFieldContent("AUTHOR_NAME")
        email  = template.getEditFieldContent("FC-EMAIL")
        url    = template.getEditFieldContent("FC-URL")

        # Now set these parameter on all pages
        for (pagenum,page) in enumerate(pages):
            template = page.Template
            template.setEditFieldContent("DRAWING_TITLE", title)
            template.setEditFieldContent("DATE", date)
            template.setEditFieldContent("AUTHOR_NAME", author)
            template.setEditFieldContent("FC-EMAIL", email)
            template.setEditFieldContent("FC-URL", url)
            template.setEditFieldContent("SHEET", "%d / %d" % (pagenum+1, pageCount))



# add the command to the workbench
Gui.addCommand( 'zsTools_copyEditableFields', CopyEditableFields() )

