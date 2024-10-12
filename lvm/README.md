# lvm resize

```shell
sudo vgdisplay
sudo lvdisplay
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
df -h
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
```