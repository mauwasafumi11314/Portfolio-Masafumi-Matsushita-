# This script represents automation of sensitivity analysis
import arcpy
from arcpy.sa import Raster, RasterCalculator 
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")  
arcpy.env.workspace = r"D:\ENVT5571\Data\Project\MyProject10\Reclassfactors.gdb"  

# The DRASTIC model is a standardized system for evaluating groundwater pollution potential using hydrogeological settings 
# DRASTIC is an acronym for the seven parameters used in the model:

# - D: Depth to water
# - R: Net recharge
# - A: Aquifer media
# - S: Soil media
# - T: Topography (slope)
# - I: Impact of the vadose zone
# - C: Hydraulic conductivity of the aquifer

# This script performs a sensitivity analysis on DRASTIC/DRSDTICL model outputs by evaluating different scenarios, 
# such as minimum, mean, and maximum conditions of the model's input parameters. The analysis helps to understand 
# how land-use changes and other factors influence groundwater vulnerability assessments.

# Define parameters for the DRASTIC model under minimum conditions (without land use, focusing on intrinsic vulnerability)
DRASTICparameterMin = [
    'ReclassClip_Reclass_Reclass_GroundwaterMin2', 
    'ReclassClip_Reclass_Reclass_Slope_Srtm', 
    'ReclassClip_Reclass_Reclass_SoilMedia', 
    'ReclassClip_Reclass_Reclass_VadoseZone', 
    'Clip_Reclass_reclass_hydraulicConductivity2', 
    'Clip_Reclass_Reclass_AquiferMedia', 
    'ExtractByMask_Reclass_Reclass_Net_recharge_min2'
]

# Define parameters for the DRASTIC model under mean conditions (average scenarios, focusing on intrinsic vulnerability)
DRASTICparameterMean = [
    'ReclassClip_Reclass_GroundwaterMean2', 
    'ReclassClip_Reclass_Reclass_Slope_Srtm', 
    'ReclassClip_Reclass_Reclass_SoilMedia', 
    'ReclassClip_Reclass_Reclass_VadoseZone', 
    'Clip_Reclass_reclass_hydraulicConductivity2', 
    'Clip_Reclass_Reclass_AquiferMedia', 
    'ExtractByMask_Reclass_Reclass_Net_recharge_mean2'
]

# Note: The following parameter list is for DRASTICL under maximum conditions (likely duplicated by mistake; needs adjustment)
DRASTICLparameterMax = [
    "ReclassClip_Reclass_Reclass_GroundwaterMax2", 
    'ReclassClip_Reclass_Reclass_Slope_Srtm', 
    'ReclassClip_Reclass_Reclass_SoilMedia', 
    'ReclassClip_Reclass_Reclass_VadoseZone', 
    'Clip_Reclass_reclass_hydraulicConductivity2', 
    'Clip_Reclass_Reclass_AquiferMedia', 
    "ExtractByMask_Reclass_Reclass_Net_recharege_max2"
]

# Weights and Input names for the DRASTIC model (reduced model without land use)
Weight2 = [5, 1, 2, 5, 3, 3, 4]
Input_name2 = ["D", "T", "S", "I", "C", "A", "R"]

# Combine all parameter lists for iteration over different DRASTIC/L models and scenarios
DRASTICparameterList = [
    DRASTICLparameterMin, DRASTICLparameterMean, DRASTICLparameterMax, 
    DRASTICparameterMin, DRASTICparameterMean, DRASTICLparameterMax
]

# Define corresponding model names for each parameter set to keep track of different scenarios
DRASTICmodel = [
    "DRASTICLmodel_min", "DRASTICLmodel_mean", "DRASTICLmodel_max", 
    "DRASTICmodel_min", "DRASTICmodel_mean", "DRASTICmodel_max"
]

# Set the base path where output files will be saved
output_base_path = r"D:\ENVT5571\Data\Project\MyProject10\Sensitive\Sensitive.gdb"


# Iterate through each DRASTICL model and corresponding parameters to perform sensitivity analysis
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
# Iterate through each DRASTIC model and corresponding parameters to perform sensitivity analysis
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


