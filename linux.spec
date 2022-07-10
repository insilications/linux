#
# note to self: Linus releases need to be named 5.x.0 not 5.x or various
# things break
#
#

Name:           linux
Version:        5.19.0
Release:        1840
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        file:///insilications/apps/linux-5.19.0.tar.gz
Source1:        config
Source2:        cmdline

%define ktarget  native
%define kversion %{version}-%{release}.%{ktarget}

BuildRequires:  buildreq-kernel
BuildRequires:  bash
BuildRequires:  bc
BuildRequires:  binutils-dev
BuildRequires:  binutils-staticdev
BuildRequires:  elfutils
BuildRequires:  elfutils-dev
BuildRequires:  kmod
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-dev
BuildRequires:  flex bison
BuildRequires:  ncurses-dev
BuildRequires:  slang-dev
BuildRequires:  libunwind-dev
BuildRequires:  libunwind-dev32
BuildRequires:  zlib-dev
BuildRequires:  xz-dev
BuildRequires:  numactl-dev
BuildRequires:  perl
BuildRequires:  xmlto
BuildRequires:  asciidoc
BuildRequires:  util-linux
BuildRequires:  libxml2-dev
BuildRequires:  libxslt
BuildRequires:  docbook-xml
BuildRequires:  audit-dev
BuildRequires:  python3-dev
BuildRequires:  python3-staticdev
BuildRequires:  python3
BuildRequires:  babeltrace-dev
BuildRequires:  zstd-dev
BuildRequires:  libcap-dev
BuildRequires:  pciutils-dev
BuildRequires:  pciutils
BuildRequires:  libcap-ng
BuildRequires:  libcap-ng-dev
BuildRequires:  libcap-dev
BuildRequires:  libcap
BuildRequires:  json-c
BuildRequires:  json-c-dev

Requires: systemd-bin
Requires: init-rdahead-extras
Requires: linux-license = %{version}-%{release}

# don't strip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true


%description
The Linux kernel.

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel
Requires:       linux-license = %{version}-%{release}

%description extra
Linux kernel extra files

%package license
Summary: license components for the linux package.
Group: Default

%description license
license components for the linux package.

%package cpio
License:        GPL-2.0
Summary:        cpio file with kenrel modules
Group:          kernel

%description cpio
Creates a cpio file with some modules

%package applications
License:        GPL-2.0
Summary:        applications compiled by the kernel package
Group:          kernel

%description applications
Applications compiled by the kernel package

%package dev
License:        GPL-2.0
Summary:        The Linux kernel
Group:          kernel
Requires:       linux = %{version}-%{release}
Requires:       linux-extra = %{version}-%{release}
Requires:       linux-license = %{version}-%{release}

%description dev
Linux kernel build files

%prep
%setup -q -n linux-5.19.0

cp %{SOURCE1} .

%build
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
    export CFLAGS="-O2 -march=native -mtune=native -Wl,-O2 -falign-functions=32 -mno-vzeroupper -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe"
    export KCFLAGS="-O2 -march=native -mtune=native -Wl,-O2 -falign-functions=32 -mno-vzeroupper -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe"

    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile

    make O=${Target} -s mrproper
    cp config ${Target}/.config

    make O=${Target} -s ARCH=${Arch} olddefconfig
    make O=${Target} -s ARCH=${Arch} V=2 KCFLAGS="-O2 -march=native -mtune=native -Wl,-O2 -falign-functions=32 -mno-vzeroupper -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CONFIG_DEBUG_SECTION_MISMATCH=y -j16
}

BuildKernel %{ktarget}

