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
ANALYTICS_ICON = ICONS_DIR / "analytics.png"
ANALYTICS_ICON_SELECTED = ICONS_DIR / "analytics_selected.png"
PERSON_ICON = ICONS_DIR / "person.png"
PERSON_ICON_SELECTED = ICONS_DIR / "person_selected.png"

# Font paths
FONTS_DIR = UI_DIR / "font"
INTER_FONT = FONTS_DIR / "Inter.ttf"

# Other assets
ASSETS_DIR = BASE_DIR / "assets"
DATA_JSON = ASSETS_DIR / "data.json"
MODEL_FILE = ASSETS_DIR / "model.onnx"

# Define the same colors as in draw_bounding_box
COLORS = [
    (242, 203, 255),  # Light Pink
    (133, 37, 247),   # Pink
    (158, 23, 181),   # Red Violet
    (183, 9, 114),    # Violet
    (163, 12, 58),    # Dark Violet
    (238, 97, 67),    # Blue
    (72, 239, 149),   # Cerulean
    (240, 201, 76)    # Light Cerulean
]

# Progress Bar
DEFAULT_STYLE = """

QProgressBar {
  border: none;
  border-radius: 2px;
  background-color: #f0f0f0;
  height: 16px;
  text-align: center;
}
QProgressBar::chunk {
  background-color: green;
  border-radius: 2px;
}

#feed_detect_btn,
#feed_stop_btn,
#discard_btn,
#save_btn {
  border-radius: 14px;
  padding: 15px 10px;
  text-align: center;
  color: white;
  font-weight: 700;
}

#feed_detect_btn {
  background-color: #210F37;
}

#feed_detect_btn:hover {
  background-color: #4F1C51;
}

#feed_stop_btn,
#discard_btn {
  background-color: #900D09;
}

#feed_stop_btn:hover,
#discard_btn {
  background-color: red;
}
"""

COMPLETED_STYLE = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: red;
    width: 10px;
    margin: 1px;
}

#feed_detect_btn,
#feed_stop_btn {
  border-radius: 14px;
  padding: 15px 10px;
  text-align: center;
  color: white;
  font-weight: 700;
}

#feed_detect_btn {
  background-color: #210F37;
}

#feed_detect_btn:hover {
  background-color: #4F1C51;
}

#feed_stop_btn {
  background-color: #003c00;
}

#feed_stop_btn:hover {
  background-color: green;
}

"""

# Pages
MENU = [
    { 
        "name": "     Camera View", 
        "default_icon": LOGO_ICON,
        "selected_icon": LOGO_ICON_SELECTED,
        "description": "Instructions", 
    },
    { 
        "name": "     Analytics", 
        "default_icon": ANALYTICS_ICON,
        "selected_icon": ANALYTICS_ICON_SELECTED,
        "description": "Analytics and the detections the user made will be viewed here", 
    },
    {
        "name": "     About", 
        "default_icon": PERSON_ICON,
        "selected_icon": PERSON_ICON_SELECTED,
        "description": "", 
    },
    { 
        "name": "     Configuration", 
        "default_icon": SETTING_ICON,
        "selected_icon": SETTING_ICON_SELECTED,
        "description": """
            Input your preferred YOLO configuration file and the camera RTSP Link

            Camera RTSP Link is already given since it is the default stream URL for the ToupTek Microscope Camera
        """, 
    }
]

# About
ABOUT = [
    {
        "name": "Dr. Val Randolf M. Madrid", 
        "designation": "Adviser",
        "college": "ICS"
    },
    {
        "name": "Ariezel M. Bautista", 
        "designation": "Undergraduate Student",
        "college": "ICS"
    },
    {
        "name": "James Albert M. Caraan", 
        "designation": "Undergraduate Student",
        "college": "IPB"
    },
    {
        "name": "Mark Cyril Mercado", 
        "designation": "Graduate Student",
        "college": "IPB"
    },
]

CAMERA_DESCRIPTION = """
1) Click the START button to view the camera feed

2) The DETECT button will be responsible for sending an image to the server for an inference
    a) DETECT will temporarily stop the feed and the user can review the resulting detections
    b) The user has the choice to save or discard the resulting image image

3) Press START FEED again to continue your search
"""