import arcpy

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyr = arcpy.mapping.ListLayers(df)[0]

wlist = [["HARNEY"], ["GRANT"], ["BAKER"]]
vlist = [["1945"], ["1776"], ["1969"]]

def Replace_Text(lyr,well_list,value_list):
    with arcpy.da.UpdateCursor(lyr, ["TextString"]) as cursor:
        for well, value in zip(well_list, value_list):
        
            new_text = ("""%s
%s""" %(well,value,))
            for row in cursor:
                if well in row[0]:
                
                    print("found IT!!!")
                    row[0] = new_text
                    print(row[0])
                    cursor.updateRow(row)
                    break                    
                else:
                
                    print(row[0])
                cursor.updateRow(row)
                
Replace_Text(lyr, wlist, vlist)
