# lvm resize

```shell
sudo vgdisplay
sudo lvdisplay
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
df -h
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
df -h # check 
```

# add external disk 
```shell
sudo fdisk -l
sudo pvcreate /dev/sdb
sudo vgextend  ubuntu-vg  /dev/sdb
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
df -h
```