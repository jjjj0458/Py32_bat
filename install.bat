@echo off
echo @author: JackCCChang
set PIP_INDEX_URL=http://autcbdpypi.corpnet.auo.com/simple
set PIP_TRUSTED_HOST=autcbdpypi.corpnet.auo.com
set ZipDir=%ProgramFiles%\7-Zip
set curdir=%~dp0
set pyzip=python-3.7.9-embed-win32.zip



echo 預設python壓縮檔位置:%curdir%%pyzip%
echo 電腦需安裝7z
if exist "%ZipDir%\7z.exe" (echo 已找到："%ZipDir%\7z.exe") else (echo 找不到："%ZipDir%\7z.exe"請檢查。 & pause&exit)
pause
cls
set deckPath=D:
set /p deckPath=安裝位置 (default - %deckPath%):
set outdir=%deckPath%\Python37-32bit\
echo 安裝位置:%outdir%
pause
cls
echo 解壓縮python壓縮檔到 %outdir%
pause
start /wait "" "%ZipDir%\7z.exe" x %curdir%%pyzip% -o%outdir% -aoa
pause
cls
echo 複製設定檔到 %outdir%
pause
robocopy "%curdir%Scripts" "%outdir%Scripts" /E
robocopy "%curdir%DLLs" "%outdir%DLLs" /E
robocopy "%curdir%Db2" "%outdir%Db2" /E
robocopy "%curdir%Utils" "%outdir%Utils" /E
copy "%curdir%python37._pth" "%outdir%python37._pth" /Y
copy "%curdir%sitecustomize.py" "%outdir%sitecustomize.py" /Y
pause
cls
echo 安裝pip
pause
%outdir%python %outdir%Scripts\get-pip.py
pause
cls
echo 安裝db2撈取資料相關套件
pause
%outdir%python -m pip install --force-reinstall %outdir%\Utils\pyodbc-4.0.32-cp37-cp37m-win32.whl
%outdir%python -m pip install %outdir%\Utils\numpy-1.21.5+vanilla-cp37-cp37m-win32.whl 
%outdir%python -m pip install %outdir%\Utils\pandas-1.0.0-cp37-cp37m-win32.whl
pause
cls
echo Check data query
echo 參考:%outdir%Db2\get_data.py 
pause
%outdir%python %outdir%Db2\get_data.py 
pause
