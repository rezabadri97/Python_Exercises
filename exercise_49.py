import clr
clr.AddReference('RevitAPI')
try:
    from Autodesk.Revit.DB import*
    objects={"walls":BuiltInCategory.OST.Walls, "Floors": BuiltInCategory.OST.Floors}
    for key,value in objects.items():
        object_found=FilteredElementCollector(doc).OfCategory(items).ToElements()
    print(f"Audit: Found {value.Count} {key} in the model.")
except Exception as e:
    print(e)