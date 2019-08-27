from ij import IJ
from ij.plugin.frame import RoiManager
from ij.gui import Roi
from ij.gui import Overlay
from ij import ImagePlus
from ij.plugin import ChannelSplitter
from ij import measure
from ij.plugin.filter import Analyzer
from ij.measure import ResultsTable
from ij import WindowManager
from java.io import File

import os

import random
import datetime
#this function returns a string of all duplicates within an array. It only returns redundant values; if a list has two values that are the same, this returns only one of them.
def getDuplicates (an_array):
	#initialize an array to store values in.
	duplicates = []
	#iterates across the passed array, checking if an instance appears more than once.
	for x in an_array:
		if an_array.count(x) > 1:
			#if a duplicate is found, add it to the duplicates list and remove it from the original one.
			duplicates.append(x)
			an_array.remove(x)
	return duplicates

#This is a specific function for selecting only objects which are handdrawn unique cells (as opposed to rectangular ROIs and duplicates)
def uniqueCells(an_array):
	cells = []
	for item in an_array:
		#check if the items in the passed array are drawn
		if str(item.getClass()== "<type 'ij.gui.PolygonRoi'>":
			cells.append(item)
	#this call uses getDuplicates() as a cleaner, removing any duplicate values from the array without retaining them as a string. This ensures that if any overlays have accidentally been duplicated, the function will not run twice on them.
	getDuplicates(cells)
	return cells

def ROI_gen (file_path):
	# Global Variables 

	# This varible sets the width in pixels of the randomly placed ROIs. The height will be half of this value in pixels
	roi_width = 20
	# This variable sets the number of random ROIs to be generated
	num_roi = 20
	# Initializes roi_area as zero to be filled in later
	roi_area = 0
	# Initialises boolean that tracks weather the images have background spots
	has_background = False

	# Image opening
	imp = IJ.openImage(file_path)
	imp.show()
	
	# Initial image handling 
	
	# Saves the active image to the variable imp
	
	# Saves the title of the active image as title
	title = imp.getTitle()
	# Saves the overlay of the active image as ove
	ove = ImagePlus.getOverlay(imp)
	#Stores the overlay into an array file for iterating over
	ove_array = ove.toArray()
	#creates an array containing only one copy of each cell, excluding any duplicates or the background boxes. Do not create freehand background samples if you want this to work.
	unique_cells = uniqueCells(ove_array)
	
	######### Creating instances of ImageJ tools ##########

	# Activates/Opens an instance of the ROI manager and clears it
	rm = RoiManager.getInstance()
	if not rm:
	    rm = RoiManager()
	rm.reset()
	
	# Initializes a Results Table instance to interface with the results table and clears it
	rt = ResultsTable.getResultsTable();
	if (rt==None):
	    rt = ResultsTable();
	rt.reset()
	
	# Initializes an Analyzer for imp
	alz = Analyzer(imp)
	
	# Turns all measurments off
	alz.setMeasurement(1043199, False)
	# Sets Area measurement 
	alz.setMeasurement(1, True)
	# Sets Mean measurement 
	alz.setMeasurement(2, True)
	# Stes INTEGRATED_DENSITY measurement 
	alz.setMeasurement(32768, True)
	
	
	######### Maybe make a method to do this ##########
	######### Dealing with Background Spots ##########
	
	# Gets the total number of shapes in the overlay
	shapes_num = ove.size()
	# Initializes an empty list for storing dimensions of the shapes
	width_height = []

	
	
	# Gets size information from each shape in the overlay
	for cell in unique_cells:
		# Gets a bounding box for each shape
		box = Roi.getBounds(cell )
		# Multiplies the width and height values of that box
		active_wh = box.width*box.height
		# Stores the resulting value in the width_height list 
		width_height.append(active_wh)
		
	#create a list of all existing duplicates in width_height
	dupes_list = getDuplicates(width_height)
	# If there are duplicates, the program deals with the uniformly sized background spots
	if not len(dupes_list) == 0: 

		# Initializes a list for storing the background spots 
		background_spots = []
		
	
		# This segment of code finds the non-unique w*h area value
	
		# This will hold a set of prevously encountered w*h areas
		seen = set()
		# This variable will be set equal to the repeated w*h value once it is found
		repeat = 0
		# This loop checks each area value to see if it has been seen before. If it has it stores the value and terminates, otherwise it adds the value to the 'seen' set
		for area in width_height:
		    	if area in seen:
		        	repeat = area
		        	return
		        seen.add(area)
	
		# This loop adds all of the ROIs with the same repeated area to a list and then removes them from the overlay
		for i in range (0, len(width_height),1):
			if width_height[i] == repeat:
				background_spots.append(ove.get(i))
				ove.remove(i)
				# Sets the has_backgrouns boolean to true for later reference
				has_background = True
	
	
	######### Generating ROIs for each cell ##########
	
	# Should I make seperate files for each channel for background spots, whole cells, and subROIs? Probably... Interface with R? 
	# Should I append data together for all images in the same trial?

	# Initializes an array in which to store all of the cell outlines
	cells = []
	# Initializes an array in which to store final, approved ROIs 
	good_rois = []
	
	# Asks for the number of outlines still present in ove and sets this as the number of cells in the image
	num_cells = ove.size()
	# Makes a new empty overlay for array -> shape purposes 
	ove1 = Overlay()
	#turn the overlay into an iterable array
	oveArray = ove.toArray()
	#clean up the overlay array to ensure you only iterate over truly unique values of the cells
	unique_cells = uniqueCells(ove_array)
	# Master loop for looping through cells in the image
	for cell in unique_cells:
	
		# Saves an outline from the overlay as an ROI
		active_cell = cell
		# Adds the active cell to the cells array
		cells.append(active_cell)
		# Adds ROI active_cell to ROI manager
		rm.addRoi(active_cell)
		# Saves the bounding rectangle of the Roi as bound 
		bound = Roi.getBounds(active_cell)
		
		#!!!!!!!??????!!!!!!! PROBLEM AREA !!!!!!!???????!!!!!!!
		rm.setSelectedIndexes([0,1]) 
		rm.runCommand(imp, "Measure")
		rm.reset()
		# This retreives the area measurement of the cell and stores it as cell_area
		cell_area = rt.getValueAsDouble(0, 0)
		# Clears the results table
		rt.reset()
	
		# This variable keeps track of how many good ROIs have been found
		found_roi = 0
		# This variable keeps track of how many attempts have gone by without finding a good ROI
		tries = 0
	
		# Loop for generating many ROIs
		while (found_roi < num_roi and tries < 20):

			# This increases the tries count by one
			tries = tries + 1
			# Uses the cell ROI bounding box dimensions to get a 'good guess' putative roi placement
			rand_x = bound.x + random.randint(0,bound.width-(roi_width))
			rand_y = bound.y + random.randint(0,bound.height-(roi_width/2))
	
			# Creates new ROI based on the guess
			test_roi = Roi(rand_x, rand_y, roi_width, roi_width/2)
			# Adds the new ROI to an overlay
			ove1.add(test_roi)	
			# Pulls the ROI back out of the overlay as r3
			r3 = ove1.get(0)
			# Adds r3 to the ROI manager
			rm.addRoi(r3)
			# Clears ove1
			ove1.clear()
			
			 
			# This section checks if the random ROI falls entirely within the cell outline
		
			# If the roi_area variable had not been filled with a value yet, set it to the area of one rectangular ROI
			if roi_area == 0:
				rm.setSelectedIndexes([0])
				rm.runCommand(imp, "Measure")
				roi_area = rt.getValueAsDouble(0, 0)
				rt.reset()
			# Adds the active cell outline to the ROI manager  
			rm.addRoi(active_cell)

			#!!!!!!!??????!!!!!!! PROBLEM AREA !!!!!!!???????!!!!!!!
			rm.setSelectedIndexes([0,1]) 
			# Uses the ROI manager OR command to make a composit of the rectangular ROI and the cell outline
			rm.runCommand("OR")
			# Adds the composite as a new ROI to the ROI manager
			rm.runCommand("Add")
			# Selects the composite and measures it to get the area
			rm.runCommand(imp, "Measure")
			new_area = rt.getValueAsDouble(0, 0)
			
			rt.reset()
			rm.reset()
			
			# If the composite has the same area as the cell_area then the rectangular ROI is completely contained within the cell outline and is 'legal', thus we add it to the good_rois list
			
			
			if new_area == cell_area:
			 	good_rois.append(r3)
			 	# This increases the found_roi count by 1
			 	found_roi = found_roi + 1
			 	# This resets the tries counter after a new good roi is found
			 	tries = 0
			 	print "found_roi"
			 	print good_rois


	
	######### Measuring all ROIs and Saving results ##########

	# This splits the color channels in the image into the three componants and saves the result as a list of images
	imp_list = ChannelSplitter.split(imp)
	# This makes the channel of interest in the list visible
	imp_list[1].show()
	imp_list[2].show()

	
	# This block of code calculates background values
	if has_background == True:
		rm.clear()
		# Loop that adds all spots to the ROI manager
		for spot in background_spots:
			rm.addRoi(roi)
		# Make 1st channel active
		# Measure for the first channel
		# Initializes a variable for calculating the mean background in channel 1
		mean_ch1 = 0 
		# Get average of mean intensity for channel 1 background 
		for i in range (0,rt.size(),1): 
			mean_ch1 = mean_ch1 + rt.getValue("Mean",i)
		mean_ch1 = mean_ch1 / rt.size()
		rt.clear()
		# Make 2nd channel active
		# Measure for second channel
		# Initializes a variable for calculating the mean background in channel 2
		mean_ch2 = 0 
		# Get average of mean intensity for channel 2 background 
		for i in range (0,rt.size(),1): 
			mean_ch2 = mean_ch2 + rt.getValue("Mean",i)
		mean_ch2 = mean_ch2 / rt.size()
		rt.clear()
		rm.clear()
	
	# Adds all of the cell outlines to the ROI manager
	for cell in cells:
		rm.addRoi(cell)

	# This makes the first channel of interest in the list visible
	imp_list[1].show()

	# This measures all of the cells in this first channel

	if has_background == True:
		print "boo"
		# Loop that subtracts the appropriate background value 
		

	# This makes the second channel of interest in the list visible
	imp_list[2].show()

	# This measures all of the cells in the second channel


	
	 	


	# This region of the code extracts measurement information from the results table, formats it and saves it to an appropriately named file

	# This saves the whole results table directly as a text file
	rt.saveAs("C:\\Users\\Alexander Saunders\\Desktop\\Orp1 Images\\Results"+ time + "__" + title + "results.txt") 

	# This can write a formated sting to a text file if we want that instead 
	#output = open("C:\\Users\\xenon\\Desktop\\BioFinalP\\Results\\"+ time + "__" + title + "output.txt", "w+")
	#output.close()
	
	# This splits the color channels in the image into the three componants and saves the result as a list of images
	imp_list = ChannelSplitter.split(imp)

	# This makes the first image in the list visible
	imp_list[1].show()

	#!!!!!!!??????!!!!!!! Problem area !!!!!!!???????!!!!!!!
	# This attempts to make that image the temporarily active image (for measuring off of)
	WindowManager.setTempCurrentImage(imp_list[1])
	rm.runCommand(imp_list[1], "Measure")


	#Close image, clear things and return
	return

# Folder
# Make list of files
# Initialize files to append to 
# Loop to call ROI.gen


# Make the good ROIs list ordered 1)background 2)cells 3)rectangular ROIs
# Make all background spots exactly the same size

# Timestamp



# This segment of code retreives the current time and makes it into a string that can be added as a time stamp to the files generated in the program
now = str(datetime.datetime.now())
nnow = now.split(" ")
time = nnow[1]
time = time.replace(":",".")

#____________________INPUT FILEPATH of tiff library as you would navigate to it. Make sure you double slash all the slashes in the filepath______________________
folder ="C:\\Users\\Alexander Saunders\\Desktop\\Orp1 Images\\14B11SFT"
tifs = []
for file in os.listdir(folder):
    filename = file
    if filename.endswith(".tif"): 
    	fullpath = folder + "\\" + filename
        tifs.append(fullpath)
    else:
        continue
for x in tifs:
	ROI_gen(x)
	
