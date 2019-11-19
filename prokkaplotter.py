#!/usr/bin/env python
# -*- coding: utf-8 -*-

# prokkaplotter.py

# Description
# > Command line program for generating plots from Prokka GFF files (from assemblies) using DnaFeaturesViewer

# %% Python Dependencies
import 	sys
import 	os
import 	re 
import 	argparse
import 	pandas as pd 
from 	dna_features_viewer import GraphicFeature, GraphicRecord, CircularGraphicRecord

# %% Argument Definitions
# > Construct the argument parser
ap 	= argparse.ArgumentParser(description = "Gene diagram creation from Prokka GFF files")
# > GFF File
ap.add_argument("-g", "--gffFile", action = "store", required = True, dest = "gffFile", type = str,
	help = "Prokka GFF file")
# > Output directory
ap.add_argument("-o", "--outdir", action = "store", required = True, dest = 'outdir', type = str,
	help = "Directory to output the gene diagrams")
## Optional Arguments
# > Node selection
ap.add_argument("-n","--nodes", action = "store", required = False, default = "all", dest = "nodeID", type = str,
	help = "Nodes to create diagrams for [default = all nodes]")
# > Linear / Circular plots
ap.add_argument("-f","--figtype", action = "store", required = False, default = "linear", dest = "figType", type = str,
	help = "Figure type of linear or circular [default = linear]")
# > Figure width
ap.add_argument("-w","--width", action = "store", required = False, default = 5, dest = "figWidth", type = int, 
	help = "Figure width in inches [default = 5]")
# > Figure height
ap.add_argument("-l","--height", action = "store", required = False, default = 5, dest = "figHeight", type = int, 
	help = "Figure height in inches [default = 5]")
# > Verbosity
ap.add_argument("-v","--verbosity", action = "store_true", required = False, default = False,
	help = "Display verbose output [default = False]")
## UPCOMING FEATURES
# > Custom features: Supply a CSV file with custom features to add into the GFF file
# ap.add_argument("-c","--custom", action = "store", required = False, default = None,
#	help = "Custom features to add to GFF file in CSV format")
# > Collect arguments
args = ap.parse_args()

# %% Function Definition
# > Parse Prokka GFF file
def gffParse(gffFile):
	# > Load gffFile
	gffFrame 	= pd.read_csv(gffFile, sep = 't', header = None, comment = '#')
	# > Name columns
	colNames 	= ['id','source','type','start','end','score','strand','frame','attribute'] 
	gffFrame.columns 	= colNames
	# > Extract genes only with information for plotting
	exFrame 	= gffFrame[['id','start','end','strand','attribute']][df['feature'] == 'gene']
	# > Return the frame
	return gffFrame