# Ports-Jar Delivery Manifest

Target: Minecraft 1.20.1, Forge, Create mc1.20.1-6.0.8. Snapshot: 2026-10-23.

The Desktop `Ports-Jar` directory contains exactly one physical install file: `Ghouls-Create-Addons-1.20.1-Create-6.0.8.jar`. It is a Forge Jar-in-Jar package: the eight upstream JARs listed below are nested unmodified under `META-INF/jarjar/` and are still discovered by Forge as separate mods. They are not merged into one code namespace.

| Output | Size | SHA-256 | SHA-512 |
| --- | ---: | --- | --- |
| `Ghouls-Create-Addons-1.20.1-Create-6.0.8.jar` | 26,346,994 bytes | `10bf226d456578ce9658ced9770f53c1b52a79b219386f7ec4ac7382cee1a05c` | `3a065c0566d4e2216693e40f469ff27ec08f2be33ade7a8b187ce64eb63f7624dbf487bf4ccd4e6e60fd6e05adf36543af5d8acd4225ef1bc5ff1933b4e8d522` |

The outer ZIP/JAR integrity and all eight nested SHA-512 checksums were verified. No Minecraft runtime launch has been performed; this records packaging integrity, not combined in-game compatibility.

| Nested JAR under `META-INF/jarjar/` | Project/version | Source | SHA-512 |
| --- | --- | --- | --- |
| `Steam_Rails-1.7.3+forge-mc1.20.1.jar` | Steam 'n' Rails 1.7.3 Forge 1.20.1 C6 | https://modrinth.com/mod/create-steam-n-rails/version/7Uk6lWkU | `c46bd5e48e64914433157e8cb92f5679d3407fc6e3e3b40a1a41b043efa6f32a2eb9c486313358e92f9e4cf169710ab161bbfa86a2763afcadff3b6e92021175` |
| `createaddition-1.20.1-1.3.3.jar` | Crafts & Additions 1.3.3 Forge | https://modrinth.com/mod/createaddition/version/9LgyB6Yb | `a34f5c3b0226069d2882a3e23ba0e364a78bc5d26983b0cecea8d998718f454d3238ab7c5b4b3ef1749b6f2b26a4e427839c7c32468558fa7a8edb0edc727d10` |
| `create-enchantment-industry-2.5.4b.jar` | Enchantment Industry 2.5.4b, Create 6.0.8-291 | https://modrinth.com/mod/create-enchantment-industry/version/fs3kihCQ | `f8192da48ccf81821bb5c6666201e084611a877fc3ea188031aa15c66eee70a4c5e6484e5a20badde83bce30091e507ece81168a11984f406a683f407af0f75a` |
| `CreateDragonsPlus-1.11.9.jar` | Required by Enchantment Industry; Create 6.0.8 | https://modrinth.com/mod/create-dragons-plus/version/eMalpJtP | `6c9fe7b2cd0a3431cfb1b5c717fa2b03153c750f53e4cc394a2290447bc52848891627b0131f6e6dbc947e6f0c618e416d34942f9dd963a025f9ad18c015716a` |
| `sliceanddice-forge-3.6.0.jar` | Slice & Dice 3.6.0 Forge | https://modrinth.com/mod/slice-and-dice/version/KWLI8Ng7 | `b6108218d933ba6b612f2018efe1329957c0cde473f07bc405f7defa76602bb2f6749763db5734ec8547e8c5c1908ef57a9c539c90c23068ed9ab5be267e73a0` |
| `create-new-age-1.2.0+forge-mc1.20.1.jar` | New Age 1.2.0 Forge | https://modrinth.com/mod/create-new-age/version/7vnwbouk | `2a24913624febc797275654dd31a6ef0aeb63da71d243b5ab9c58b7fc8e51455f24645bed87ec430bd166c69e23df044dcfcf5fc2bde1d8b7c1c3206724a7a07` |
| `botarium-forge-1.20.1-2.3.4.jar` | Required by New Age on 1.20.1 | https://modrinth.com/mod/botarium/version/O7D6FTfW | `aa3530dde50966e47958690b02a343c4de3782d32ae3b2cb75b2155eebb76e172a292768d846b8d14a97bc9ebe18f1f655eaa3469fce13b2b4b15b16af0aba01` |
| `createdieselgenerators-1.20.1-1.3.12.jar` | Diesel Generators 1.3.12; Create 6.0.8 | https://modrinth.com/mod/create-diesel-generators/version/DTQVvA5H | `fc9aebaa5b654078be4736e1c35cc34edda0986db75fc3ce1391a86a499df6dcb3958d9854d402f5479eeb38d0f9388223b0359a34d594589e75ed3a58dd45a1` |

## Excluded

- Create Deco 2.0.3: its `mods.toml` pins Create to exactly 6.0.2, so it is incompatible with the requested 6.0.8 and is not present in the Desktop folder.
- Create Aeronautics/Sable: no official Forge 1.20.1 release; the experimental backport remains separate and is not repackaged here.
- Create core: the instance supplies Create 6.0.8; this folder contains add-ons and their required dependencies only.

The manifest records upstream version metadata and checksums; it does not certify combined runtime behavior.
