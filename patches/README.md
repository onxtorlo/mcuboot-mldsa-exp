# Local patches to west modules

Measurement hooks (`MEASD` lines, see MCUboot `CONFIG_BOOT_MEASURE_SIG_DETAIL` /
`CONFIG_BOOT_MEASURE_SIG_PRIMS`) inside library modules that west fetches unmodified.
They compile to nothing unless the build is MCUboot with `CONFIG_BOOT_MEASURE_TIMING`.

| patch | module (west path) | base commit |
|---|---|---|
| tf-psa-crypto_boot_measure.diff | modules/crypto/tf-psa-crypto | dc575a2 |
| mldsa-native_boot_measure.diff | modules/crypto/mldsa-native | 3fc1998 |

Apply after `west update` (from the workspace top, ~/secureboot):

    git -C modules/crypto/tf-psa-crypto apply ../../../mcuboot-mldsa-exp/patches/tf-psa-crypto_boot_measure.diff
    git -C modules/crypto/mldsa-native apply ../../../mcuboot-mldsa-exp/patches/mldsa-native_boot_measure.diff

Undo: `git -C <module> checkout -- . && git -C <module> clean -f`
(`west update` keeps local changes; results record them in meta.json as
`tf_psa_crypto` / `mldsa_native` with `dirty` and `diff_sha1`).
