#!/usr/bin/env python3
"""Build one Forge Jar-in-Jar bundle from pinned official Create add-on JARs.

All downloads stay in memory. The only output is the requested outer JAR.
The bundled add-ons remain distinct Forge mods and retain their original JARs.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import pathlib
import urllib.request
import zipfile

ARTIFACTS = [
    {
        "mod_id": "railways",
        "version": "1.7.3+forge-mc1.20.1",
        "filename": "Steam_Rails-1.7.3+forge-mc1.20.1.jar",
        "url": "https://cdn.modrinth.com/data/ZzjhlDgM/versions/7Uk6lWkU/Steam_Rails-1.7.3%2Bforge-mc1.20.1.jar",
        "sha512": "c46bd5e48e64914433157e8cb92f5679d3407fc6e3e3b40a1a41b043efa6f32a2eb9c486313358e92f9e4cf169710ab161bbfa86a2763afcadff3b6e92021175",
    },
    {
        "mod_id": "createaddition",
        "version": "1.3.3",
        "filename": "createaddition-1.20.1-1.3.3.jar",
        "url": "https://cdn.modrinth.com/data/kU1G12Nn/versions/9LgyB6Yb/createaddition-1.20.1-1.3.3.jar",
        "sha512": "a34f5c3b0226069d2882a3e23ba0e364a78bc5d26983b0cecea8d998718f454d3238ab7c5b4b3ef1749b6f2b26a4e427839c7c32468558fa7a8edb0edc727d10",
    },
    {
        "mod_id": "create_enchantment_industry",
        "version": "2.5.4b",
        "filename": "create-enchantment-industry-2.5.4b.jar",
        "url": "https://cdn.modrinth.com/data/JWGBpFUP/versions/fs3kihCQ/create-enchantment-industry-2.5.4b.jar",
        "sha512": "f8192da48ccf81821bb5c6666201e084611a877fc3ea188031aa15c66eee70a4c5e6484e5a20badde83bce30091e507ece81168a11984f406a683f407af0f75a",
    },
    {
        "mod_id": "create_dragons_plus",
        "version": "1.11.9",
        "filename": "CreateDragonsPlus-1.11.9.jar",
        "url": "https://cdn.modrinth.com/data/dzb1a5WV/versions/eMalpJtP/CreateDragonsPlus-1.11.9.jar",
        "sha512": "6c9fe7b2cd0a3431cfb1b5c717fa2b03153c750f53e4cc394a2290447bc52848891627b0131f6e6dbc947e6f0c618e416d34942f9dd963a025f9ad18c015716a",
    },
    {
        "mod_id": "sliceanddice",
        "version": "3.6.0",
        "filename": "sliceanddice-forge-3.6.0.jar",
        "url": "https://cdn.modrinth.com/data/GmjmRQ0A/versions/KWLI8Ng7/sliceanddice-forge-3.6.0.jar",
        "sha512": "b6108218d933ba6b612f2018efe1329957c0cde473f07bc405f7defa76602bb2f6749763db5734ec8547e8c5c1908ef57a9c539c90c23068ed9ab5be267e73a0",
    },
    {
        "mod_id": "create_new_age",
        "version": "1.2.0+mc1.20.1",
        "filename": "create-new-age-1.2.0+forge-mc1.20.1.jar",
        "url": "https://cdn.modrinth.com/data/FTeXqI9v/versions/7vnwbouk/create-new-age-1.2.0%2Bforge-mc1.20.1.jar",
        "sha512": "2a24913624febc797275654dd31a6ef0aeb63da71d243b5ab9c58b7fc8e51455f24645bed87ec430bd166c69e23df044dcfcf5fc2bde1d8b7c1c3206724a7a07",
    },
    {
        "mod_id": "botarium",
        "version": "2.3.4",
        "filename": "botarium-forge-1.20.1-2.3.4.jar",
        "url": "https://cdn.modrinth.com/data/2u6LRnMa/versions/O7D6FTfW/botarium-forge-1.20.1-2.3.4.jar",
        "sha512": "aa3530dde50966e47958690b02a343c4de3782d32ae3b2cb75b2155eebb76e172a292768d846b8d14a97bc9ebe18f1f655eaa3469fce13b2b4b15b16af0aba01",
    },
    {
        "mod_id": "createdieselgenerators",
        "version": "1.20.1-1.3.12",
        "filename": "createdieselgenerators-1.20.1-1.3.12.jar",
        "url": "https://cdn.modrinth.com/data/ZM3tt6p1/versions/DTQVvA5H/createdieselgenerators-1.20.1-1.3.12.jar",
        "sha512": "fc9aebaa5b654078be4736e1c35cc34edda0986db75fc3ce1391a86a499df6dcb3958d9854d402f5479eeb38d0f9388223b0359a34d594589e75ed3a58dd45a1",
    },
]

ROOT_MOD_ID = "ghouls_create_addons_bundle"
BUNDLE_NAME = "Ghouls Create Add-ons Bundle"
BUNDLE_VERSION = "1.0.0"


def download_artifacts() -> list[tuple[dict, bytes]]:
    request_headers = {"User-Agent": "GhoulsCreateAddonsBundle/1.0"}
    downloaded = []
    for item in ARTIFACTS:
        request = urllib.request.Request(item["url"], headers=request_headers)
        with urllib.request.urlopen(request, timeout=90) as response:
            payload = response.read()
        actual = hashlib.sha512(payload).hexdigest()
        if actual != item["sha512"]:
            raise ValueError(f"SHA-512 mismatch for {item['filename']}: {actual}")
        with zipfile.ZipFile(io.BytesIO(payload)) as inner:
            if inner.testzip() is not None:
                raise ValueError(f"Corrupt nested JAR: {item['filename']}")
            if "META-INF/mods.toml" not in inner.namelist():
                raise ValueError(f"Forge metadata missing in {item['filename']}")
        downloaded.append((item, payload))
        print(f"Verified {item['filename']} ({len(payload)} bytes)")
    return downloaded


def create_bundle(output: pathlib.Path, downloaded: list[tuple[dict, bytes]]) -> None:
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {output}")

    metadata = {
        "jars": [
            {
                "identifier": {
                    "group": "com.santipdr.ghouls",
                    "artifact": item["mod_id"],
                },
                "version": {
                    "range": f"[{item['version']}]",
                    "artifactVersion": item["version"],
                },
                "path": f"META-INF/jarjar/{item['filename']}",
            }
            for item, _ in downloaded
        ]
    }
    mods_toml = f'''modLoader="lowcodefml"
loaderVersion="[47,)"
license="See the original license metadata in each nested mod JAR"

[[mods]]
modId="{ROOT_MOD_ID}"
version="{BUNDLE_VERSION}"
displayName="{BUNDLE_NAME}"
description=''' + '''"A single-file Forge Jar-in-Jar package of Create add-ons. Nested mods retain their own metadata and load as separate mods."'''

    notice = """Create add-ons bundle
