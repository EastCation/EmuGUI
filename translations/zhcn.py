from translations.systemdefaultset import *


def translateMainCN(window):
    # Tab group 1
    window.tabWidget.setTabText(0, "主页")  # Main
    window.tabWidget.setTabText(1, "设置")  # Settings

    # Main tab
    window.pushButton_8.setText("创建新的虚拟机")  # New virtual machine
    window.pushButton_9.setText("启动虚拟机")  # Start virtual machine
    window.pushButton_10.setText("编辑选中的虚拟机")  # Edit selected virtual machine
    window.pushButton_11.setText("删除选中的虚拟机")  # Delete selected virtual machine
    window.pushButton_22.setText("导出选中的虚拟机")  # Export selected virtual machine
    window.pushButton_23.setText("导入现有的虚拟机")  # Import virtual machine

    # Settings tabs
    window.tabWidget_2.setTabText(0, "一般")  # General
    window.tabWidget_2.setTabText(3, "关于 EmuGUI")  # About EmuGUI

    # General tab
    window.label_15.setText("语言")  # Language
    window.pushButton_15.setText("应用")  # Apply

    # Combo box for languages
    i = 0

    while i < window.comboBox_4.count():
        sysDefSet("系统缺省", window.comboBox_4, i)  # System default

        i += 1

    # Combo box for themes
    i = 0

    while i < window.comboBox_5.count():
        sysDefSet("系统缺省", window.comboBox_5, i)  # System default

        i += 1

    # QEMU tab
    window.label.setText("qemu-img 路径")  # qemu-img 路径
    window.label_2.setText("qemu-system-i386 路径")  # qemu-system-i386 路径
    window.label_3.setText("qemu-system-x86_64 路径")  # qemu-system-x86_64 路径
    window.label_4.setText("qemu-system-ppc 路径")  # qemu-system-ppc 路径
    window.label_5.setText("qemu-system-mips64el 路径")  # qemu-system-mips64el 路径
    window.label_9.setText("qemu-system-aarch64 路径")  # qemu-system-aarch64 路径
    window.label_11.setText("qemu-system-arm 路径")  # qemu-system-arm 路径
    window.label_16.setText("qemu-system-ppc64 路径")  # qemu-system-ppc64 路径
    window.label_17.setText("qemu-system-mipsel 路径")  # qemu-system-mipsel 路径
    window.label_18.setText("qemu-system-mips 路径")  # qemu-system-mips 路径
    window.label_19.setText("qemu-system-mips64 路径")  # qemu-system-mips64 路径
    window.label_12.setText("qemu-system-sparc 路径")  # qemu-system-sparc 路径
    window.label_13.setText("qemu-system-sparc64 路径")  # qemu-system-sparc64 路径
    window.lbl_alpha.setText("qemu-system-alpha 路径")  # qemu-system-alpha 路径
    window.lbl_riscv32.setText("qemu-system-riscv32 路径")  # qemu-system-riscv32 路径
    window.lbl_riscv64.setText("qemu-system-riscv64 路径")  # qemu-system-riscv64 路径

    window.pushButton.setText("浏览")  # 浏览
    window.pushButton_2.setText("浏览")  # 浏览
    window.pushButton_3.setText("浏览")  # 浏览
    window.pushButton_4.setText("浏览")  # 浏览
    window.pushButton_5.setText("浏览")  # 浏览
    window.pushButton_7.setText("浏览")  # 浏览
    window.pushButton_12.setText("浏览")  # 浏览
    window.pushButton_16.setText("浏览")  # 浏览
    window.pushButton_17.setText("浏览")  # 浏览
    window.pushButton_18.setText("浏览")  # 浏览
    window.pushButton_19.setText("浏览")  # 浏览
    window.pushButton_13.setText("浏览")  # 浏览
    window.pushButton_14.setText("浏览")  # 浏览
    window.btn_alpha.setText("浏览")  # 浏览
    window.btn_riscv32.setText("浏览")  # 浏览
    window.btn_riscv64.setText("浏览")  # 浏览
    window.pushButton_6.setText("应用")  # Apply
    window.btn_apply_qemu2.setText("应用")  # Apply

    # About tab
    # label_7 = Built on Python and PyQt technology, licensed under GNU General Public License 3.0
    window.label_7.setText("使用Python和PyQt技术，基于GNU GPLv3许可证进行授权")

    window.label_10.setText(
        """
        WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.
        """
    )  # WARNING: This program comes with ABSOLUTELY NO WARRANTY under applicable law. Please see the GNU GPL license for details.

    window.label_14.setText("Banner made by Tech-FZ.")  # Banner made by (insert author of current banner here).

    window.label_21.setText("在社交媒体上的 EmuGUI (使用英语)")  # EmuGUI on social media (in English)


