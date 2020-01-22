# Space Engineers Utilities
A Blender 2.8+ addon.

## Features
* Full Blender 2.8+ integration using collections instead of layers
* Spawn dummies, highlight empties and subparts directly from the context menu
* See full SE materials in Blender, as close to how they appear in the game as possible
* Create your own custom materials in Blender from presets
* Vanilla materials of imported FBX are automatically switched to make them display correctly
* Empties on imported FBX are automatically switched to cube display
* Set LOD distances directly in the UI
* Change grid scale between large and small grid directly
* See bounding box of block (respects grid scale setting)
* Exports collision model
* Exports basic CubeBlocks entry
* Exports directly to MWM

## Installation
1. Download the latest release of the addon from the releases section, enable it in Blender.
2. Download the supplementary ZIP (SEUT.zip) containing additional required files.
3. Ensure you have downloaded the Space Engineers Mod SDK.
4. Unpack the supplementary ZIP file onto a drive with ~15GB available disk space.
5. Within the resulting directory you should have the following structure:
```
SEUT\Materials\
SEUT\convert_textures.bat
```
5. Run the BAT file. Point it at the correct folder for your SE installation and SE Mod SDK's `texconv.exe`
6. Once the textures are unpacked, you should have the following structure:
```
SEUT\Materials\
SEUT\Textures\
SEUT\convert_textures.bat
```
7. In Blender, use File --> Link and navigate to the MatLib_*.blend files within the `SEUT\Materials\`-folder. Select `MatLib_Materials.blend` and link all its contained materials. Do the same for `MatLib_Armors.blend` and `MatLib_Items.blend`. You likely won't usually need the remaining ones.
8. Open the Toolbar in Blender by pressing `N` in the 3D View or Node Editor. Access Empty spawning by right-clicking into the 3D View.

## Support
Feel free to support the development of this addon by becoming one of Stollie's patreons! Without him, the development of the addon would never have gotten this far.

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Patreon_logo_with_wordmark.svg/512px-Patreon_logo_with_wordmark.svg.png)](https://www.patreon.com/Stollie)

## Credits
* **Stollie** - So much general help but also writing everything havok-related, which I wouldn't have been able to do at all.
* **Harag** - Writing the original Blender SE plugin. A lot of code in this addon is based on his.
* **Kamikaze (Blender Discord)** - Writing the `remapMaterials()`-function and generally helping out constantly by answering a lot of questions.
