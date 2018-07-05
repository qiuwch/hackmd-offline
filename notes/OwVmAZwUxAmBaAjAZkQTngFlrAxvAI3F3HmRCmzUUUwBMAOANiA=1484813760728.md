# Solve OS issues.
## Solve bluetooth issue of Linux

Useful commands `hcitool scan/lescan`, `bluetoothctl`. After successfuly connect through `bluetoothctl`, still no mouse input. [Use xinput](https://ubuntuforums.org/showthread.php?t=2142366) shows nothing useful. Another place to check input device is `cat proc/bus/input/devices`. After power off/on the mouse and reconnect the mouse, it can work fine.