# AUTOKALIDD

stuff for automating downloading and dding kali iso into a specific pendrive.
---

Check available disks using `fdisk -l`, extract `/dev/....` path.

Next, check it's serial number:

```
[root@titanium]# udevadm info -a --attribute-walk --root  /dev/sda | grep -i serial
    ATTRS{serial}=="013337XDXD133337"
    ATTRS{serial}=="0000:00:13.37"
[root@titanium]# 
```

put this value into udev rule:
```
SUBSYSTEM=="usb", ACTION=="add", ENV{DEVTYPE}=="usb_device", ATTR{serial}=="013337XDXD133337", RUN="/tmp/test.sh"

```

after this step you need to reload udev rules:
```
udevadm control --reload-rules
```





---
docs:
https://opensource.com/article/18/11/udev
