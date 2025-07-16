import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from langgraphagent.ui.streamlitui.loadui import launch_ui
from langgraphagent.ui.uiconfigfile import *

if __name__ == "__main__":
    launch_ui()