def translateNewVmCN(window):
    window.setWindowTitle("EmuGUI - 创建新的虚拟机")

    # First page
    window.lbl_vmname.setText("名称")  # Name
    window.lbl_arch.setText("架构")  # Architecture
    window.cb_arch.setPlaceholderText("请选择一个架构")  # Please choose an architecture

    window.btn_next1.setText("下一步 >")  # Next >
    window.btn_cancel1.setText("取消")  # Cancel

    # Second page
    window.lbl_machine.setText("机型")  # Machine
    window.lbl_cpu.setText("处理器")  # CPU
    window.lbl_ram.setText("内存（以MB为单位）")  # RAM in MB

    window.cb_machine.setPlaceholderText("请选择一款机型")  # Please select a machine
    window.cb_cpu.setPlaceholderText("请选择一款处理器")  # Please select a processor

    window.pb_prev2.setText("< 上一步")  # < Previous
    window.pb_next2.setText("下一步 >")  # Next >
    window.pb_cancel2.setText("取消")  # Cancel

    # Combo boxes on second page
    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "让QEMU自己决定")  # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "让QEMU自己决定")  # Let QEMU decide
            break

        i += 1

    # Third page
    window.lbl_vhdU.setText("VHD使用情况")  # VHD usage

    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdU.setItemText(i, "创建一个新的虚拟磁盘")  # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdU.setItemText(i, "添加一个现有的虚拟磁盘")  # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdU.count():
        if window.cb_vhdU.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdU.setItemText(i, "不要添加虚拟磁盘")  # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_vhdP.setText("VHD路径")  # VHD path
    window.lbl_vhdF.setText("VHD文件格式")  # VHD file format
    window.lbl_maxsize.setText("最大大小")  # Maximum size
    window.lbl_hddC.setText("硬盘控制器")  # HDD controller

    i = 0

    while i < window.cb_hddC.count():
        if window.cb_hddC.itemText(i) == "Let QEMU decide" or window.cb_hddC.itemText(i) == "QEMU überlassen":
            window.cb_hddC.setItemText(i, "让QEMU自己决定")  # Let QEMU decide
            break

        i += 1

    window.cb_vhdF.setPlaceholderText("(请选择一种文件格式)")  # (Please select a file format)

    window.btn_vhdP.setText("浏览")  # 浏览
    window.btn_prev3.setText("< 上一步")  # < Previous
    window.btn_next3.setText("下一步t >")  # Next >
    window.btn_cancel3.setText("取消")  # Cancel

    # Fourth page
    window.lbl_vga.setText("显卡")  # VGA
    window.lbl_net.setText("网卡")  # Network
    window.lbl_mouse.setText("鼠标")  # Mouse

    window.cb_vga.setPlaceholderText("(请选择一种图形适配器)")  # (Please select a graphics adapter)
    window.cb_net.setPlaceholderText("(请选择一种网卡)")  # (Please select a network adapter)

    window.btn_prev4.setText("< 上一步")  # < Previous
    window.btn_next4.setText("下一步 >")  # Next >
    window.btn_cancel4.setText("取消")  # Cancel

    # Fifth page
    window.lbl_biosLoc.setText(
        "外部固件文件（留空使用缺省固件）"
    )  # Location of external\nBIOS file (Leave\nempty to use the\ndefault BIOS)

    window.lbl_biosF.setText("外部固件文件")  # External BIOS file

    window.btn_biosF.setText("浏览")  # 浏览
    window.btn_prev5.setText("< 上一步")  # < Previous
    window.btn_next5.setText("下一步 >")  # Next >
    window.btn_cancel5.setText("取消")  # Cancel

    # Sixth page
    window.lbl_sound.setText("声卡")  # Sound card
    window.lbl_cores.setText("处理器核心数")  # CPU cores
    window.lbl_kbd.setText("键盘")  # Keyboard
    window.lbl_kbdlayout.setText("键盘格式")  # Keyboard layout

    window.btn_prev6.setText("< 上一步")  # < Previous
    window.btn_next6.setText("下一步 >")  # Next >
    window.btn_cancel6.setText("取消")  # Cancel

    # Seventh page
    window.lbl_kernel.setText("Linux 内核")  # Linux kernel
    window.lbl_initrd.setText("Linux 初始化内存盘")  # Linux initrd image
    window.lbl_cmd.setText("Linux cmd 命令")  # Linux cmd args

    window.btn_kernel.setText("浏览")  # 浏览
    window.btn_initrd.setText("浏览")  # 浏览
    window.btn_prev7.setText("< 上一步")  # < Previous
    window.btn_next7.setText("下一步 >")  # Next >
    window.btn_cancel7.setText("取消")  # Cancel

    # Eighth page
    window.lbl_accel.setText("加速")  # Acceleration
    window.lbl_cdc1.setText("光驱控制器1")  # CD controller 1
    window.lbl_cdc2.setText("光驱控制器2")  # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "让QEMU自己决定")  # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "让QEMU自己决定")  # Let QEMU decide
            break

        i += 1

    window.btn_prev8.setText("< 上一步")  # < Previous
    window.btn_next8.setText("下一步 >")  # Next >
    window.btn_cancel8.setText("取消")  # Cancel

    # Ninth page
    window.lbl_addargs.setText("附加参数 (如果需要)")  # Additional arguments (if needed)

    window.checkBox_2.setText(
        "我想安装Windows 2000\n(已弃用)")  # I want to install Windows 2000\n(depreciated)
    window.chb_usb.setText("添加USB支持")  # Add USB support

    window.btn_prev9.setText("< 上一步")  # < Previous
    window.btn_finish.setText("完成")  # Finish
    window.btn_cancel9.setText("取消")  # Cancel


