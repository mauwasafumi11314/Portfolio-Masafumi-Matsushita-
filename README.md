# Python Code for Dissertation
This repository represents Python code scripts used for the dissertation project "Spatial Vulnerability Assessment of Groundwater Contamination in the Swan Coastal Plain, Perth, Western Australia"

# [Description](https://github.com/mauwasafumi11314/Python-Code-for-Dissertation/blob/main/Dissertation.pdf)
This study assesses groundwater vulnerability to nitrate and arsenic contamination in the Swan Coastal Plain, Western Australia, using the standardized models, DRASTIC and DRASTICL model, across three seasonal scenarios.

Environmental parameters were analyzed in ArcGIS, with the robustness of the models tested through map removal sensitivity analysis and validated using the Kendall rank coefficient test.

Findings indicated a significant correlation between the models and nitrate concentration. The risk classification maps revealed a linear trend between higher risk levels and samples exceeding nitrate concentration thresholds. The DRASTIC model showed promise in predicting areas vulnerable to nitrate contamination above 5 mg/L, 25 mg/L, and 50 mg/L.

The DRASTIC(L) model is a standardized system for evaluating groundwater pollution potential based on hydrogeological settings. DRASTIC is an acronym representing seven key parameters:

D: Depth to water
R: Net recharge
A: Aquifer media
S: Soil media
T: Topography (slope)
I: Impact of the vadose zone
C: Hydraulic conductivity of the aquifer
L: Land use

Python code scripts were used to automate the map removal sensitivity analysis and store the outputs in a table.


# [Automation of Sensitivity Analysis](https://github.com/mauwasafumi11314/Python-Code-for-Dissertation/blob/main/Python_Script1.py)
Sensitivity analysis evaluates how changes in each parameter affect the overall vulnerability index of the DRASTIC(L) models. For this study, map removal sensitivity analysis, as proposed by Lodwick et al. (1990), was conducted. The map removal sensitivity analysis was conducted using the following equation:

$$
S = \left(\frac{|V/N – V’/n|}{V}\right) \times 100
$$

where:
- \( V \) represents the unperturbed vulnerability index,
- \( V' \) denotes the vulnerability index with the targeted parameter removed,
- \( N \) and \( n \) are the numbers of parameters corresponding to \( V \) and \( V' \).


# [Storing Values in a Table.](https://github.com/mauwasafumi11314/Python-Code-for-Dissertation/blob/main/Python_Script2.py)
After conducting the sensitivity analysis, the statistical properties of the DRASTIC(L) models were systematically calculated. A script was then designed to automate the process of storing these statistical results into a table within a specified geodatabase.
