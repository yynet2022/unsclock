"""Windows のシステムスリープおよび画面ロックを抑制するモジュール。

Windows API の SetThreadExecutionState を呼び出し、メッセージボックスが
閉じられてプロセスが終了するまでの間、スリープと画面オフを抑制する。
"""

import ctypes
from tkinter import messagebox

# SetThreadExecutionState に渡す実行状態フラグ定数
ES_CONTINUOUS: int = 0x80000000
ES_AWAYMODE_REQUIRED: int = 0x00000040
ES_SYSTEM_REQUIRED: int = 0x00000001
ES_DISPLAY_REQUIRED: int = 0x00000002


# 動作しているかは、管理者権限で
# powercfg requests
# で確認できる。
def main() -> None:
    """スリープ抑制を有効化し、維持用の情報ダイアログを表示する。"""
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_DISPLAY_REQUIRED | ES_SYSTEM_REQUIRED | ES_CONTINUOUS
    )
    messagebox.showinfo(
        "Sleep Prevention - Info",
        "Sleep prevention is active.\nClick OK to stop and exit.",
    )


if __name__ == "__main__":
    main()
