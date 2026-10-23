# Create 6.0.8 Add-on Compatibility Matrix

Research snapshot: 2026-10-23. Target: Minecraft 1.20.1, Forge 47.4.x, Java 17, Create 6.0.8. This matrix records upstream releases; runtime compatibility in the full modpack is not implied unless stated.

| Add-on | Current target build | Create 6.0.8 evidence | Dependency / caveat |
| --- | --- | --- | --- |
| Steam 'n' Rails | 1.7.3 Forge 1.20.1 | Upstream labels the Forge file C6. | Requires Create; keep the exact Forge artifact, not Fabric. |
| Crafts & Additions | 1.3.3 Forge 1.20.1 | Release notes say updated to Create 6.0.8. | Electricity and kinetic-power content. |
| Enchantment Industry | 1.4.1 Forge 1.20.1 | Dedicated upstream release for Create 1.20.1-6.0.8. | Use the Forge release; later 2.x builds target a different branch/runtime. |
| Slice & Dice | 3.6.0 Forge 1.20.1 | Current Forge release exists for 1.20.1. | Recipe behavior should be checked with Farmer's Delight and this pack's Create build. |
| New Age | 1.2.0 Forge 1.20.1 | Current Forge release exists for 1.20.1. | Botarium is required on 1.20.1; its release page does not state a Create version pin. |
| Diesel Generators | 1.3.12 Forge 1.20.1 | Official version metadata requires Create mc1.20.1-6.0.8. | Runtime still needs checking alongside the selected add-ons. |
| Create Deco | 2.0.3 Forge 1.20.1 | Release notes say it was updated to Create 6. | Reports exist for some Create 6.0.8 combinations; isolate before combining with the pack. |
| Create Aeronautics / Sable | No official Forge 1.20.1 release identified. | Official Create Aeronautics distribution targets 1.21.1 NeoForge. | Keep the existing experimental backport isolated in its own workstream and honor its asset/license boundaries. |

## Interpretation

Most requested add-ons already publish 1.20.1 Forge artifacts targeting Create 6.0.8. Rebuilding or patching them without a demonstrated incompatibility would fork working code unnecessarily. The remaining work is dependency resolution and a combined runtime matrix; modify an add-on only after a reproducible failure is traced to its code.

## Upstream evidence

- Create 6.0.8: https://www.curseforge.com/minecraft/mc-mods/create/files/all?version=1.20.1
- Steam 'n' Rails 1.7.3 C6: https://www.curseforge.com/minecraft/mc-mods/create-steam-n-rails/files/all?version=1.20.1
- Crafts & Additions 1.3.3: https://www.curseforge.com/minecraft/mc-mods/createaddition/files/7208610
- Enchantment Industry 1.4.1: https://www.curseforge.com/minecraft/mc-mods/create-enchantment-industry/files/all?gameVersionTypeId=6&page=1
- Slice & Dice 3.6.0: https://www.curseforge.com/minecraft/mc-mods/slice-and-dice/files/all?version=1.20.1
- New Age 1.2.0: https://www.curseforge.com/minecraft/mc-mods/create-new-age/files/all
- Diesel Generators 1.3.12: https://modrinth.com/mod/create-diesel-generators/version/DTQVvA5H
- Create Deco 2.0.3: https://modrinth.com/mod/create-deco/version/2.0.3-1.20.1-forge
- Aeronautics official compatibility: https://modrinth.com/modpack/create-aeronautics
- REA study: https://github.com/inematds/rea-engenharia-reversa