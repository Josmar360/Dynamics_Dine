# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['Inicio.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('Image/*.png', 'Image'),
        ('Image/*.jpg', 'Image'),
        ('Screen/*.py', 'Screen'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Dynamics_Dine_Movil',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='Icon/Dynamics_Dine.png'  # Opcional: especifica el icono de tu aplicación
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Dynamics_Dine'
)
