# UE4 git template

###### tags: `UE4`

.gitignore
```
Saved/
Intermediate/
Build/
Binaries/
Plugins/
```

.gitattributes
```
*.uasset filter=lfs diff=lfs merge=lfs -text
*.umap filter=lfs diff=lfs merge=lfs -text
```