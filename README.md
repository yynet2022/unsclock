# unsclock

A simple Windows utility to prevent system sleep and display lock while a dialog box is open.

---

## English

### Overview

`unsclock` is a lightweight Python tool for Windows that prevents the system from entering sleep mode or turning off the display (which often triggers the screen lock). It calls the Windows API `SetThreadExecutionState` and keeps the state active until you close the information dialog.

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

When launched, an information dialog titled **"Sleep Prevention - Info"** will appear:

> Sleep prevention is active.  
> Click OK to stop and exit.

While this dialog remains open, Windows will not automatically go to sleep or turn off the display. To end sleep prevention, simply click **OK** (or close the dialog).

### How to Verify

You can check whether `unsclock` is actively preventing sleep by running the following command in an **Administrator** Command Prompt or PowerShell while the dialog is open:

```powershell
powercfg /requests
```

You will see `python.exe` (or `pythonw.exe`) listed under the `DISPLAY:` and `SYSTEM:` sections.

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

`unsclock` は、ダイアログを表示している間、Windows のシステムスリープおよび画面オフ（画面ロック）を抑制する軽量な Python ツールです。Windows API の `SetThreadExecutionState` を呼び出し、情報ダイアログが閉じられるまでの間、スリープ抑制状態を維持します。

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

起動すると、**"Sleep Prevention - Info"** というタイトルの情報ダイアログが表示されます。

> Sleep prevention is active.  
> Click OK to stop and exit.

このダイアログが開いている間、Windows は自動的にスリープへ移行したりディスプレイの電源を切ったりしなくなります。スリープ抑制を終了するには、ダイアログの **OK** をクリック（またはダイアログを終了）してください。

### 動作確認方法

スリープ抑制が有効に機能しているかどうかは、ダイアログを開いた状態で **管理者権限** のコマンドプロンプトまたは PowerShell から以下のコマンドを実行することで確認できます。

```powershell
powercfg /requests
```

`DISPLAY:` および `SYSTEM:` の項目に、実行中の `python.exe`（または `pythonw.exe`）が表示されます。

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
