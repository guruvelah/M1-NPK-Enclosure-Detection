# Raspberry Pi Camera Connection — M1

## Hardware
- Raspberry Pi with CSI camera interface
- Raspberry Pi Camera Module
- CSI ribbon cable
- 5V power supply
- microSD card with Raspberry Pi OS

## Connection
1. Power off the Raspberry Pi.
2. Insert the CSI ribbon cable into the camera connector with the contacts aligned correctly.
3. Connect the other end to the Raspberry Pi CSI camera connector.
4. Boot Raspberry Pi OS.
5. Verify the camera stack with:

```bash
rpicam-hello --timeout 5000
```

## Working capture
The project uses OpenCV after the camera is verified. Run:

```bash
python3 01_camera_and_repo/camera_test.py
```

Expected result:

```
CAMERA TEST: PASS
Resolution: 640x480
Channels: 3
```

The exact resolution printed by the script is the value actually returned by the connected camera; do not hard-code a different resolution in the final report.