def translateStartVmCN(window, vmname):
    window.setWindowTitle(f"EmuGUI - 启动 {vmname}")
    window.label_4.setText("日期与时间")  # Date & Time
    window.label_3.setText("引导设备")  # Boot from
    window.label_6.setText("TPM 路径 (仅Linux)")  # TPM path (Linux only)
    window.label_7.setText("从终端创建TPM")  # Create the TPM from the terminal!

    window.label_5.setText("""
    注意：如果虚拟机在五分钟内无法启动，你应该检查一下QEMU和虚拟机的设置
    """)  # Note: If the VM doesn't start within five minutes, then you should check the VM and QEMU settings.

    window.pushButton.setText("浏览")  # 浏览
    window.pushButton_2.setText("浏览")  # 浏览
    window.pushButton_6.setText("浏览")  # 浏览
    window.pushButton_5.setText("选择系统")  # Set to system
    window.pushButton_3.setText("启动虚拟机")  # Start VM
    window.pushButton_4.setText("取消")  # Cancel
    window.checkBox.setText("使用实时时钟选项")  # Use RTC option

    # Combo box for boot
    i = 0

    while i < window.comboBox.count():
        if window.comboBox.itemText(i) == "Let QEMU decide" or window.comboBox.itemText(i) == "QEMU überlassen":
            window.comboBox.setItemText(i, "让QEMU自己决定")  # Let QEMU decide
            break

        i += 1


def translateVmExistsCN(window):
    window.label.setText(
        "抱歉，已存在一个名字相同的虚拟机"
    )  # Sorry, but a VM with this name already exists.

    window.label_2.setText(
        "请考虑删除那个虚拟机或者换个名字"
    )  # Please consider either deleting that VM or thinking of a new name.

    window.pushButton.setText("确认")  # OK


