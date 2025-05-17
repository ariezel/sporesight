# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ui', 'ui'),
    ],
    hiddenimports=['PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'PyQt5.sip'],  # Add Qt dependencies
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SporeSight',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Set to True temporarily for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='ui/logo/sporesight.icns',
    onefile=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SporeSight',
)

# macOS .app bundle configuration
app = BUNDLE(
    coll,  # Change back to using coll
    name='SporeSight.app',
    icon='ui/logo/sporesight.icns',
    bundle_identifier='com.sporesight.app',
    info_plist={
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleVersion': '1.0.0',
        'CFBundleExecutable': 'SporeSight',
        'NSHighResolutionCapable': 'True',
        'LSBackgroundOnly': 'False',
        'NSRequiresAquaSystemAppearance': 'False',
        'NSPrincipalClass': 'NSApplication',
        'CFBundleDisplayName': 'SporeSight',
        'CFBundleName': 'SporeSight',
        'NSAppleScriptEnabled': False,
        # Add macOS-specific Qt config
        'PyQt5Environment': {
            'QT_MAC_WANTS_LAYER': '1',
            'QT_QPA_PLATFORM': 'cocoa',
        },
    },
)