import subprocess
import gphoto2cffi as gp
import sys
import os
from cameras import cameras

cams = gp.list_cameras()
mappings = { c.status.eosserialnumber : c._usb_address for c in cams }

if len(sys.argv) > 1:
    print(mappings)
    exit()

for c in cams:
    c.config['settings']['capturetarget'].set('Memory card')


output = '#!/bin/bash\n'
output += 'dir=$(dirname "$0")\n'
for serial, address in mappings.items():
    output+= 'pushd "$dir/CM{}/"\n'.format(cameras[serial])
    output+= 'gphoto2 --capture-tethered --port "usb:{:03d},{:03d}" --keep-raw --force-overwrite&\n'.format(*address)
    output+= "popd\n"

for serial, cam in cameras.items():
    if serial not in mappings:
        output+= "# {} not found\n".format(serial)
        print("\033[91m{} (cam {}) not found\033[0m".format(serial, cam))

tether_exec = 'tether'
with open(tether_exec, 'w') as f:
    f.write(output)

os.chmod(tether_exec, 755)
