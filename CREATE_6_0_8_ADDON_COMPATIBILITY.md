# Create 6.0.8 Add-on Compatibility Matrix

Research snapshot: 2026-10-23. Target: Minecraft 1.20.1, Forge 47.4.x, Java 17, Create mc1.20.1-6.0.8. Upstream release metadata establishes declared targets, not runtime compatibility in the complete Ghouls modpack.

| Add-on | Latest selected 1.20.1 Forge build | Create 6.0.8 evidence | Required dependency / caveat |
| --- | --- | --- | --- |
| Steam 'n' Rails | 1.7.3 | Upstream release name explicitly says Forge 1.20.1 C6; JAR accepts Create 6.0.7+. | Requires Create. |
| Crafts & Additions | 1.3.3 | Release notes say updated to Create 6.0.8; JAR accepts Create 6.0.3+. | Requires Create. |
| Enchantment Industry | 2.5.4b | Upstream release is explicitly for Create 6.0.8-291; JAR accepts Create 6.0.8 through <6.1.0. | Requires Create: Dragons Plus 1.11.9, itself explicitly for Create 6.0.8; both included. |
| Slice & Dice | 3.6.0 | Forge build exists for 1.20.1; JAR accepts Create 6.0.7+. | Farmer's Delight integration is optional; verify desired recipes against the installed Farmer's Delight version. |
| New Age | 1.2.0 | JAR accepts Create 6.0.8 through <6.1.0. | Botarium is required on 1.20.1; Botarium 2.3.4 Forge is included. |
| Diesel Generators | 1.3.12 | Official version metadata pins required Create to mc1.20.1-6.0.8; JAR accepts Create 6.0.7 through <6.1.0. | Requires Create. |
| Create Deco | 2.0.3 | The JAR's Forge metadata requires Create exactly 6.0.2. | Excluded: does not accept Create 6.0.8. Release notes saying “Create 6” are too broad to establish compatibility. |
| Create Aeronautics / Sable | No official 1.20.1 Forge release identified. | Official Aeronautics release targets 1.21.1 NeoForge. | Experimental backport remains separate and must retain its own license and asset boundaries. |

## Decision

Eight selected JARs have Forge metadata accepting Create 6.0.8; this includes required Create: Dragons Plus and Botarium dependencies. Create Deco is excluded because its declared Create dependency is the exact version 6.0.2. Do not force-load it or claim compatibility without a source-level fix and runtime validation. No compatibility patch is needed for the selected official JARs. The complete modpack is not runtime-certified by this metadata audit.

## Upstream evidence

- Create 6.0.8: https://modrinth.com/mod/create/version/8amzvn9x
- Steam 'n' Rails 1.7.3 C6: https://modrinth.com/mod/create-steam-n-rails/version/7Uk6lWkU
- Crafts & Additions 1.3.3: https://www.curseforge.com/minecraft/mc-mods/createaddition/files/7208610
- Enchantment Industry 2.5.4b: https://modrinth.com/mod/create-enchantment-industry/version/fs3kihCQ
- Create: Dragons Plus 1.11.9: https://modrinth.com/mod/create-dragons-plus/version/eMalpJtP
- Slice & Dice 3.6.0: https://modrinth.com/mod/slice-and-dice/version/KWLI8Ng7
- New Age 1.2.0: https://modrinth.com/mod/create-new-age/version/7vnwbouk
- Botarium 2.3.4: https://modrinth.com/mod/botarium/version/O7D6FTfW
- Diesel Generators 1.3.12: https://modrinth.com/mod/create-diesel-generators/version/DTQVvA5H
- Create Deco 2.0.3: https://modrinth.com/mod/create-deco/version/e9gaSRMd
- Aeronautics official compatibility: https://modrinth.com/modpack/create-aeronautics
- REA study: https://github.com/inematds/rea-engenharia-reversa
