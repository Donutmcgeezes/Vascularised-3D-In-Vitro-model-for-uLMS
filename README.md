This is an archive of the code used to process raw z-stacks to get Length Density, Branchpoint Density, Endpoint-to-Branchpoint Ratio and Median Tortuosity metrics for 3D vasculature

1. Read VESNA processing>Instructions
2. Install VESNA plugin from this repository: https://github.com/scfischer/schuettler-et-al-2025
3. Place raw z-stacks in one folder and create an empty output folder
4. Run the SubtractBG_batch.ijm macro in Fiji/ImageJ. Follow the instructions in VESNA processing> Instructions
5. Use the the background subtracted z-stacks as the input to VESNA
6. Set the output folder to an empty folder
7. Input parameters for VESNA:
Min Brightness: 3
Max Brightness: 180
Gaussian Blur: 1.5
Size Threshold: 30
Max Filter Radius: 3
Min Filter Radius: 2
Length Threshold: 15
*Just tick all the checkboxes
8. Once done, VESNA will produce a bunch of .csv files in the specified output folder
9. Copy this output folder path and paste it into the file path field in the VESNA_summarise_plots.py file. The python files uses matplotlib.pyplot, numpy, pandas, os and math libraries. Install them before running the script
10. Output of the python script is a 'vesna_summary.csv' which has 1 row for each sample then 2 extra rows at the bottom which are just the MEAN and STANDARD DEVIATION.
