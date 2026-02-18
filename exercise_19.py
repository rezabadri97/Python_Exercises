report_text="Project: Tower A\nTotal Area: 150.5 m2\nStatus: Approved"
with open("site_report.txt","w") as my_file:
    my_file.write(report_text)
print("File created successfuly")