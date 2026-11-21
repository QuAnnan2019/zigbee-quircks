# Zigbee Quirks and Converters

[中文说明](README.zh-CN.md)

This repository contains maintained local integrations for Zigbee devices across:

- Home Assistant ZHA custom quirks
- Zigbee2MQTT external converters

Each integration is organized by platform, vendor, and device model. The repository
contains reviewed integration source code, rather than raw protocol notes,
experiments, deployment examples, or work-progress records.

## Planned Layout

```text
zha/<vendor>/<model>/
z2m/<vendor>/<model>/
```

Device-specific directories contain the implementation for the target platform.

## Scope

This repository stores integration source code only. Local protocol checklists,
captures, logs, deployment examples, experiments, and personal development progress
records remain outside this repository.
