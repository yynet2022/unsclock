# unsclock

A simple Windows utility to prevent system sleep and display lock while a dialog window is open.

---

## English

### Overview

`unsclock` is a lightweight Python tool for Windows that prevents the system from entering sleep mode or turning off the display (which often triggers the screen lock). It calls the Windows API `SetThreadExecutionState` and keeps the state active until you close the window.

You can also dynamically toggle whether to prevent display turn-off (screen lock) using the checkbox in the window.

No external dependencies are required; it only uses the Python standard library (`ctypes` and `tkinter`).

### Requirements

- **OS**: Windows 10 / Windows 11
- **Python**: 3.9 or higher

### Usage

Run the script directly with Python:

```bash
python unsclock.py
```

Or run it without a console window using `pythonw`:

```bash
pythonw unsclock.py
```

When launched, a window titled **"Sleep Prevention - Info"** will appear:

> Sleep prevention is active.  
> Click OK to stop and exit.
>
> [x] Prevent display turn-off (screen lock)

- **While the window remains open**: Windows will not automatically go to sleep.
- **Prevent display turn-off (screen lock)** *(checked by default)*:
  - **Checked**: Prevents both system sleep and display turn-off (`ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED`).
  - **Unchecked**: Prevents system sleep only, allowing the display to turn off according to Windows settings (`ES_SYSTEM_REQUIRED`).
- **To exit**: Click **OK**, press `Enter` / `Esc`, or close the window.

### How to Verify

You can check whether `unsclock` is actively preventing sleep by running the following command in an **Administrator** Command Prompt or PowerShell while the window is open:

```powershell
powercfg /requests
```

You will see `python.exe` (or `pythonw.exe`) listed under `SYSTEM:` (and under `DISPLAY:` when the checkbox is checked).

### Development

Install development dependencies (`ruff`):

```bash
pip install -e ".[dev]"
```

Run linter and formatter checks:

```bash
ruff check .
ruff format --check .
```

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 日本語

### 概要

`unsclock` は、ウィンドウを表示している間、Windows のシステムスリープおよび画面オフ（画面ロック）を抑制する軽量な Python ツールです。Windows API の `SetThreadExecutionState` を呼び出し、ウィンドウが閉じられるまでの間、スリープ抑制状態を維持します。

ウィンドウ内のチェックボタンを使って、画面オフ（画面ロック）の抑制を有効にするかどうかを動的に切り替えることも可能です。

外部ライブラリへの依存はなく、Python の標準ライブラリ（`ctypes` および `tkinter`）のみで動作します。

### 動作要件

- **OS**: Windows 10 / Windows 11
- **Python**: 3.9 以上

### 使い方

Python で直接スクリプトを実行します。

```bash
python unsclock.py
```

コンソールウィンドウを表示させずに実行したい場合は `pythonw` を使用します。

```bash
pythonw unsclock.py
```

起動すると、**"Sleep Prevention - Info"** というタイトルのウィンドウが表示されます。

> Sleep prevention is active.  
> Click OK to stop and exit.
>
> [x] Prevent display turn-off (screen lock)

- **ウィンドウが開いている間**: Windows は自動的にシステムスリープへ移行しなくなります。
- **Prevent display turn-off (screen lock)** *(デフォルトで ON)*:
  - **チェック ON**: システムスリープと画面オフの両方を抑制します（`ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED`）。
  - **チェック OFF**: システムスリープのみを抑制し、画面オフは Windows の電源設定に従って許可します（`ES_SYSTEM_REQUIRED`）。
- **終了方法**: **OK** ボタンをクリックするか、`Enter` / `Esc` キーを押すか、ウィンドウを閉じてください。

### 動作確認方法

スリープ抑制が有効に機能しているかどうかは、ウィンドウを開いた状態で **管理者権限** のコマンドプロンプトまたは PowerShell から以下のコマンドを実行することで確認できます。

```powershell
powercfg /requests
```

`SYSTEM:` の項目（およびチェック ON の場合は `DISPLAY:` の項目）に、実行中の `python.exe`（または `pythonw.exe`）が表示されます。

### 開発者向け情報

開発用依存パッケージ（`ruff`）のインストール:

```bash
pip install -e ".[dev]"
```

Linter および Formatter のチェック実行:

```bash
ruff check .
ruff format --check .
```

### ライセンス

本プロジェクトは MIT ライセンスのもとで公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。
