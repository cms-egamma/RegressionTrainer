#!/usr/bin/env python
"""
Thomas:
"""

########################################
# Imports
########################################

import os
import argparse
import pickle

import sys
sys.path.append('src')
from SlicePlot import SlicePlot

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gROOT.ProcessLine("gErrorIgnoreLevel = kError;")
ROOT.gStyle.SetOptStat(0)


########################################
# Main
########################################

def Plot():

    ########################################
    # Command line options
    ########################################

    parser = argparse.ArgumentParser()
    parser.add_argument( '--plotdir', type=str, help='Overwrites the default plot directory and uses this one' )
    parser.add_argument( '--fitfun', type=str, default='CB', choices=['CB', 'Gaus', 'Max'])
    parser.add_argument( 'picklefiles', metavar='N', type=str, nargs='+', help='Give a list of fitted pickle files to plot')
    parser.add_argument( '--compare', action='store_true', help='Compare the two given pickle files')
    parser.add_argument( '--override', action='store_true', help='Overrrides certain plot options (set in Plot.py)')
    args = parser.parse_args()    


    fit = 'CB'
    if args.fitfun == 'Gaus':
        fit = 'Gaus'
    elif args.fitfun == 'Max':
        fit = 'Max'
    else:
        fit = 'CB'

    
    ########################################
    # PLOTTING PROCEDURE
    ########################################    

    if not args.compare:

        for pickle_fn in args.picklefiles:

            if not os.path.isfile( pickle_fn ):
                print 'Error: Can not make plots because {0} does not exist'.format( pickle_fn )
                continue

            with open( pickle_fn, 'rb' ) as pickle_fp:
                sliceplot = pickle.load( pickle_fp )


            if args.override:
                #sliceplot.sliceplot_y_min = 0.905
                #sliceplot.sliceplot_y_min = 0.85
                sliceplot.sliceplot_y_min = 0.6
                #sliceplot.sliceplot_y_max = 1.095
                sliceplot.sliceplot_y_max = 1.2

                #sliceplot.sliceplotsigma_y_min   = 0.0005
                #sliceplot.sliceplotsigma_y_max   = 0.1005

                sliceplot.sliceplotsigma_y_min   = 0.0005
                sliceplot.sliceplotsigma_y_max   = 0.2



            if args.plotdir:
                sliceplot.plotdir = args.plotdir

            if not os.path.isdir( sliceplot.plotdir ): os.makedirs( sliceplot.plotdir )

            #sliceplot.MakePlots_standard()
            if fit=='Gaus':
                sliceplot.MakePlots_standard_Gaus()
            elif fit=='Max':
                sliceplot.MakePlots_standard_Max()

            else:
                sliceplot.MakePlots_standard()
            


    # Compare two fits
    elif args.compare:

        if not len(args.picklefiles)==2:
            print 'Only 2 picklefiles can be compared at a time!'
            return

        picklefile1 = args.picklefiles[0]
        picklefile2 = args.picklefiles[1]

        with open( picklefile1, 'rb' ) as pickle_fp:
            sliceplot1 = pickle.load( pickle_fp )
        with open( picklefile2, 'rb' ) as pickle_fp:
            sliceplot2 = pickle.load( pickle_fp )

        sliceplot1.MakePlots_comparison( sliceplot2 )

    pickle_fp.close()

########################################
# Functions
########################################


########################################
# End of Main
########################################
if __name__ == "__main__":
    Plot()
    print 'Everything DONE'
