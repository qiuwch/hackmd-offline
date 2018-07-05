# UE4 scripts.

###### tags: `UE4`

`install-unrealcv.sh`

```shell
project_folder=$1
if [[ -z ${project_folder} ]]; then
  echo Please specify project folder
else
  echo Project folder is ${project_folder}
  rm -rf ${project_folder}/Plugins
  cp -r /c/qiuwch/workspace/unrealcv/unrealcv/Plugins ${project_folder}
fi
```

`build-project.bat`

```shell
set UE4=C:\Program Files\Epic Games\UE_4.14
REM set project_file=UrbanCity/UrbanCity.uproject
REM set project_file=RealisticRendering/RealisticRendering.uproject
REM set project_file=ArchinteriorsVol2Scene1/ArchinteriorsVol2Scene1.uproject
set project_file=%1
set binary_folder=%CD%/binary-414-v0.3
"%UE4%/Engine/Build/BatchFiles/RunUAT.bat" BuildCookRun -project=%CD%/%project_file% -archivedirectory=%binary_folder% -noP4 -platform=Win64 -clientconfig=Development -serverconfig=Development -allmaps -stage -pak -archive -build -cook
```