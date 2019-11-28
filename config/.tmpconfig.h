/*
 * Automatically generated C config: don't edit
 * LTIB version: 8.1.2
 */
#define AUTOCONF_INCLUDED
#define CONFIG_CONFIG_TITLE "Freescale i.MX development platforms"

/*
 * Choose the platform type
 */
#undef CONFIG_PCF_PLATFORM_IMX25_3STACK
#undef CONFIG_PCF_PLATFORM_IMX233
#undef CONFIG_PCF_PLATFORM_IMX27ADS
#undef CONFIG_PCF_PLATFORM_IMX28
#undef CONFIG_PCF_PLATFORM_IMX31ADS
#undef CONFIG_PCF_PLATFORM_IMX31_3STACK
#undef CONFIG_PCF_PLATFORM_IMX35_3STACK
#undef CONFIG_PCF_PLATFORM_IMX37_3STACK
#define CONFIG_PCF_PLATFORM_IMX5 1
#define CONFIG_PLATFORM "imx51"

/*
 * Choose the packages profile
 */
#define CONFIG_PCF_NO_PROFILE 1
#undef CONFIG_PCF_MIN_PROFILE
#undef CONFIG_PCF_DEV_PROFILE
#undef CONFIG_PCF_MAX_PROFILE
#undef CONFIG_PCF_REL_GNOME_PROFILE
#undef CONFIG_PCF_UPDATER_PROFILE
#define CONFIG_PCF_PRECONFIG "imx51.cf"
#define CONFIG_PCF_PROFILE ""
#define CONFIG_PCF_KCONFIG "main.lkc"
#define CONFIG_ERASE_BLOCK_SIZE "64"
#define CONFIG_CAP_UCLIBC 1
#define CONFIG_CAP_GLIBC 1
#define CONFIG_CAP_LFS_5_1 1
#define CONFIG_CAP_HAS_MMU 1
#define CONFIG_CAP_HAS_SHARED 1
#define CONFIG_PKG_GCC_NAME "nobuild"
#define CONFIG_DISTRO "dist/lfs-5.1"
#define CONFIG_ENDIAN "little"
#define CONFIG_SYSCFG_TMPFS "tmpfs"
#define CONFIG_INITTAB_LINE "::respawn:-/sbin/getty -L console 0 screen"
#define CONFIG_UCLIBC_DYNAMIC_LINKER "/lib/ld-uClibc.so.0"
#define CONFIG_GLIBC_DYNAMIC_LINKER "/lib/ld.so.1"
#define CONFIG_SYSCFG_BAUD "115200"
#define CONFIG_SYSCFG_CONSOLEDEV "ttyS0"
#define CONFIG_SYSCFG_BOOTLOADER "u-boot"
#define CONFIG_U_BOOT_IMAGE_TYPE "ppc"
#define CONFIG_SYSCFG_RUNKERNELADDR "0x0"
#define CONFIG_SYSCFG_LOADKERNELADDR "0x800000"
#define CONFIG_SYSCFG_LOADDTBADDR "0x9F0000"
#define CONFIG_SYSCFG_LOADRAMADDR "0xB00000"
#define CONFIG_SYSCFG_CUTARG "zImage"
#define CONFIG_CAP_FSL_EXT 1
#define CONFIG_LTIB_RELEASE "8.1.2"
