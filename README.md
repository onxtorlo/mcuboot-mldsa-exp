# mcuboot-mldsa-exp

Replacing the MCUboot image signature with ML-DSA on STM32F429I-DISC1.
This repo is the west manifest plus everything that is not MCUboot source
(app, board config, scripts, results). MCUboot changes live in the fork
[onxtorlo/mcuboot](https://github.com/onxtorlo/mcuboot), branch `sign-replace`.

| Component | Version |
|---|---|
| Zephyr | v4.4.2 |
| MCUboot | v2.4.0 (fork, `sign-replace`) |
| Zephyr SDK | 1.0.1 (`arm-zephyr-eabi`) |
| Python `cryptography` | 50.0.1 |
| OpenOCD | 0.12.0 |

## Workspace setup (WSL, once per PC)

```bash
west init -m https://github.com/onxtorlo/mcuboot-mldsa-exp ~/secureboot
cd ~/secureboot
python3 -m venv .venv && . .venv/bin/activate
pip install -U pip west
west update --narrow -o=--depth=1
pip install -r zephyr/scripts/requirements.txt
pip install -r bootloader/mcuboot/scripts/requirements.txt
pip install -U "cryptography>=50"
west zephyr-export
west sdk install --version 1.0.1 -t arm-zephyr-eabi

# MCUboot fork: full history + push remote + work branch
cd bootloader/mcuboot
git fetch --unshallow
git remote add origin git@github.com:onxtorlo/mcuboot.git
git fetch origin sign-replace && git checkout -B sign-replace origin/sign-replace
```

After `west update`, run `git checkout <branch>` again in `bootloader/mcuboot`
(west leaves it on a detached HEAD).

Signing keys are not committed. Generate one per PC:

```bash
python bootloader/mcuboot/scripts/imgtool.py keygen -k mcuboot-mldsa-exp/keys/rsa2048.pem -t rsa-2048
```

## Board

Attach the ST-Link to WSL (PowerShell): `usbipd attach --wsl --busid <busid>`.
Serial console: `minicom -D /dev/ttyACM0 -b 115200` (one reader at a time).

Flash layout (`boot_conf/stm32f429i_disc1.overlay`):

| Partition | Address | Size |
|---|---|---|
| mcuboot | 0x08000000 | 128 KB |
| slot0 | 0x08020000 | 768 KB |
| scratch | 0x080E0000 | 128 KB |
| storage | 0x08100000 | 128 KB |
| slot1 | 0x08120000 | 768 KB |

## Boot flow (run from `~/secureboot`)

```bash
S=mcuboot-mldsa-exp/scripts
$S/build_boot.sh rsa2048              # MCUboot with boot_conf/rsa2048.conf + keys/rsa2048.pem
$S/build_app.sh v1                    # apps/hello, prints "[v1] Hello World!"
$S/sign_app.sh rsa2048 v1 1.0.0
$S/flash.sh erase
$S/flash.sh boot rsa2048
$S/flash.sh slot0 build/hello_v1/hello_v1_rsa2048.bin

# Upgrade: v2 into slot1, swapped in on next boot
$S/build_app.sh v2
$S/sign_app.sh rsa2048 v2 2.0.0 upgrade
$S/flash.sh slot1 build/hello_v2/hello_v2_rsa2048_upgrade.bin

# Images that must be rejected (bad payload / bad signature / wrong key)
$S/make_bad_images.sh rsa2048 v1
```

`west flash` defaults to STM32CubeProgrammer; the scripts use `--runner openocd`.

## Checks done (RSA-2048)

| Case | Result |
|---|---|
| Signed v1 in slot0 | boots `[v1]` |
| Signed v2 in slot1 (upgrade) | swap-using-scratch, boots `[v2]` |
| 1 bit flipped in code | rejected |
| 1 bit flipped in signature | rejected |
| Signed with another key | rejected |
