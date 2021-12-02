#!/usr/bin/env bash
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-dev-5.14.0-666.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-abi-5.14.0-666.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-license-5.14.0-666.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-extra-5.14.0-666.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-5.14.0-666.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
rpm2cpio /aot/build/clearlinux/packages/linux/rpms/linux-applications-5.14.0-666.x86_64.rpm | (cd /; sudo cpio -i -d -u -v);
