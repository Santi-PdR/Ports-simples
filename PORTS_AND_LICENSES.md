# Port sources and notices

This repository combines two existing Forge 1.20.1 port baselines. It retains
their license files and attribution; local build scripts and integration work
must not remove those notices.

| Workspace | Source | Imported revision | Target |
| --- | --- | --- | --- |
| `simulated-project/` | [NotAsher999/Simulated-Project-1.20.1](https://github.com/NotAsher999/Simulated-Project-1.20.1) | `50c1a6ae9508b66142ac026cbf671de170dbfde1` | Forge 1.20.1, Create 6.0.8 |
| `sable/` | [NotAsher999/sable-1.20.1](https://github.com/NotAsher999/sable-1.20.1) | `e4d2ab3724a9f5820e758646447d3a571761db11` | Forge 1.20.1, Create 6.0.8 |

The Simulated Project source identifies its upstream baseline as commit
`4406c68ba0cdb5585a55edee69de2812f47416a1` of
[Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project).
The imported branch documents that its Forge port-specific work was AI-produced
and human-reviewed. This workspace's changes remain separately attributable.

## License boundaries

- Simulated Project code is MIT-licensed. Its `LICENSE.md` states that assets
  under `simulated-project/{aeronautics,simulated,offroad}/common/src/main/resources/assets/`
  are All Rights Reserved. The permission for those assets must cover inclusion
  in this public repository and any later binary distribution.
- Sable is under PolyForm Shield 1.0.0. Keep `sable/LICENSE.md`, the required
  notices, and `sable/THIRD_PARTY_NOTICES.md`. Distribution and derivative-work
  terms remain subject to that license and any separate permission obtained.
- Rapier and other bundled third-party material retain their notices in the
  relevant source tree. Check those notices before publishing binaries.

The user has represented that they hold the required permissions for this
port. This note records the source boundaries; it does not replace the license
texts or grant rights to downstream recipients.
