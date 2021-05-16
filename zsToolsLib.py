#!/usr/bin/env python3
# coding: utf-8
#
# zsTools Library
#



import os
wbPath   = os.path.dirname(__file__)
iconPath = os.path.join( wbPath, 'Resources/icons' )


# Types of datum objects
datumTypes = [  'PartDesign::CoordinateSystem', \
                'PartDesign::Plane',            \
                'PartDesign::Line',             \
                'PartDesign::Point']


containerTypes = [ 'App::Part', 'PartDesign::Body' ]

# Part Infos
partInfo = [ 'Material', \
             'Description' ]
