#!/usr/bin/env python

from os import path
import vtk

class Surface(object):

    def __init__(self):
        self.geometry = None

    def read(self, file_name):
        filename, file_extension = path.splitext(file_name)
        reader = vtk.vtkXMLPolyDataReader()
        reader.SetFileName(file_name)
        reader.Update()
        geometry = reader.GetOutput()
        self.geometry = geometry 

        #cleaner = vtk.vtkCleanPolyData()
        #cleaner.SetInputData(geometry);
        #cleaner.PieceInvariantOn();
        #cleaner.Update();
        #self.geometry = cleaner.GetOutput()
        #self.geometry.BuildLinks()


