@echo off
cd /d %~dp0
echo [CML_S] Spoustím hromadné značkování na všech jednotkách...
python batch_tag_all.py
pause
