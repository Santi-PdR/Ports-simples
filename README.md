# Create Aeronautics / Sable — Forge 1.20.1

An unofficial source workspace for the Create Simulated suite on Minecraft
1.20.1 Forge, targeting Create 6.0.8. The workspace contains:

- `sable/`: Sable Forge port and its Rapier native physics layer.
- `simulated-project/`: Simulated, Create Aeronautics, and Offroad Forge ports.
- `simulated-project/aeronautics-bundled/`: combined distribution module for
  the three Create Simulated mods.

## Target versions

| Component | Version |
| --- | --- |
| Minecraft | 1.20.1 |
| Forge | 47.4.0 |
| Java | 17 |
| Create | 6.0.8 (`6.0.8-289`) |
| Flywheel | 1.0.5 |
| Ponder | 1.0.91 |
| Registrate | MC1.20-1.3.3 |
| Sable | 2.0.5-port.1 |
| Veil | 1.0.0.296 |

The full set of pinned compile/runtime dependencies is in
[`simulated-project/gradle.properties`](simulated-project/gradle.properties)
and [`sable/gradle.properties`](sable/gradle.properties).

## Build

Build the Sable Forge module first, then build the bundled Simulated Project.
The Aeronautics Gradle wrapper supplies the Gradle version used by both trees:

```bash
./simulated-project/gradlew -p sable :forge:build
SIMULATED_SABLE_JAR="$PWD/sable/forge/build/libs/sable-forge-1.20.1-2.0.5-port.1.jar" \
  ./simulated-project/gradlew -p simulated-project :aeronautics-bundled:build
```

Install the Sable JAR and the `create-aeronautics-bundled` JAR together. The
bundled JAR contains the `simulated`, `aeronautics`, and `offroad` mods; Sable
is a separate required mod. Also install Forge 47.4.0, Create 6.0.8, Veil
1.0.0.296, and the matching Create runtime dependencies listed above. Install
the same set on both client and server.

The individual Forge artifacts are also available from the `:simulated:forge`,
`:aeronautics:forge`, and `:offroad:forge` projects. Runtime testing must use
the dependency versions in the table above. The port remains experimental;
back up worlds before testing it in an existing modpack.

## Current validation

Both production artifacts compile on Java 17. The dedicated Forge GameTest
server also loaded Forge 47.4.0, Create 6.0.8, Sable and Rapier, then passed all
13 required tests. This validates the server-side load and those GameTest
scenarios; it does not certify every client renderer, shader, or modpack
combination. See [`BUILD_VALIDATION.md`](BUILD_VALIDATION.md) for artifact
paths and checksums.

## Compatibility notes

- Sable is an invasive physics and mixin library; review its upstream
  compatibility notes before adding optimization, renderer, or shader mods.
- The port baseline documents a known conflict with Immersive Optimization.
- Sable also documents conflicts with Radium, EntityCulling, and Chloride, and
  a Colorwheel issue when shader-enabled Flywheel instancing is active.
- Aeronautics includes Simulated and Offroad as companion content; use the
  bundled artifact when installing the full suite.
- This repository is an unofficial backport. Report port-specific problems
  here, and upstream-version problems to their respective upstream projects.

## Provenance and licensing

See [`PORTS_AND_LICENSES.md`](PORTS_AND_LICENSES.md) for source revisions,
attribution, retained license texts, and asset restrictions. This workspace is
not an official release of The Simulated Project or Sable.
