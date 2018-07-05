# Linux tips

[Specify filename for wget command](https://www.electrictoolbox.com/wget-save-different-filename/), simply use `-O` is enough.

[Power saving](http://askubuntu.com/questions/300953/how-can-i-improve-battery-life-on-my-laptop)

Learn how to write xorg.conf by hand, or use a UI to generate it.

Dual boot machine, diable the utc time in the linux.

[This is a dedicated article about linux display configuration](https://wiki.ubuntu.com/X/Troubleshooting/Resolution)

The connection to eduroam and hopkins.

Hopkins id for eduroam is wqiu7@jhu.edu

Install [Intel graphics for Linux](https://01.org/linuxgraphics) to support HDMI output

How to monitor CPU temp. watch -n 1 sensors

Update modules
http://askubuntu.com/questions/173721/how-do-i-update-my-nvidia-modules-after-updating-my-kernel

sudo dpkg-reconfigure nvidia-375

KDE, slow to boot and slow to shutdown
Unity, buggy and the display configuration is wrong.

I need the environment to be battery friendly, help me concentrate, maybe xubuntu is the best. But I am not sure.

https://www.ubuntu.com/download/desktop/create-a-usb-stick-on-windows

Compare the size of iso, xubuntu is the smallest, meaning a smaller footprint?

Install CUDA and CuDnn

How to release cuda memory??

[Bug of fcitx pinyin](http://askubuntu.com/questions/668269/fcitx-pinyin-input-menu-doesnt-appear)

[Fix linux sound problem](https://itsfoss.com/fix-sound-ubuntu-1304-quick-tip/)

Use UE4 to check whether the graphics card is running well.


Xconfig!!
Make the nvidia-prime is installed, otherwise the laptop display will be unusable.

```
# nvidia-xconfig: X configuration file generated by nvidia-xconfig
# nvidia-xconfig:  version 375.26  (buildmeister@swio-display-x86-rhel47-01)  Thu Dec  8 19:07:46 PST 2016

Section "ServerLayout"
    Identifier     "layout"
    Screen      0  "nvidia" 0 0
    Inactive       "intel"
    InputDevice    "Keyboard0" "CoreKeyboard"
    InputDevice    "Mouse0" "CorePointer"
EndSection

Section "InputDevice"
    # generated from default
    Identifier     "Keyboard0"
    Driver         "keyboard"
EndSection

Section "InputDevice"
    # generated from default
    Identifier     "Mouse0"
    Driver         "mouse"
    Option         "Protocol" "auto"
    Option         "Device" "/dev/psaux"
    Option         "Emulate3Buttons" "no"
    Option         "ZAxisMapping" "4 5"
EndSection

Section "Monitor"
    Identifier     "Monitor0"
    VendorName     "Unknown"
    ModelName      "Unknown"
    HorizSync       28.0 - 33.0
    VertRefresh     43.0 - 72.0
    Option         "DPMS"
EndSection

Section "Device"
    Identifier     "intel"
    Driver         "modesetting"
    Option         "AccelMethod" "None"
    BusID          "PCI:0@0:2:0"
EndSection

Section "Device"
    Identifier     "nvidia"
    Driver         "nvidia"
    BusID          "PCI:1@0:0:0"
EndSection

Section "Screen"
    Identifier     "intel"
    Device         "intel"
    Monitor        "Monitor0"
EndSection

Section "Screen"
    Identifier     "nvidia"
    Device         "nvidia"
    Monitor        "Monitor0"
    DefaultDepth    24
    Option         "AllowEmptyInitialConfiguration" "on"
    Option         "IgnoreDisplayDevices" "CRT"
    Option         "ConstrainCursor" "off"
    SubSection     "Display"
        Depth       24
        Modes      "nvidia-auto-select"
    EndSubSection
EndSection
```

The default configuration