Minecraft 1.20.1 | Forge 47.4.x | Create 6.0.8

The nested JARs are unmodified official artifacts. Forge loads each nested mod as its own mod; this outer archive only provides one physical file for installation. Each nested JAR retains its own metadata and license notices.

Included artifacts:
""" + "".join(f"- {item['filename']}\n" for item, _ in downloaded)

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_STORED) as outer:
        outer.writestr("META-INF/MANIFEST.MF", "Manifest-Version: 1.0\r\n\r\n")
        outer.writestr("META-INF/mods.toml", mods_toml)
        outer.writestr(
            "META-INF/jarjar/metadata.json",
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        )
        outer.writestr("META-INF/NOTICE.txt", notice)
        outer.writestr(
            "pack.mcmeta",
            json.dumps({"pack": {"pack_format": 15, "description": BUNDLE_NAME}}, ensure_ascii=False) + "\\n",
        )
        for item, payload in downloaded:
            outer.writestr(f"META-INF/jarjar/{item['filename']}", payload)

    with zipfile.ZipFile(output) as outer:
        if outer.testzip() is not None:
            output.unlink(missing_ok=True)
            raise ValueError("Outer bundle failed ZIP integrity validation")
        if len(metadata["jars"]) != len(ARTIFACTS):
            output.unlink(missing_ok=True)
            raise ValueError("Nested JAR manifest count mismatch")
        for item, payload in downloaded:
            embedded = outer.read(f"META-INF/jarjar/{item['filename']}")
            if hashlib.sha512(embedded).hexdigest() != item["sha512"]:
                output.unlink(missing_ok=True)
                raise ValueError(f"Embedded JAR changed: {item['filename']}")

    digest = hashlib.sha512(output.read_bytes()).hexdigest()
    print(f"Created {output}")
    print(f"Nested Forge JARs: {len(downloaded)}")
    print(f"Outer size: {output.stat().st_size} bytes")
    print(f"Outer SHA-512: {digest}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=pathlib.Path)
    args = parser.parse_args()
    create_bundle(args.output, download_artifacts())


if __name__ == "__main__":
    main()
