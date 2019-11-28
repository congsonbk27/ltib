# template = u-boot-common.tmpl

%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Universal Bootloader firmware
Name            : u-boot
Version         : 2009.08
Release         : imx_11.03.00
License         : GPL
Vendor          : Freescale
Packager        : MAD
Group           : Applications/System
Source          : %{name}-%{version}.tar.bz2
Source1         : %{name}-v%{version}-%{release}.tar.bz2
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

Open source u-boot v2009.08 version

%Prep
%setup

# A single bz2 file contains all the patches and a series file.
tar jxvf %{SOURCE1}

chmod 755 patches/patch-uboot.sh
./patches/patch-uboot.sh


%Build
: ${PKG_U_BOOT_CONFIG_TYPE:?must be set, e.g. MPC8548CDS_config}
PKG_U_BOOT_PATH_PRECONFIG=$(eval echo $PKG_U_BOOT_PATH_PRECONFIG)
SRC_DIR=${PKG_U_BOOT_PATH_PRECONFIG:-%{_builddir}/%{buildsubdir}}
%{!?showsrcpath: %define showsrcpath 0}
%if %{showsrcpath}
%{echo:%(eval echo ${PKG_U_BOOT_PATH_PRECONFIG:-%{_builddir}/%{buildsubdir}})}
%endif

BUILD_DIR=%{_builddir}/%{buildsubdir}
if [ $SRC_DIR != $BUILD_DIR ]
then
    mkdir -p $BUILD_DIR
fi
cd $SRC_DIR
if [ -n "$LTIB_FULL_REBUILD" ]
then
    make HOSTCC="$BUILDCC" CROSS_COMPILE=$TOOLCHAIN_PREFIX O=$BUILD_DIR distclean
fi
make HOSTCC="$BUILDCC" CROSS_COMPILE=$TOOLCHAIN_PREFIX O=$BUILD_DIR $PKG_U_BOOT_CONFIG_TYPE
make HOSTCC="$BUILDCC" HOSTSTRIP="$BUILDSTRIP" \
     CROSS_COMPILE=$TOOLCHAIN_PREFIX $PKG_U_BOOT_BUILD_ARGS \
     O=$BUILD_DIR all

%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}/boot
BUILD_DIR=%{_builddir}/%{buildsubdir}
cd $BUILD_DIR
for i in u-boot.bin u-boot
do
    cp $i $RPM_BUILD_ROOT/%{pfx}/boot
done

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
