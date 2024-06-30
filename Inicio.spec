# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['Inicio.py'],  # Archivo principal de tu aplicación
    pathex=[],
    binaries=[],
    datas=[
        ('Font/*.otf', 'Font'),     # Incluir todas las fuentes .ttf en la carpeta Font
        ('Font/*.ttf', 'Font'),     # Incluir todas las fuentes .ttf en la carpeta Font
        ('Image/*.png', 'Image'),       # Incluir todas las imágenes en la carpeta Image
        ('Screen/*.py', 'Screen'),  # Incluir todos los archivos .py en la carpeta Screen
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

# Configuración del empaquetado
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    icon='Icon/Dynamics_Dine.png',  # Ruta al archivo .png que deseas usar como icono
    exclude_binaries=True,
    name='Inicio',
    debug=False,
    strip=False,
    upx=True,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,  # Incluir los archivos y carpetas especificados en datas
    strip=False,
    upx=True,
    name='dist/Inicio',
)
