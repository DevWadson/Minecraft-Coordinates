@echo off
set caminho_pasta_to_App=c:\Workspace-Geral\Programacao\Ling.Python\Minecraft Coordinates\App

echo Criando o executável...
"C:\Users\DELL\AppData\Local\Programs\Python\Python312\python.exe" -m PyInstaller --name "Minecraft Coordinates" --onefile --noconsole --hidden-import=pandas mine_coords_index.py

if exist "%caminho_pasta_to_App%" (
    echo Pasta '%caminho_pasta_to_App%' já existe. Removendo...
    rmdir /S /Q "%caminho_pasta_to_App%"
    mkdir "%caminho_pasta_to_App%"

) else (
    echo Pasta '%caminho_pasta_to_App%' não existe. Criando...
    mkdir "%caminho_pasta_to_App%"
)

move /Y dist "%caminho_pasta_to_App%\"
move /Y build "%caminho_pasta_to_App%\"
move /Y "*.spec" "%caminho_pasta_to_App%\"

echo Processo concluído! O executável está em "%caminho_pasta_to_App%\dist".
pause
