from satpy import available_readers
from pyorbital.orbital import Orbital
from pyspectral import near_infrared_reflectance
import pprint
from satpy import Scene
import datetime
import os
import glob
from satpy.writers import compute_writer_results

start = datetime.datetime.now()
pprint.pprint(available_readers())
process_path = r"/media/knn/F/validation_2020/msg_rgb_data/extracted"
dates = list(set([f.split("_")[4][0:8] for f in glob.glob1(process_path, "*.nc")]))

for date_ in dates:
    # date_ = "20200220"
    hour_ = "1200"
    files = [os.path.join(process_path, row) for row in glob.glob1(process_path, "W_XX*" + date_ + hour_ + "*.nc")]
    print(date_, files)
    scn = Scene(reader="seviri_l1b_nc", filenames=files)
    pprint.pprint(scn.available_composite_names())
    scn.load(['natural_color', 'snow'], calibrations=['radiance'])
    # scn.show("natural_color")
    # scn.show("snow")
    # scn.show("natural_enh")
    if not os.path.exists(os.path.join(r"outputs", date_)):
        os.mkdir(os.path.join(r"outputs", date_))
    a = scn.save_datasets(
        filename='{name}_{start_time:%Y%m%d_%H%M%S}.png', base_dir=os.path.join(r"outputs", date_))
    # break
end = datetime.datetime.now()
print("Duration is : ", str(end - start))
