# This script represents storing values in a table.
import arcpy

# Define the workspace - adjust the path to your geodatabase or directory containing the output rasters
arcpy.env.workspace = r"D:\ENVT5571\Data\Project\MyProject10\Sensitive\Sensitive.gdb"

# Dynamically list all rasters produced by the sensitivity analysis
rasters = arcpy.ListRasters()

# Name of the table to store the results
output_table = "RasterStatistics"

# Create the output table if it does not exist
if not arcpy.Exists(output_table):
    arcpy.CreateTable_management(arcpy.env.workspace, output_table)

    # Add necessary fields
    arcpy.AddField_management(output_table, "Raster", "TEXT")
    arcpy.AddField_management(output_table, "Mean", "FLOAT")
    arcpy.AddField_management(output_table, "Minimum", "FLOAT")
    arcpy.AddField_management(output_table, "Maximum", "FLOAT")
    arcpy.AddField_management(output_table, "SD", "FLOAT")

def get_raster_stats(raster):
    mean = arcpy.GetRasterProperties_management(raster, "MEAN")
    minimum = arcpy.GetRasterProperties_management(raster, "MINIMUM")
    maximum = arcpy.GetRasterProperties_management(raster, "MAXIMUM")
    sd = arcpy.GetRasterProperties_management(raster, "STD")
    return [mean.getOutput(0), minimum.getOutput(0), maximum.getOutput(0), sd.getOutput(0)]

# Insert the statistics into the table
with arcpy.da.InsertCursor(output_table, ["Raster", "Mean", "Minimum", "Maximum", "SD"]) as cursor:
    for raster in rasters:
        stats = get_raster_stats(raster)
        row = (raster,) + tuple(stats)  # Create a tuple for the row
        cursor.insertRow(row)

print("Table filled with raster statistics.")
