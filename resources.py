from pathlib import Path

# Base directory (automatically detects the project root)
BASE_DIR = Path(__file__).resolve().parent

# UI-related assets
UI_DIR = BASE_DIR / "ui"
STYLE_QSS = UI_DIR / "style.qss"

# Icon paths
ICONS_DIR = UI_DIR / "icons"
LOGO_ICON = ICONS_DIR / "feed.png"
LOGO_ICON_SELECTED = ICONS_DIR / "feed_selected.png"
MENU_OPEN_ICON = ICONS_DIR / "menu_open.png"
MENU_CLOSE_ICON = ICONS_DIR / "menu_close.png"
SETTING_ICON = ICONS_DIR / "settings.png"
SETTING_ICON_SELECTED = ICONS_DIR / "settings_selected.png"
PERSON_ICON = ICONS_DIR / "person.png"
PERSON_ICON_SELECTED = ICONS_DIR / "person_selected.png"

# Font paths
FONTS_DIR = UI_DIR / "font"
INTER_FONT = FONTS_DIR / "Inter.ttf"

# Other assets
ASSETS_DIR = BASE_DIR / "assets"
DATA_JSON = ASSETS_DIR / "data.json"
MODEL_FILE = ASSETS_DIR / "model.onnx"
