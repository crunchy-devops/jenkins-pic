# Add a device yo ubuntu LVM
```shell
lsblk  # check if the new device is attached
sudo lvmdiskscan # check lvm partition
sudo pvcreate /dev/sdc  # create physical volume (PV)
sudo lvdisplay # Check Logical Volume (LV)
sudo vgextend ubuntu-vg /dev/sdc  # use volume group name 
sudo lvm lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv # extend the Logical Volume 
sudo resize2fs -p /dev/mapper/ubuntu--vg-ubuntu--lv # One last command is needed so that the “df -h” output shows the correct size of your file system:
``` 

