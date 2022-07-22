#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : linux
Version  : 5.19.0
Release  : 1906
URL      : file:///insilications/apps/linux-5.19.0.tar.gz
Source0  : file:///insilications/apps/linux-5.19.0.tar.gz
Source1  : config
Source2  : cmdline
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: init-rdahead-extras
Requires: systemd-bin
BuildRequires : asciidoc
BuildRequires : audit-dev
BuildRequires : babeltrace-dev
BuildRequires : bash
BuildRequires : bc
BuildRequires : binutils-dev
BuildRequires : binutils-staticdev
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-kernel
BuildRequires : docbook-xml
BuildRequires : elfutils
BuildRequires : elfutils-dev
BuildRequires : flex bison
BuildRequires : json-c
BuildRequires : json-c-dev
BuildRequires : kmod
BuildRequires : libcap
BuildRequires : libcap-dev
BuildRequires : libcap-ng
BuildRequires : libcap-ng-dev
BuildRequires : libunwind-dev
BuildRequires : libunwind-dev32
BuildRequires : libxml2-dev
BuildRequires : libxslt
BuildRequires : make
BuildRequires : ncurses-dev
BuildRequires : numactl-dev
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : pciutils
BuildRequires : pciutils-dev
BuildRequires : perl
BuildRequires : pypi(jinja2)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sphinx_rtd_theme)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : slang-dev
BuildRequires : util-linux
BuildRequires : xmlto
BuildRequires : xz-dev
BuildRequires : zlib-dev
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Linux kernel
============
There are several guides for kernel developers and users. These guides can
be rendered in a number of formats, like HTML and PDF. Please read

%prep
%setup -q -n linux-5.19.0
cd %{_builddir}/linux-5.19.0

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658498055
## altflags1f content
## altflags1
unset CFLAGS
unset CXXFLAGS
unset LDFLAGS
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe"
export KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe"
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/glibc-hwcaps/x86-64-v3:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/glibc-hwcaps/x86-64-v3:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1f end
## make_macro content
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

%define ktarget native
%define kversion %{version}-%{release}.%{ktarget}

BuildKernel() {
    Target=$1
    Arch=x86_64
    ExtraVer="-%{release}.${Target}"

    export V=2
    export AR=/usr/bin/gcc-ar
    export RANLIB=/usr/bin/gcc-ranlib
    export NM=/usr/bin/gcc-nm
    unset CFLAGS
    unset CXXFLAGS
    unset LDFLAGS
    export CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe"
    export KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe"

    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile

    make O=${Target} -s mrproper
    cp config ${Target}/.config

    make O=${Target} -s ARCH=${Arch} olddefconfig
    make O=${Target} ARCH=${Arch} V=2 KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" -j20
}

cp %{SOURCE1} .
BuildKernel %{ktarget}
## make_macro end


%install
export SOURCE_DATE_EPOCH=1658498055
rm -rf %{buildroot}
## altflags1f content
## altflags1
unset CFLAGS
unset CXXFLAGS
unset LDFLAGS
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe"
export KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe"
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/glibc-hwcaps/x86-64-v3:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/glibc-hwcaps/x86-64-v3:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1f end
## install_macro start
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

%define ktarget native
%define kversion %{version}-%{release}.%{ktarget}

InstallKernel() {
    Target=$1
    Kversion=$2
    Arch=x86_64
    KernelDir=%{buildroot}/usr/lib/kernel
    DevDir=%{buildroot}/usr/lib/modules/${Kversion}/build

    export V=2
    export AR=/usr/bin/gcc-ar
    export RANLIB=/usr/bin/gcc-ranlib
    export NM=/usr/bin/gcc-nm
    unset CFLAGS
    unset CXXFLAGS
    unset LDFLAGS
    export CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe"
    export KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe"

    mkdir   -p ${KernelDir}
    install -m 644 ${Target}/.config    ${KernelDir}/config-${Kversion}
    install -m 644 ${Target}/System.map ${KernelDir}/System.map-${Kversion}
    install -m 644 ${Target}/vmlinux    ${KernelDir}/vmlinux-${Kversion}
    install -m 644 %{SOURCE2}           ${KernelDir}/cmdline-${Kversion}
    cp  ${Target}/arch/x86/boot/bzImage ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}
    chmod 755 ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}

    mkdir -p %{buildroot}/usr/lib/modules
    make O=${Target} ARCH=${Arch} INSTALL_MOD_PATH=%{buildroot}/usr V=2 modules_install

    make O=${Target} ARCH=${Arch} CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" PREFIX=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} MANDIR=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 -j1 tools/acpi tools/acpi_install || :

    make O=${Target} ARCH=${Arch} CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" PREFIX=/usr WERROR=0 CONFDIR=/usr/share/cpupower INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} MANDIR=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 -j1 tools/cpupower tools/cpupower_install || :

    make O=${Target} ARCH=${Arch} CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" PREFIX=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} MANDIR=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 -C tools/ -j1 firmware || :
    install -m 755 tools/firmware/ihex2fw %{buildroot}/usr/bin/ || :

    make O=${Target} ARCH=${Arch} CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" PREFIX=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} MANDIR=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 -C tools/ -j1 intel-speed-select intel-speed-select_install || :

    make O=${Target} ARCH=${Arch} CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" PREFIX=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} MANDIR=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 -C tools/ -j1 objtool || :
    install -m 755 native/objtool/objtool %{buildroot}/usr/bin/ || :
    install -m 755 native/objtool/fixdep %{buildroot}/usr/bin/ || :
    install -m 755 native/objtool/libsubcmd.a %{buildroot}/usr/lib64/ || :

    make O=${Target} ARCH=${Arch} CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" PREFIX=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} MANDIR=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 -C tools/ -j1 pci pci_install || :

