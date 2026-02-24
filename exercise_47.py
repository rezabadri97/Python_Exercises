import clr
try:
    # تمام کدهای زیر باید با یک Tab فاصله از لبه نوشته شوند
    collector = FilteredElementCollector(doc)
    windows = collector.OfCategory(BuiltInCategory.OST_Windows).ToElements()
    
    # چاپ خروجی با استفاده از .Count دات‌نتی
    print(f"Project Update: Total of {windows.Count} windows were collected for processing.")

except Exception as e:
    # این بخش هم‌تراز با try قرار می‌گیرد
    print(f"Failed to collect windows: {e}")