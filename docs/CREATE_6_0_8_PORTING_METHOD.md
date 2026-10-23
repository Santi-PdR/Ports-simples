# Create 6.0.8 Add-on Porting Method

This guide records a repeatable, evidence-based workflow for checking and porting Create add-ons to Minecraft 1.20.1 Forge with Create 6.0.8. It adapts the evidence/map/limits/unknowns approach described by the public [REA reverse-engineering study](https://github.com/inematds/rea-engenharia-reversa). It does not copy that project's software or claim that reverse engineering alone grants distribution rights.

## Target contract

Pin and record all of the following before changing code:

- Minecraft 1.20.1
- Forge 47.4.x (record the exact build used for each validation)
- Java 17
- Create 6.0.8
- Exact Ponder, Flywheel, Registrate, loader, and add-on versions
- Client, dedicated-server, and integrated-server scope

Keep every add-on a separate mod artifact unless its upstream project already defines a supported bundle. Record the exact filename, internal mod id/version, dependencies, loader range, and SHA-256 for each final artifact.

## Source and permission review

1. Prefer the corresponding public source revision to bytecode analysis.
2. Record upstream repository, commit/tag, license file, asset license, and attribution requirements for each add-on and bundled dependency.
3. Preserve notices and license files. Treat the owner's authorization as applying only to the scope actually granted; it does not replace license notices or automatically grant downstream distribution rights.
4. Do not bypass DRM, access controls, or protections. If source is unavailable and authorized analysis is in scope, use static inspection and document the exact evidence and remaining unknowns.
5. Do not copy code, assets, or behavior from the REA study repository; it is a methodology reference only.

## Evidence-first reverse engineering

For each feature that must be preserved, create an evidence record with:

| Field | Record |
| --- | --- |
| Observation | User-visible behavior, registry entry, packet, data format, or crash |
| Evidence | Source path and symbol, or JAR/class/method descriptor and bytecode location |
| Map | Callers/callees, event or lifecycle path, state ownership, and side |
| Confidence | Directly observed, strongly inferred, or unknown |
| Limits | What was not inspected or tested |

For binary-only analysis, inventory the JAR without executing it. Inspect mods.toml, manifests, embedded dependencies, mixin configs, access transformers, service declarations, registries, resources, and relevant class files. Follow call sites and descriptors rather than guessing from names. Time-box expensive decompilation, isolate analysis tools, and preserve a record of skipped or undecodable classes. A decompiler rendering is evidence for investigation, not proof of runtime semantics.

## Porting workflow

1. Identify API changes between the add-on's supported Create release and Create 6.0.8. Search for changed signatures, removed internals, registry timing, rendering hooks, contraption serialization, and networking changes.
2. Make the smallest compatibility patch that preserves observable behavior. Keep compatibility edits separate from gameplay changes.
3. Keep client-only references out of dedicated-server loading paths.
4. Check registrations, ResourceLocations, codecs/data, block entities, capabilities, packets, and mixins against Forge 1.20.1 lifecycle.
5. Preserve data formats and saved-world compatibility. Do not silently rename registry ids or discard unknown saved data.
6. Build each add-on independently, then run a combined dependency matrix. Prefer Forge GameTests for deterministic server behavior; also launch a client for screens, models, rendering, and interactions.
7. Compare the produced JAR against the source project: metadata, required classes, assets, mixin configs, nested dependencies, and license notices.
8. Record every failure, workaround, warning, and untested surface.

## Validation gates

Do not call an add-on compatible based only on a successful compile or a Minecraft-version tag. Record results separately for:

- dependency resolution and Forge mod loading;
- dedicated-server startup and GameTests;
- client startup, screens, models, particles, and rendering;
- actual feature behavior and save/reload;
- coexistence with the other selected Create add-ons.

Use exact version pins. Test a minimal baseline first, then add one integration at a time. If an integration changes mixin targets, test both application orders where the loader permits it. A skipped optional injection is not proof that behavior works.

## Artifact hygiene

The delivery directory is an output location, not a workspace. Keep source, logs, downloaded references, intermediate builds, and backups outside it. After a build passes all gates, copy only the newest verified final JAR for each requested mod. Before copying, verify the JAR opens, inspect internal metadata and required entries, and calculate SHA-256. Remove superseded output only after the replacement passes verification; never leave duplicate versions or temporary files in the delivery directory.

## Current candidate status (research snapshot)

These are research findings, not runtime certification:

| Add-on | Candidate for 1.20.1 Forge / Create 6.0.8 | Evidence and caveat |
| --- | --- | --- |
| Steam 'n' Rails | 1.7.3 Forge | Upstream file is marked C6; verify the full pack at runtime. |
| Crafts & Additions | 1.3.3 Forge | Release notes state it was updated to Create 6.0.8. |
| Enchantment Industry | 1.4.1 Forge | Dedicated release for Create 6.0.8; use its 1.20.1 Forge file. |
| Slice & Dice | 3.6.0 Forge | Correct MC/loader file exists; verify with the pack's Create build and Farmer's Delight recipes. |
| New Age | 1.2.0 Forge | Correct MC/loader file exists; Botarium is required on 1.20.1. |
| Diesel Generators | 1.3.12 Forge | Latest listed 1.20.1 Forge file; its Create 6.0.8 behavior still needs a controlled runtime check. |
| Create Deco | 2.0.3 Forge | Changelog says Create 6 support; reports exist for some Create 6.0.8 combinations, so isolate and test. |
| Create Aeronautics | No official 1.20.1 Forge file identified | Official release page lists 1.21.1 NeoForge. This repository's backport is a separate experimental port. |

## Research reference

The REA repository presents reverse engineering as evidence-backed mapping with explicit limitations and unknowns. Its README also warns that analysis tools are not a sandbox and that license/protection boundaries still apply. This workflow applies those lessons to Minecraft JARs while preferring source-based ports whenever available.

- REA study: https://github.com/inematds/rea-engenharia-reversa
- Existing port and license record: ../PORTS_AND_LICENSES.md
