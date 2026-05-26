import os
import sys
import time
import threading
import requests
import keyboard
import psutil
import pystray
from PIL import Image, ImageDraw

running = True
resolume_running = False
webserver_ok = False
active_port = None
last_icon_state = None

HOTKEY = "ctrl+delete"
PORT_RANGE = range(8880, 8890)
RESOLUME_EXE_NAMES = ["Arena.exe", "Avenue.exe"]
CLEAR_DELAY = 0.08


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def load_icon_file(filename):
    ico_path = resource_path(filename)

    if os.path.exists(ico_path):
        try:
            img = Image.open(ico_path)
            img = img.convert("RGBA")
            img = img.resize((64, 64), Image.LANCZOS)
            return img
        except Exception:
            pass

    img = Image.new("RGBA", (64, 64), (30, 30, 30, 255))
    d = ImageDraw.Draw(img)
    d.rectangle((14, 14, 50, 50), outline=(120, 220, 200, 255), width=4)
    d.line((22, 22, 42, 42), fill=(255, 120, 120, 255), width=5)
    d.line((42, 22, 22, 42), fill=(255, 120, 120, 255), width=5)
    return img


def set_icon_state(icon, connected):
    global last_icon_state

    state = "connected" if connected else "disconnected"

    if last_icon_state == state:
        return

    if connected:
        icon.icon = load_icon_file("clear2.ico")
    else:
        icon.icon = load_icon_file("clear1.ico")

    last_icon_state = state


def is_resolume_running():
    names = [n.lower() for n in RESOLUME_EXE_NAMES]

    for p in psutil.process_iter(["name"]):
        try:
            pname = p.info.get("name")
            if pname and pname.lower() in names:
                return True
        except Exception:
            pass

    return False


def test_port(port):
    url = f"http://127.0.0.1:{port}/api/v1/composition"

    try:
        r = requests.get(url, timeout=0.4)
        if r.status_code < 500:
            return True
    except Exception:
        pass

    return False


def find_resolume_port():
    for port in PORT_RANGE:
        if test_port(port):
            return port
    return None


def find_selected_clip_ids(obj):
    found = []

    if isinstance(obj, dict):
        if (
            "id" in obj
            and "selected" in obj
            and isinstance(obj["selected"], dict)
            and obj["selected"].get("value") is True
        ):
            found.append(obj["id"])

        for v in obj.values():
            found.extend(find_selected_clip_ids(v))

    elif isinstance(obj, list):
        for item in obj:
            found.extend(find_selected_clip_ids(item))

    return found


def clear_selected_clip():
    global active_port

    if not resolume_running:
        return

    if not webserver_ok:
        return

    if active_port is None:
        return

    try:
        comp_url = f"http://127.0.0.1:{active_port}/api/v1/composition"
        r = requests.get(comp_url, timeout=0.8)

        if r.status_code >= 500:
            return

        data = r.json()
        clip_ids = find_selected_clip_ids(data)

        if not clip_ids:
            return

        clip_ids = list(dict.fromkeys(clip_ids))

        for clip_id in clip_ids:
            clear_url = (
                f"http://127.0.0.1:{active_port}"
                f"/api/v1/composition/clips/by-id/{clip_id}/clear"
            )
            requests.post(clear_url, timeout=0.5)
            time.sleep(CLEAR_DELAY)

    except Exception:
        pass


def rescan_now(icon=None, item=None):
    global active_port, webserver_ok

    active_port = find_resolume_port()
    webserver_ok = active_port is not None

    if icon:
        set_icon_state(icon, webserver_ok)

        if webserver_ok:
            icon.title = f"Resolume Clear Hotkey: Active / Port {active_port}"
        else:
            icon.title = "Resolume Clear Hotkey: Webserver OFF"


def monitor_status(icon):
    global resolume_running, webserver_ok, active_port, running

    while running:
        resolume_running = is_resolume_running()

        if resolume_running:
            if active_port is not None and test_port(active_port):
                webserver_ok = True
            else:
                active_port = find_resolume_port()
                webserver_ok = active_port is not None
        else:
            webserver_ok = False
            active_port = None

        connected = resolume_running and webserver_ok
        set_icon_state(icon, connected)

        if connected:
            icon.title = f"Resolume Clear Hotkey: Active / Port {active_port}"
        elif resolume_running and not webserver_ok:
            icon.title = "Resolume Clear Hotkey: Webserver OFF / Check 8880-8889"
        else:
            icon.title = "Resolume Clear Hotkey: Standby"

        time.sleep(2)


def quit_app(icon, item):
    global running

    running = False
    keyboard.unhook_all_hotkeys()
    icon.stop()


def main():
    keyboard.add_hotkey(HOTKEY, clear_selected_clip)

    icon = pystray.Icon(
        "ResolumeClearHotkey",
        load_icon_file("clear1.ico"),
        "Resolume Clear Hotkey: Standby",
        menu=pystray.Menu(
            pystray.MenuItem("Rescan Port 8880-8889", rescan_now),
            pystray.MenuItem("Exit", quit_app),
        ),
    )

    threading.Thread(target=monitor_status, args=(icon,), daemon=True).start()
    icon.run()


if __name__ == "__main__":
    main()