import subprocess
import gphoto2cffi as gp
import sys

cams = gp.list_cameras()

folders = ['A', 'B', 'C', 'D']
ports = [c._usb_address for c in cams]

if len(folders) != len(ports):
    print("Note: Camera mismatch, found {}, looking for {}".format(len(ports), len(folders)))

output = 'dir=$(dirname "$0")\n'
for folder, port in zip(folders, ports):
    output+= "pushd $dir/CM{}/\n".format(folder)
    output+= 'gphoto2 --capture-tethered --port "usb:{:03d},{:03d}" --keep-raw --force-overwrite&\n'.format(*port)
    output+= "popd\n"
    print("Folder {} being used for port {}".format(folder, port))


with open('tether', 'w') as f:
    f.write(output)
