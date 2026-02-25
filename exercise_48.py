import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*

try:
    target_category=BuiltInCategory.OST.Floors
    floor_list=FilteredElementCollector(doc).OfCategory(target_categoty).ToElements()
    print(f"Site Analysis: {floor_list.Count} floors detected in the project")
except Exception as e:
    print(f"{e}")