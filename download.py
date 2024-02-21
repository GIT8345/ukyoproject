# ここにファイルの内容を生成するロジックを追加
file_content = """import tkinter as tk
from tkinter import ttk

root = tk.Tk()
radio_value = tk.IntVar()

rdio_1 = ttk.Radiobutton(root, text="1", variable=radio_value, value=1)
rdio_1.grid(row=0, column=0)

rdio_2 = ttk.Radiobutton(root, text="2", variable=radio_value, value=2)
rdio_2.grid(row=0, column=1)

button = tk.Button(root, text="check!!", command=lambda: print(radio_value.get()))
button.grid(row=1, column=3)

root.mainloop()
"""

# ファイルをダウンロードするためのHTTPヘッダーを設定
print("Content-Type: application/octet-stream")
print("Content-Disposition: attachment; filename=downloaded_file.py\n")

# ファイルの内容を出力
print(file_content)
