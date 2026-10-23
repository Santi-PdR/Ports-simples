# Create 6.0.8 Add-on Compatibility Matrix

Research snapshot: 2026-10-23. Target: Minecraft 1.20.1, Forge 47.4.x, Java 17, Create mc1.20.1-6.0.8. Upstream release metadata establishes declared targets, not runtime compatibility in the complete Ghouls modpack.

| Add-on | Latest selected 1.20.1 Forge build | Create 6.0.8 evidence | Required dependency / caveat |
| --- | --- | --- | --- |
| Steam 'n' Rails | 1.7.3 | Upstream release name explicitly says Forge 1.20.1 C6. | Requires Create. |
| Crafts & Additions | 1.3.3 | Release notes explicitly say updated to Create 6.0.8. | Requires Create. |
| Enchantment Industry | 2.5.4b | Upstream release is explicitly for Create 6.0.8-291. | Requires Create: Dragons Plus 1.11.9, itself explicitly for Create 6.0.8; include both. |
| Slice & Dice | 3.6.0 | Forge build exists for 1.20.1 and declares Create as required. | Farmer's Delight integration is optional; verify the desired recipes against the installed Farmer's Delight version. |
| New Age | 1.2.0 | Forge 1.20.1 release exists; project supports Create add-on integration. | Botarium is required on 1.20.1; include Botarium 2.3.4 Forge. |
| Diesel Generators | 1.3.12 | Official Modrinth version metadata pins required Create to mc1.20.1-6.0.8. | Requires Create. |
| Create Deco | 2.0.3 | Upstream release notes say updated to Create 6. | Reports exist for some Create 6.0.8 combinations; keep isolated until runtime tested. |
| Create Aeronautics / Sable | No official 1.20.1 Forge release identified. | Official Aeronautics release targets 1.21.1 NeoForge. | The experimental backport is a separate workstream and must retain its own license and asset boundaries. |

## Decision

The official 1.20.1 Forge builds above already target Create 6.0.8 either explicitly or through the upstream Create 6 release. No source fork is justified without a reproducible failure. Package the latest upstream JAR for each selected add-on, plus the two required libraries/add-ons listed above. Do not represent Create Deco or the full pack as runtime-certified until tested.

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
