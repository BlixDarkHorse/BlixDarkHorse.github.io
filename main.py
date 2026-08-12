from pathlib import Path
import webview
ROOT=Path(__file__).resolve().parent
webview.create_window('UNIVERSO BDH', (ROOT/'index.html').as_uri(), width=1500, height=920, min_size=(1000,700), frameless=True, resizable=True)
webview.start(gui='edgechromium', debug=False)
