Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import arcpy
from arcpy.sa import Raster, RasterCalculator  # Make sure to import RasterCalculator
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")  # Ensure the Spatial Analyst extension is available
arcpy.env.workspace = r"D:\ENVT5571\Data\Project\MyProject10\Reclassfactors.gdb"  # Use straight quotes here

DRASTICLparameterMin = [ 'ReclassClip_Reclass_Reclass_GroundwaterMin2', 'ReclassClip_Reclass_Reclass_Landuse2', 'ReclassClip_Reclass_Reclass_Slope_Srtm', 'ReclassClip_Reclass_Reclass_SoilMedia', 'ReclassClip_Reclass_Reclass_VadoseZone', 'Clip_Reclass_reclass_hydraulicConductivity2', 'Clip_Reclass_Reclass_AquiferMedia', 'ExtractByMask_Reclass_Reclass_Net_recharge_min2']

DRASTICLparameterMean = [ 'ReclassClip_Reclass_GroundwaterMean2', 'ReclassClip_Reclass_Reclass_Landuse2', 'ReclassClip_Reclass_Reclass_Slope_Srtm', 'ReclassClip_Reclass_Reclass_SoilMedia', 'ReclassClip_Reclass_Reclass_VadoseZone', 'Clip_Reclass_reclass_hydraulicConductivity2', 'Clip_Reclass_Reclass_AquiferMedia', 'ExtractByMask_Reclass_Reclass_Net_recharge_mean2']

DRASTICLparameterMax = [ "ReclassClip_Reclass_Reclass_GroundwaterMax2", 'ReclassClip_Reclass_Reclass_Landuse2', 'ReclassClip_Reclass_Reclass_Slope_Srtm', 'ReclassClip_Reclass_Reclass_SoilMedia', 'ReclassClip_Reclass_Reclass_VadoseZone', 'Clip_Reclass_reclass_hydraulicConductivity2', 'Clip_Reclass_Reclass_AquiferMedia', "ExtractByMask_Reclass_Reclass_Net_recharege_max2"]

Weight = [5, 5, 1, 2, 5, 3, 3, 4]
Input_name = [“D”, “Lu”, “T”, “S”, “I”, “C”, “A”, “R”]

DRASTICparameterMin = [ 'ReclassClip_Reclass_Reclass_GroundwaterMin2', 'ReclassClip_Reclass_Reclass_Slope_Srtm', 'ReclassClip_Reclass_Reclass_SoilMedia', 'ReclassClip_Reclass_Reclass_VadoseZone', 'Clip_Reclass_reclass_hydraulicConductivity2', 'Clip_Reclass_Reclass_AquiferMedia', 'ExtractByMask_Reclass_Reclass_Net_recharge_min2']
DRASTICparameterMean = [ 'ReclassClip_Reclass_GroundwaterMean2', 'ReclassClip_Reclass_Reclass_Slope_Srtm', 'ReclassClip_Reclass_Reclass_SoilMedia', 'ReclassClip_Reclass_Reclass_VadoseZone', 'Clip_Reclass_reclass_hydraulicConductivity2', 'Clip_Reclass_Reclass_AquiferMedia', 'ExtractByMask_Reclass_Reclass_Net_recharge_mean2']

DRASTICLparameterMax = [ "ReclassClip_Reclass_Reclass_GroundwaterMax2", 'ReclassClip_Reclass_Reclass_Slope_Srtm', 'ReclassClip_Reclass_Reclass_SoilMedia', 'ReclassClip_Reclass_Reclass_VadoseZone', 'Clip_Reclass_reclass_hydraulicConductivity2', 'Clip_Reclass_Reclass_AquiferMedia', "ExtractByMask_Reclass_Reclass_Net_recharege_max2"]

Weight2 = [5, 1, 2, 5, 3, 3, 4]
Input_name2 = [“D”, “T”, “S”, “I”, “C”, “A”, “R”]

DRASTICparameterList = [DRASTICLparameterMin, DRASTICLparameterMean, DRASTICLparameterMax, DRASTICparameterMin, DRASTICparameterMean, DRASTICLparameterMax]

DRASTICmodel = ["DRASTICLmodel_min", "DRASTICLmodel_mean", "DRASTICLmodel_max","DRASTICmodel_min","DRASTICmodel_mean", "DRASTICmodel_max"]
output_base_path = r"D:\ENVT5571\Data\Project\MyProject10\Sensitive\Sensitive.gdb"

for DRASTICparameter, DRASTIC in zip(DRASTICparameterList, DRASTICmodel):
    if len(DRASTICparameter) == 8: 
        for i, (param, input, wei) in enumerate(zip(DRASTICparameter, Input_name, Weight)):
            input_names = [name for j, name in enumerate(Input_name) if j != i] 
            rasters = [param for j, param in enumerate(DRASTICparameter) if j != i] 
            weights = [wei for j, wei in enumerate(Weight) if j != i]
            expression = " + ".join([f"{input} * {weight}" for input, weight in zip(input_names, weights)])
            output_raster = RasterCalculator(rasters, input_names, expression)

            rasters2 = [DRASTIC, output_raster]
            input_names2 = ["y", "x"]  
            expression2 = f"( (y/8 -x/7)/y) *100"
            output_raster2 = RasterCalculator(rasters2, input_names2, expression2)
            out_abs = arcpy.sa.Abs(output_raster2)
            output_path = f"{output_base_path}\\remove_{DRASTIC}_{param.split('_')[-1]}"
            out_abs.save(output_path)
    else:
        for i, (param, input, wei) in enumerate(zip(DRASTICparameter, Input_name2, Weight2)):
            input_names = [name for j, name in enumerate(Input_name2) if j != i] 
            rasters = [param for j, param in enumerate(DRASTICparameter) if j != i] 
            weights = [wei for j, wei in enumerate(Weight2) if j != i]
            expression = " + ".join([f"{input} * {weight}" for input, weight in zip(input_names, weights)])
            output_raster = RasterCalculator(rasters, input_names, expression)

            rasters2 = [DRASTIC, output_raster]
            input_names2 = ["y", "x"]  
            expression2 = f"( (y/7 -x/6)/y) *100"
            output_raster2 = RasterCalculator(rasters2, input_names2, expression2)
            out_abs = arcpy.sa.Abs(output_raster2)
            output_path = f"{output_base_path}\\remove_{DRASTIC}_{param.split('_')[-1]}"
            out_abs.save(output_path)
Type "help", "copyright", "credits" or "license()" for more information.
SyntaxError: multiple statements found while compiling a single statement


Type "help", "copyright", "credits" or "license()" for more information.