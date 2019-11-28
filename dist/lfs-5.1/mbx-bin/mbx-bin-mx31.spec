%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : MBX 3D driver and app
Name            : mbx-bin
Version         : 11.03.00
Release         : 1
License         : Proprietary
Vendor          : Freescale
Packager        : Yi Li
Group           : System/Servers
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build

%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}
cp -rf * $RPM_BUILD_ROOT/%{pfx}
pwd
ls

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(755,root,root)
%{pfx}/*
