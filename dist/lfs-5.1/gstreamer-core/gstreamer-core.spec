%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : GStreamer Core
Name            : gstreamer-core
Version         : 0.10.28
Release         : 2
License         : LGPL
Vendor          : Freescale Semiconductor
Packager        : Kurt Mahan, Dexter Ji
Group           : Applications/System
Source          : gstreamer-%{version}.tar.bz2
Patch1          : %{name}-0.10.12-relink.patch
Patch2          : gstreamer-%{version}-gstmfwbuffer_v3.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup -n gstreamer-%{version}
%patch1 -p1
%patch2 -p1


%Build
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} \
            --disable-valgrind --without-check NM=nm
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*.la" | xargs rm -f

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
