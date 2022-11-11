# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['toolbox.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'export_chart',
        'import_chart',
        'preview_chart'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'altgraph',
        'future',
        'pefile',
        'pip',
        'pyinstaller',
        'pyinstaller-hooks-contrib',
        'pywin32-ctypes',
        'setuptools',
        'wheel'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Omegar-Toolbox',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='Omega.ico',
)