%install

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
    export CFLAGS="-O2 -march=native -mtune=native -Wl,-O2 -falign-functions=32 -mno-vzeroupper -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe"
    export KCFLAGS="-O2 -march=native -mtune=native -Wl,-O2 -falign-functions=32 -mno-vzeroupper -mprefer-vector-width=256 -fuse-ld=bfd -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe"

    mkdir   -p ${KernelDir}
    install -m 644 ${Target}/.config    ${KernelDir}/config-${Kversion}
    install -m 644 ${Target}/System.map ${KernelDir}/System.map-${Kversion}
    install -m 644 ${Target}/vmlinux    ${KernelDir}/vmlinux-${Kversion}
    install -m 644 %{SOURCE2}           ${KernelDir}/cmdline-${Kversion}
    cp  ${Target}/arch/x86/boot/bzImage ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}
    chmod 755 ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}

    mkdir -p %{buildroot}/usr/lib/modules
    make O=${Target} -s ARCH=${Arch} INSTALL_MOD_PATH=%{buildroot}/usr V=2 modules_install

    make O=${Target} ARCH=${Arch} prefix=/usr WERROR=0 DESTDIR=%{buildroot} mandir=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 VERBOSE=1 KCFLAGS="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CXXFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" -j1 tools/acpi tools/acpi_install || :

    make O=${Target} ARCH=${Arch} prefix=/usr WERROR=0 confdir=/usr/share/cpupower DESTDIR=%{buildroot} mandir=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 VERBOSE=1 KCFLAGS="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CXXFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" -j1 tools/cpupower tools/cpupower_install || :

    make O=${Target} ARCH=${Arch} prefix=/usr WERROR=0 DESTDIR=%{buildroot} mandir=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 VERBOSE=1 KCFLAGS="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CXXFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" -C tools/ -j1 firmware || :
    install -m 755 tools/firmware/ihex2fw %{buildroot}/usr/bin/ || :

    make O=${Target} ARCH=${Arch} prefix=/usr WERROR=0 DESTDIR=%{buildroot} mandir=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 VERBOSE=1 -C tools/ -j1 intel-speed-select intel-speed-select_install || :

    make O=${Target} ARCH=${Arch} prefix=/usr WERROR=0 DESTDIR=%{buildroot} mandir=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 VERBOSE=1 -C tools/ -j1 objtool || :
    install -m 755 native/objtool/objtool %{buildroot}/usr/bin/ || :
    install -m 755 native/objtool/fixdep %{buildroot}/usr/bin/ || :
    install -m 755 native/objtool/libsubcmd.a %{buildroot}/usr/lib64/ || :

    make O=${Target} ARCH=${Arch} prefix=/usr WERROR=0 DESTDIR=%{buildroot} mandir=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 VERBOSE=1 KCFLAGS="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CXXFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" -C tools/ -j1 pci pci_install || :

#     make O=${Target} ARCH=${Arch} prefix=/usr WERROR=0 DESTDIR=%{buildroot} mandir=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 VERBOSE=1 -C tools/ -j1 bootconfig bootconfig_install || :

    make O=${Target} ARCH=${Arch} prefix=/usr WERROR=0 DESTDIR=%{buildroot} mandir=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 VERBOSE=1 KCFLAGS="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CXXFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" -C tools/ -j1 spi spi_install || :

    make O=${Target} ARCH=${Arch} prefix=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} mandir=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 VERBOSE=1 KCFLAGS="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CXXFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" -C tools/ -j1 tmon_install || :

    make O=${Target} ARCH=${Arch} prefix=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} mandir=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 VERBOSE=1 KCFLAGS="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CXXFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" -C tools/ -j1 turbostat turbostat_install || :

    make O=${Target} ARCH=${Arch} prefix=/usr WERROR=0 INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot} mandir=/usr/share/man PYTHON=/usr/bin/python3 PYTHON_CONFIG=/usr/bin/python3-config V=1 VERBOSE=1 KCFLAGS="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" CXXFLAGS+="-O2 -march=native -Wl,-O2 -falign-functions=32 -fdevirtualize-at-ltrans -fgraphite-identity -floop-nest-optimize -floop-block -ftree-loop-distribute-patterns -fno-tree-loop-vectorize -fuse-ld=bfd -fno-math-errno -fno-trapping-math -fno-semantic-interposition -fno-stack-protector -malign-data=cacheline -pipe" -C tools/ -j1 x86_energy_perf_policy_install || :

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
    cp %{buildroot}${ModDir}/kernel/drivers/input/serio/i8042.ko      cpiofile${ModDir}/kernel/drivers/input/serio
    cp %{buildroot}${ModDir}/kernel/drivers/input/serio/libps2.ko     cpiofile${ModDir}/kernel/drivers/input/serio
    cp %{buildroot}${ModDir}/kernel/drivers/input/keyboard/atkbd.ko   cpiofile${ModDir}/kernel/drivers/input/keyboard
    cp %{buildroot}${ModDir}/kernel/drivers/hid/hid-logitech-dj.ko    cpiofile${ModDir}/kernel/drivers/hid
    cp %{buildroot}${ModDir}/kernel/drivers/hid/hid-logitech-hidpp.ko cpiofile${ModDir}/kernel/drivers/hid
    cp %{buildroot}${ModDir}/kernel/drivers/hid/hid-apple.ko          cpiofile${ModDir}/kernel/drivers/hid
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

%files
%dir /usr/lib/kernel
%dir /usr/lib/modules/%{kversion}
/usr/lib/kernel/config-%{kversion}
/usr/lib/kernel/cmdline-%{kversion}
/usr/lib/kernel/org.clearlinux.%{ktarget}.%{version}-%{release}
/usr/lib/kernel/default-%{ktarget}
/usr/lib/modules/%{kversion}/kernel
/usr/lib/modules/%{kversion}/modules.*

%files extra
%dir /usr/lib/kernel
/usr/lib/kernel/System.map-%{kversion}
/usr/lib/kernel/vmlinux-%{kversion}

%files applications
/usr/bin
/usr/sbin
/usr/share
/usr/lib64
/usr/include

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/linux

%files cpio
/usr/lib/kernel/initrd-org.clearlinux.%{ktarget}.%{version}-%{release}

%files dev
%defattr(-,root,root)
/usr/lib/modules/%{kversion}/build
