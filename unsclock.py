"""Windows のシステムスリープおよび画面ロックを抑制するモジュール。

Windows API の SetThreadExecutionState を呼び出し、ウィンドウが閉じられて
プロセスが終了するまでの間、システムスリープを抑制する。また、画面上の
チェックボタンにより、画面オフ（画面ロック）の抑制を動的に切り替えられる。
"""

import ctypes
import tkinter as tk
from tkinter import ttk

# SetThreadExecutionState に渡す実行状態フラグ定数
ES_CONTINUOUS: int = 0x80000000
ES_AWAYMODE_REQUIRED: int = 0x00000040
ES_SYSTEM_REQUIRED: int = 0x00000001
ES_DISPLAY_REQUIRED: int = 0x00000002


# 動作しているかは、管理者権限で
# powercfg requests
# で確認できる。
def update_execution_state(prevent_display_off: bool) -> None:
    """スレッドの実行状態を更新し、スリープおよび画面オフの抑制を設定する。

    Args:
        prevent_display_off: 画面オフの抑制も有効にする場合は True。
    """
    flags: int = ES_SYSTEM_REQUIRED | ES_CONTINUOUS
    if prevent_display_off:
        flags |= ES_DISPLAY_REQUIRED
    ctypes.windll.kernel32.SetThreadExecutionState(flags)


def main() -> None:
    """スリープ抑制を有効化し、設定切り替えと維持用のウィンドウを表示する。"""
    root = tk.Tk()
    root.title("Sleep Prevention - Info")
    root.resizable(False, False)

    # チェックボタンの状態変数（デフォルトは ON: 画面オフも抑制する）
    prevent_display_var = tk.BooleanVar(value=True)

    def on_toggle() -> None:
        """チェックボタンの状態変更時に実行状態を更新する。"""
        update_execution_state(prevent_display_var.get())

    # 初期状態（スリープ抑制 + 画面オフ抑制）を適用する
    update_execution_state(prevent_display_var.get())

    frame = ttk.Frame(root, padding=(20, 15))
    frame.grid(row=0, column=0, sticky="nsew")

    message_label = ttk.Label(
        frame,
        text="Sleep prevention is active.\nClick OK to stop and exit.",
        justify="left",
    )
    message_label.grid(row=0, column=0, sticky="w", pady=(0, 10))

    display_check = ttk.Checkbutton(
        frame,
        text="Prevent display turn-off (screen lock)",
        variable=prevent_display_var,
        command=on_toggle,
    )
    display_check.grid(row=1, column=0, sticky="w", pady=(0, 15))

    ok_button = ttk.Button(frame, text="OK", command=root.destroy, width=10)
    ok_button.grid(row=2, column=0)
    ok_button.focus_set()

    # Enter キーや Escape キーでも閉じられるようにバインドする
    root.bind("<Return>", lambda _event: root.destroy())
    root.bind("<Escape>", lambda _event: root.destroy())

    root.mainloop()


if __name__ == "__main__":
    main()
