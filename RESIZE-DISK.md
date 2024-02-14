# Resize vm virtualbox ubuntu

```shell
sudo vgdisplay ubuntu-vg
sudo lvextend -L +10G /dev/mapper/ubuntu--vg-ubuntu--lv
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
```
