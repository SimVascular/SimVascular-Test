'''Test getting a model from the SV Data Manager.

   This is tested using the Demo Project.
'''
import sv
import vtk
  
## Get model object from the SV Data Manager 'Models/demo' node. 
#
model_name = "demo"
print("Get model: " + model_name)
model = sv.dmg.get_model(model_name)
print("Model type: " + str(type(model)))
face_ids = model.get_face_ids()
print("Model Face IDs: {0:s}".format(str(face_ids)))

model_polydata = model.get_polydata()
print("Model polydata: num nodes: {0:d}".format(model_polydata.GetNumberOfPoints()))
print("Model polydata: num polygons: {0:d}".format(model_polydata.GetNumberOfCells()))


