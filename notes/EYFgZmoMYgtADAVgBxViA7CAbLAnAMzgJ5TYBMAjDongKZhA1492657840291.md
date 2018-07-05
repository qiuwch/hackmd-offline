# Razer blade

http://askubuntu.com/questions/894785/sleep-issues-on-my-razer-blade-stealth-16-04-lts

➜  ~ cat /sys/power/image_size 
➜  ~ sudo fallocate -l 6665281536 /swapfile
➜  ~ sudo dpkg-reconfigure uswsusp    

sudo systemctl status, Check system status with this command
sudo xfce4-power-manager --dump    

https://wiki.archlinux.org/index.php/swap#Swap_file_creation
https://wiki.archlinux.org/index.php/Power_management/Suspend_and_hibernate#Hibernation

https://help.ubuntu.com/stable/ubuntu-help/power-hibernate.html
http://docs.xfce.org/xfce/xfce4-power-manager/faq#why_are_the_options_for_suspendhibernate_not_there_or_i_can_not_select_them

Make sure UUID is correct.

https://askubuntu.com/questions/794218/getting-killer-wireless-ac-1535-working-for-installing-ubuntu-16-04

https://wiki.archlinux.org/index.php/Dynamic_Kernel_Module_Support#Rebuild_modules

modinfo i915

The sleep and hibernate issue!!!!! Many hours wasted
https://www.reddit.com/r/razer/comments/5cxpx7/help_razer_blade_stealth_with_ubuntu_1604_suspend/
https://www.reddit.com/r/razer/comments/447vrn/razer_blade_stealth_linux/d4zfspx/