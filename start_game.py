"""Serve the game on localhost so browser modules and camera access work."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.request import ProxyHandler, build_opener
import ctypes
import webbrowser


ROOT = Path(__file__).resolve().parent
TITLE = "粒子星球手势控制器".encode("utf-8")


class GameHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def open_game():
    opener = build_opener(ProxyHandler({}))
    handler = partial(GameHandler, directory=str(ROOT))
    for port in range(8000, 8021):
        url = f"http://localhost:{port}/"
        # Reuse an existing game server; leave unrelated services alone.
        try:
            with opener.open(url + "index.html", timeout=1) as response:
                if TITLE in response.read(65536):
                    webbrowser.open(url)
                    return
        except OSError:
            pass
        try:
            server = ThreadingHTTPServer(("127.0.0.1", port), handler)
        except OSError:
            continue
        with server:
            webbrowser.open(url)
            server.serve_forever()
        return
    raise RuntimeError("本地端口 8000–8020 均无法使用，请关闭旧的游戏服务后重试。")


if __name__ == "__main__":
    try:
        open_game()
    except Exception as error:
        ctypes.windll.user32.MessageBoxW(0, str(error), "游戏启动失败", 0x10)
