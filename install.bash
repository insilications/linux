#!/usr/bin/env bash
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-dev-5.19.0-1903.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-abi-5.19.0-1903.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-cpio-5.19.0-1903.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-license-5.19.0-1903.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-extra-5.19.0-1903.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-5.19.0-1903.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-applications-5.19.0-1903.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
