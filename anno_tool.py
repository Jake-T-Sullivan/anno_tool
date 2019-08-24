import arcpy

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
df2 = arcpy.mapping.ListDataFrames(mxd)[1]
lyr = arcpy.mapping.ListLayers(df)[0]

wlist = ["HARNEY", "GRANT", "BAKER"]
vlist = ["1945", "1776", "1969"]


def get_well_term(lyr2, well_col, attrib_col):
    with arcpy.da.UpdateCursor(lyr2, "["+ +"]"")



def Replace_Text(lyr,well_list,value_list):
    with arcpy.da.UpdateCursor(lyr, ["TextString"]) as cursor:
        for well, value in zip(well_list, value_list):

            for row in cursor:
                new_text = well + "\r\n" + value
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
