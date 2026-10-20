# Build and runtime evidence

Validated from the `ports` branch on 2026-10-20 with Eclipse Temurin Java
17.0.20.1.

## Build commands and results

1. Sable:

   ```bash
   JAVA_HOME=/usr/lib/jvm/java-17-temurin-jdk \
     PATH=/usr/lib/jvm/java-17-temurin-jdk/bin:$PATH \
     ./simulated-project/gradlew -p sable --no-daemon :forge:build
   ```

   Result: `BUILD SUCCESSFUL`; Gradle completed `:forge:build` and
   `:forge:check`.

2. Create Simulated bundle, including Simulated, Aeronautics, and Offroad:

   ```bash
   JAVA_HOME=/usr/lib/jvm/java-17-temurin-jdk \
     PATH=/usr/lib/jvm/java-17-temurin-jdk/bin:$PATH \
     SIMULATED_SABLE_JAR="$PWD/sable/forge/build/libs/sable-forge-1.20.1-2.0.5-port.1.jar" \
     ./simulated-project/gradlew -p simulated-project --no-daemon \
       :aeronautics-bundled:build
   ```

   Result: `BUILD SUCCESSFUL` (52 Gradle tasks; 44 executed, 8 up-to-date).

3. Dedicated-server GameTests with the same Sable JAR:

   ```bash
   JAVA_HOME=/usr/lib/jvm/java-17-temurin-jdk \
     PATH=/usr/lib/jvm/java-17-temurin-jdk/bin:$PATH \
     ./simulated-project/gradlew -p simulated-project \
       -Psable_jar="$PWD/sable/forge/build/libs/sable-forge-1.20.1-2.0.5-port.1.jar" \
       --no-daemon :all-forge:runGameTest
   ```

   Result: Forge 47.4.0 loaded Minecraft 1.20.1, Create 6.0.8, Sable 2.0.5-port.1,
   Rapier, and the Simulated test namespace. The server reported **all 13
   required GameTests passed**. The tests exercised Sable's physics pipeline,
   server data, and sustained Aeronautics propeller / Offroad wheel motion.

## Produced artifacts

| Artifact | Size | SHA-256 |
| --- | ---: | --- |
| `sable/forge/build/libs/sable-forge-1.20.1-2.0.5-port.1.jar` | 13,476,546 bytes | `523dbdb250e446ea77f3f2649cb72c28128280228ff45bba80b4fa6a6d6ca963` |
| `simulated-project/aeronautics-bundled/build/libs/create-aeronautics-bundled-1.20.1-1.3.1-port.1.jar` | 35,076,942 bytes | `2c69662ff95c1f120e7968d4a59f87cb6e9543f4e8ae74a9314ef6def7bcfc06` |

The bundled JAR contains nested Forge mods for `aeronautics`, `simulated`, and
`offroad`. Its nested metadata requires Create 6.0.8 or newer; Sable's metadata
restricts Create to `[6.0.8,6.1.0)`. It also contains the expected class files,
assets, and data entries for each mod. Sable remains a separately installed
JAR; Veil 1.0.0.296 is an external required dependency.

## Limits observed

- Client rendering and shader combinations were not run in this build check.
- Compilation reported deprecation and Mixin annotation-processor warnings;
  they did not fail the build or the GameTests.
- The upstream port documentation lists incompatible optimization/rendering
  mods. Review the compatibility and license notes before deploying the suite
  in a larger modpack or distributing binaries.
