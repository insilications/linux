#!/usr/bin/env bash
cat config | grep CONFIG_ACPI_TABLE_UPGRADE
cat config | grep CONFIG_FORTIFY_SOURCE
cat config | grep CONFIG_HARDENED_USERCOPY_FALLBACK
cat config | grep CONFIG_HARDENED_USERCOPY
cat config | grep CONFIG_HAVE_HARDENED_USERCOPY_ALLOCATOR
cat config | grep CONFIG_SLAB_FREELIST_RANDOM
cat config | grep CONFIG_SLAB_FREELIST_HARDENED
cat config | grep CONFIG_STACKPROTECTOR_STRONG
cat config | grep CONFIG_STACKPROTECTOR
cat config | grep CONFIG_HAVE_STACKPROTECTOR
cat config | grep CONFIG_CC_HAS_SANE_STACKPROTECTOR
cat config | grep CONFIG_RANDOMIZE_MEMORY
cat config | grep CONFIG_RANDOMIZE_BASE
cat config | grep CONFIG_PAGE_TABLE_ISOLATION
cat config | grep CONFIG_RETPOLINE
# cat config | grep CONFIG_DEBUG_FORCE_FUNCTION_ALIGN_32B
cat config | grep CONFIG_ZSWAP_DEFAULT_ON
cat config | grep CONFIG_ZSWAP
cat config | grep CONFIG_INTEL_TXT
cat config | grep CONFIG_MICROCODE
cat config | grep CONFIG_MICROCODE_INTEL
cat config | grep CONFIG_MICROCODE_AMD
cat config | grep CONFIG_MICROCODE_OLD_INTERFACE
cat config | grep CONFIG_X86_SMAP
cat config | grep CONFIG_X86_SGX
cat config | grep CONFIG_X86_INTEL_TSX_MODE_ON
cat config | grep CONFIG_X86_INTEL_TSX_MODE_AUTO
cat config | grep CONFIG_DEBUG_KERNEL
cat config | grep CONFIG_UNWINDER_ORC
cat config | grep CONFIG_PAGE_POISONING
cat config | grep CONFIG_DEBUG_NOTIFIERS
cat config | grep CONFIG_DEBUG_SG
cat config | grep CONFIG_SHUFFLE_PAGE_ALLOCATOR
cat config | grep CONFIG_REFCOUNT_FULL
cat config | grep CONFIG_VMAP_STACK
cat config | grep CONFIG_KSM
cat config | grep CONFIG_ZRAM_WRITEBACK
cat config | grep CONFIG_ZRAM
cat config | grep SCHED_STACK_END_CHECK
cat config | grep CONFIG_DYNAMIC_DEBUG
cat config | grep CONFIG_FRAME_POINTER
cat config | grep CONFIG_STACK_VALIDATION
cat config | grep CONFIG_STACKTRACE
cat config | grep CONFIG_EFI_TEST
cat config | grep CONFIG_DMI_SYSFS
cat config | grep CONFIG_CGROUP_FREEZER
cat config | grep CONFIG_FRAMEBUFFER_CONSOLE
cat config | grep CONFIG_EFI_STUB
cat config | grep CONFIG_EFI=
cat config | grep CONFIG_RELOCATABLE
cat config | grep CONFIG_EFIVAR_FS
cat config | grep CONFIG_EFI_VARS
