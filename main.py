from satpy import available_readers
from pyorbital.orbital import Orbital
from pyspectral import near_infrared_reflectance
import pprint
from satpy import Scene
import datetime
import os 
import glob 

start = datetime.datetime.now()

pprint.pprint(available_readers())


date_ = "20200218"
hour_ = "1200"
process_path = r"C:\Users\knn\Data\MSG"

files = [os.path.join(process_path, row) for row in glob.glob1(process_path, "W_XX*"+date_+hour_+"*.nc")]

print(files)
scn = Scene(reader="seviri_l1b_nc", filenames=files)
pprint.pprint(scn.available_composite_names())
scn.load(['natural_color'], calibrations=[ 'radiance'])
scn.show("natural_color")
# scn.load(['day_microphysics_winter'], calibrations=['radiance'])
# scn.show("day_microphysics_winter")

# scn.load(['realistic_colors'], calibrations=[ 'radiance'])
# scn.show("realistic_colors")

# end = datetime.datetime.now()
# print("Duration is : ", str(end-start))