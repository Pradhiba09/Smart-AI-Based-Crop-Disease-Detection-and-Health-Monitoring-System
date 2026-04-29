Location

The PlantVillage dataset should be placed in the workspace under:

data/plantvillage

Why here

- Keeps data next to code for training and preprocessing.
- Excluded from git (recommended) to avoid large repo sizes.

Quick Windows (PowerShell) steps

1. Create target folder:

```powershell
New-Item -ItemType Directory -Path .\data\plantvillage -Force
```

2. If you downloaded a ZIP (e.g., PlantVillage.zip), unzip into the folder:

```powershell
Expand-Archive -LiteralPath "C:\path\to\PlantVillage.zip" -DestinationPath .\data\plantvillage
```

3. (Optional) If files are nested, move them so each class has its own subfolder under data/plantvillage (train/val/test as needed).

Repository notes

- If you will push this repo to a remote, do NOT add raw images to git. Use Git LFS or keep the dataset outside the repo and reference its path.

Example .gitignore lines to add:

```
/data/
```

Or track large files with Git LFS:

```powershell
git lfs install
git lfs track "*.jpg"
git add .gitattributes
```

Next steps I can do for you

- Create a `data/` loader or preprocessing script and integrate it into the training flow.
- Add an upload endpoint to `app.py` so users can upload via the web app.
- Create train/val/test split script and sample commands.

Tell me which next step you want me to do.