def translateVhdExistsCN(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText(
        "抱歉，你要创建的硬盘已经创建"
    )  # Sorry, but the disk you want to create is already existant.

    window.label_2.setText("你打算覆盖还是保留它？")  # Do you want to keep or overwrite it?

    window.pushButton.setText("覆盖")  # Overwrite
    window.pushButton_2.setText("保留")  # Keep


def translateSettingsPendingCN(window):
    # The dialog which used to use this translation function is no longer in use.
    window.label.setText("你没有设置QEMU路径")
    window.label_2.setText("请在设置里设置路径，然后再试一次")

    window.pushButton.setText("OK")  # OK


def translateVmTooNewCN(window):
    window.label.setText(
        "这个虚拟机需要更新的EmuGUI才能运行. 请更新您的软件!"
    )  # This VM is made with a version of EmuGUI that is too new. Please use a later version!

    window.pushButton.setText("OK")  # OK


def translateQemuSysMissingCN(window, arch):
    window.label.setText(
        f"抱歉，EmuGUI还没有配置为使用\"qemu-system-{arch}\" \n但是此组件是虚拟机运行所必需的\n请转到设置/QEMU以解决此问题"
    )  # Sorry but EmuGUI is not configured for using \"qemu-system-{arch}\" yet.\nThis component however is necessary to start this virtual machine.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("OK")  # OK


def translateQemuImgMissingCN(window):
    window.label.setText(
        "抱歉，EmuGUI还未配置\"qemu-img\" \n但是此组件是编辑虚拟机硬盘所必需的\n请转到设置/QEMU已解决此问题."
    )  # Sorry but EmuGUI is not configured for using \"qemu-img\" yet.\nThis component however is necessary to create or edit virtual machines.\nPlease go to Settings/QEMU to solve this issue.

    window.pushButton.setText("确认")  # OK


def translateEditVMCN(window, vmname):
    window.setWindowTitle(f"EmuGUI - 编辑虚拟机 {vmname}")

    # Buttons on all tabs
    window.btn_cancel.setText("取消")  # Cancel
    window.btn_ok.setText("确认")  # OK

    # Tab names
    window.tabWidget.setTabText(0, "一般")  # General
    window.tabWidget.setTabText(1, "机器")  # Machine
    window.tabWidget.setTabText(2, "虚拟硬盘")  # Virtual hard disks
    window.tabWidget.setTabText(3, "外设")  # Peripherals
    window.tabWidget.setTabText(4, "固件")  # BIOS
    window.tabWidget.setTabText(6, "附加组件")  # Additional components

    # Translations for General tab
    window.lbl_name.setText("名称")  # Name
    window.lbl_arch.setText("架构")  # Architecture

    # Translations for Machine tab
    window.lbl_cpu.setText("处理器")  # CPU
    window.lbl_machine.setText("机型")  # Machine
    window.lbl_ram.setText("内存（以MB为单位）")  # RAM in MB

    i = 0

    while i < window.cb_cpu.count():
        if window.cb_cpu.itemText(i) == "Let QEMU decide" or window.cb_cpu.itemText(i) == "QEMU überlassen":
            window.cb_cpu.setItemText(i, "让QEMU自己决定")  # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_machine.count():
        if window.cb_machine.itemText(i) == "Let QEMU decide" or window.cb_machine.itemText(i) == "QEMU überlassen":
            window.cb_machine.setItemText(i, "让QEMU自己决定")  # Let QEMU decide
            break

        i += 1

    # Translations for VHD tab
    window.lbl_vhdu.setText("VHD 占用情况")  # VHD usage
    window.lbl_vhdp.setText("VHD 路径")  # VHD path
    window.lbl_vhdf.setText("VHD 文件格式")  # VHD file format
    window.lbl_maxsize.setText("最大容量")  # Maximum size
    window.btn_vhdp.setText("浏览")  # 浏览

    # Combobox for VHD usage
    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Create a new virtual hard drive":
            window.cb_vhdu.setItemText(i, "创建新的虚拟硬盘")  # Create a new virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Add an existing virtual hard drive":
            window.cb_vhdu.setItemText(i, "添加现有的虚拟硬盘")  # Add an existing virtual hard drive
            break

        i += 1

    i = 0

    while i < window.cb_vhdu.count():
        if window.cb_vhdu.itemText(i) == "Don't add a virtual hard drive":
            window.cb_vhdu.setItemText(i, "不要添加虚拟硬盘")  # Don't add a virtual hard drive
            break

        i += 1

    window.lbl_cdc1.setText("光驱控制器1")  # CD controller 1
    window.lbl_cdc2.setText("光驱控制器2")  # CD controller 2

    i = 0

    while i < window.cb_cdc1.count():
        if window.cb_cdc1.itemText(i) == "Let QEMU decide" or window.cb_cdc1.itemText(i) == "QEMU überlassen":
            window.cb_cdc1.setItemText(i, "让QEMU自己决定")  # Let QEMU decide
            break

        i += 1

    i = 0

    while i < window.cb_cdc2.count():
        if window.cb_cdc2.itemText(i) == "Let QEMU decide" or window.cb_cdc2.itemText(i) == "QEMU überlassen":
            window.cb_cdc2.setItemText(i, "让QEMU自己决定")  # Let QEMU decide
            break

        i += 1

    window.lbl_hddc.setText("硬盘控制器")  # HDD controller

    i = 0

    while i < window.cb_hddc.count():
        if window.cb_hddc.itemText(i) == "Let QEMU decide" or window.cb_hddc.itemText(i) == "QEMU überlassen":
            window.cb_hddc.setItemText(i, "让QEMU自己决定")  # Let QEMU decide
            break

        i += 1

    # Translations for Peripherals tab
    window.lbl_mouse.setText("鼠标类型")  # Mouse type
    window.lbl_kbdtype.setText("键盘类型")  # Keyboard type

    # Translations for BIOS tab
    # Location of external BIOS file (Leave empty to use the default BIOS)
    window.lbl_biosloc.setText("外部固件文件的路径(留空使用缺省固件)")
    window.lbl_biosf.setText("外部固件文件")  # External BIOS file
    window.btn_biosf.setText("浏览")  # 浏览

    # Translations for Linux tab
    window.lbl_kernel.setText("Linux 内核")  # Linux kernel
    window.lbl_initrd.setText("Linux 初始化内存盘")  # Linux initrd image
    window.lbl_cmd.setText("Linux cmd 命令")  # Linux cmd arguments
    window.btn_kernel.setText("浏览")  # 浏览
    window.btn_initrd.setText("浏览")  # 浏览

    # Translations for Additional components tab
    window.lbl_vga.setText("显卡")  # VGA
    window.lbl_net.setText("网卡")  # Network adapter
    window.lbl_sound.setText("声卡")  # Sound card
    window.lbl_addargs.setText("附加选项(如果需要的话)")  # Additional arguments (if necessary)
    window.lbl_cpuc.setText("处理器核心数")  # CPU cores
    window.chb_usb.setText("添加USB支持")  # Add USB support
    window.lbl_accel.setText("加速")  # Acceleration


def translateErrDialogCN(window, errcode):
    window.setWindowTitle(f"EmuGUI - 错误")

    if errcode.startswith("C"):
        window.label.setText(
            "EmuGUI遇到一个严重错误，需要关闭。")  # EmuGUI encountered a critical error and needs to be closed.

    elif errcode.startswith("E"):
        window.label.setText("EmuGUI 遇到了严重错误")  # EmuGUI encountered an error.

    elif errcode.startswith("W"):
        window.label.setText("EmuGUI 对你发出了警告")  # EmuGUI has to warn you.

    else:
        window.label.setText("EmuGUI 有一些事情对你说")  # EmuGUI has something to say.

    window.label_2.setText("错误码: " + errcode)  # Error Code:

    window.label_3.setText(
        "如果多次出现此错误，请联系管理员和/或在EmuGUI Discord服务器或其GitHub存储库上寻求帮助。"
    )  # If this error occurs multiple times, contact your administrator and/or ask for help on the EmuGUI Discord Server or on its GitHub repository.

    window.pushButton.setText("OK")  # OK