#     make O=${Target} ARCH=${Arch} PREFIX=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} MANDIR=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 -C tools/ -j1 bootconfig bootconfig_install || :

    make O=${Target} ARCH=${Arch} CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" PREFIX=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} MANDIR=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 -C tools/ -j1 spi spi_install || :

    make O=${Target} ARCH=${Arch} CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" PREFIX=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} MANDIR=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 -C tools/ -j1 tmon_install || :

    make O=${Target} ARCH=${Arch} CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" PREFIX=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} MANDIR=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 -C tools/ -j1 turbostat turbostat_install || :

    make O=${Target} ARCH=${Arch} CFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" KCFLAGS="-O2 -march=skylake -mtune=skylake -Wl,-O2 -falign-functions=32 -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -mno-avx2 -O0 -O2 -fno-tree-vectorize -mpopcnt -pipe" PREFIX=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} MANDIR=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 -C tools/ -j1 x86_energy_perf_policy_install || :

    rm -f %{buildroot}/usr/lib/modules/${Kversion}/build
    rm -f %{buildroot}/usr/lib/modules/${Kversion}/source

    mkdir -p ${DevDir}
    find . -type f -a '(' -name 'Makefile*' -o -name 'Kbuild*' -o -name 'Kconfig*' ')' -exec cp -t ${DevDir} --parents -pr {} +
    find . -type f -a '(' -name '*.sh' -o -name '*.pl' ')' -exec cp -t ${DevDir} --parents -pr {} +
    cp -t ${DevDir} -pr ${Target}/{Module.symvers,tools}
    ln -s ../../../kernel/config-${Kversion} ${DevDir}/.config
    ln -s ../../../kernel/System.map-${Kversion} ${DevDir}/System.map
    cp -t ${DevDir} --parents -pr arch/x86/include
    cp -t ${DevDir}/arch/x86/include -pr ${Target}/arch/x86/include/*
    cp -t ${DevDir}/include -pr include/*
    cp -t ${DevDir}/include -pr ${Target}/include/*
    cp -t ${DevDir} --parents -pr scripts/*
    cp -t ${DevDir}/scripts -pr ${Target}/scripts/*
    find  ${DevDir}/scripts -type f -name '*.[cho]' -exec rm -v {} +
    find  ${DevDir} -type f -name '*.cmd' -exec rm -v {} +
    # Cleanup any dangling links
    find ${DevDir} -type l -follow -exec rm -v {} +

    # Kernel default target link
    ln -s org.clearlinux.${Target}.%{version}-%{release} %{buildroot}/usr/lib/kernel/default-${Target}
}

# cpio file for keyboard drivers
createCPIO() {

    Target=$1
    Kversion=$2
    KernelDir=%{buildroot}/usr/lib/kernel
    ModDir=/usr/lib/modules/${Kversion}

    mkdir -p cpiofile${ModDir}/kernel/drivers/input/{serio,keyboard}
    mkdir -p cpiofile${ModDir}/kernel/drivers/hid
    cp %{buildroot}${ModDir}/kernel/drivers/input/serio/i8042.ko      cpiofile${ModDir}/kernel/drivers/input/serio || :
    cp %{buildroot}${ModDir}/kernel/drivers/input/serio/libps2.ko     cpiofile${ModDir}/kernel/drivers/input/serio || :
    cp %{buildroot}${ModDir}/kernel/drivers/input/keyboard/atkbd.ko   cpiofile${ModDir}/kernel/drivers/input/keyboard || :
    cp %{buildroot}${ModDir}/kernel/drivers/hid/hid-logitech-dj.ko    cpiofile${ModDir}/kernel/drivers/hid || :
    cp %{buildroot}${ModDir}/kernel/drivers/hid/hid-logitech-hidpp.ko cpiofile${ModDir}/kernel/drivers/hid || :
    cp %{buildroot}${ModDir}/kernel/drivers/hid/hid-apple.ko          cpiofile${ModDir}/kernel/drivers/hid || :
    cp %{buildroot}${ModDir}/modules.order   cpiofile${ModDir}
    cp %{buildroot}${ModDir}/modules.builtin cpiofile${ModDir}

    depmod -b cpiofile/usr ${Kversion}

    (
      cd cpiofile
      find . | cpio --create --format=newc \
        | xz --check=crc32 --lzma2=dict=512KiB > ${KernelDir}/initrd-org.clearlinux.${Target}.%{version}-%{release}
    )
}

InstallKernel %{ktarget} %{kversion}
createCPIO %{ktarget} %{kversion}

rm -rf %{buildroot}/usr/lib/firmware
mkdir -p %{buildroot}/usr/share/package-licenses/linux
cp COPYING %{buildroot}/usr/share/package-licenses/linux/COPYING
cp -a LICENSES/* %{buildroot}/usr/share/package-licenses/linux
## install_macro end
## start %find_lang macros
## end %find_lang macros

%files
%defattr(-,root,root,-)
