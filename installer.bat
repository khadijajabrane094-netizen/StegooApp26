@echo off
title 🛡️ StegoApp Premium - Installation
color 0B
echo ========================================
echo    🛡️ StegoApp Premium
echo    Installation des dépendances
echo ========================================
echo.
echo ⏳ Installation de Python packages...
echo.
pip install streamlit Pillow --quiet
echo.
echo ✅ Installation terminée avec succès !
echo.
echo 💡 Lancez maintenant lancer_App.bat
pause