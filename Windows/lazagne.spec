# -*- mode: python -*-
import sys
sys.path.append(".")
from lazagne.config.manage_modules import get_modules_names
from lazagne.softwares.browsers.chromium_browsers import chromium_based_module_location
from lazagne.softwares.browsers.firefox_browsers import mozilla_module_location

all_hidden_imports_module_names = get_modules_names() + [mozilla_module_location, chromium_based_module_location]
hiddenimports = [package_name for package_name, module_name in all_hidden_imports_module_names]

block_cipher = pyi_crypto.PyiBlockCipher(key='t7q3yircwnt3ui')

a = Analysis(
        ['laZagne.py'],
        pathex=[''],
        hiddenimports=hiddenimports,
        hookspath=None,
        runtime_hooks=None,
        cipher=block_cipher
)

for d in a.datas:
  if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
        pyz,
        a.scripts,
        a.binaries + [('msvcp100.dll', 'C:\\Windows\\System32\\msvcp100.dll', 'BINARY'),
                      ('msvcr100.dll', 'C:\\Windows\\System32\\msvcr100.dll', 'BINARY')]
        if sys.platform == 'win32' else a.binaries,
        a.zipfiles,
        a.datas,
        name='lazagne.exe',
        debug=True,
        strip=None,
        upx=False,
        console=True
)
