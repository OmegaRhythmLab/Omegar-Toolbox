# Omegar-Toolbox: Omega 官方制谱工具箱

## 常见问题解答

**Q：使用时界面消失，任务栏上也没有图标，是不是闪退了？**

**A：大概率是弹出的文件选择对话框跑到了后台，请按 Alt+Tab 寻找。**

## 如何导入谱面

### 导入 `mcz` 文件（支持批量导入）

1. 进入“导入谱面”功能，选择 `mcz` 文件，随后程序将在同目录下生成谱面文件夹。

### 导入 `mc` 文件（支持非 Malody 谱面）

1. 解压 `mcz`/`osz` 等文件。
2. 对于非 Malody 谱面，请使用 [rmstZ](https://lrfasd.github.io/rmstZ/rmstZ_20221022.html) 把 `osu` 等谱面文件转为 `mc` 格式。
3. 进入“导入谱面”功能，将对话框中的文件类型改为 `MC`，选择 `mc `文件，随后程序将在同目录下生成 `json` 工程文件。

## 如何导出谱面

### 首次导出

1. 进入“导出谱面”功能，程序询问是否使用模板时，选择“否”。
2. 填写曲名、曲师、画师。
3. 选择音频文件和曲绘图片。
4. 逐张输入谱面的难度（`Alpha` / `Beta` / `Gamma` / `Omega`）、定数和谱师，并选择 JSON 谱面文件，以添加谱面。若全部添加完毕，点击“完成添加”，否则点击“继续添加”。
5. 程序询问是否保存模板时，建议选择“是”，并选择模板文件保存位置，以便于后续重复导出。
6. 选择谱面 ZIP 文件保存位置，等待程序完成谱面的转换与打包即可。

### 重复导出

1. 进入“导出谱面”功能，程序询问是否使用模板时，选择“是”并选择 `tpl` 模板文件。
2. 查看是否需要改变歌曲信息，若不需要，点击“确认”，否则点击“更改”并跳转至首次导出的第 3~4 步。
3. 查看是否需要添加或删除谱面，若不需要，点击“完成添加”，否则跳转至首次导出的第 5 步。
4. 选择谱面 ZIP 文件保存位置，等待程序完成谱面的转换与打包即可。

## 如何预览谱面

### 预览 `omgz` 谱面

1. 进入“预览谱面”功能，选择 `omgz` 文件。
2. 若 `omgz` 文件中存在多个难度的谱面，请选择要预览的难度。
3. 若需要更改播放参数，请按以下说明修改，否则直接点击“OK”以使用默认值。
   * 流速倍率：谱面中 note 移动的速度，1 表示最低速度，该值越大速度越快。
   * 音乐音量：歌曲音频播放的音量，0 表示静音，1 表示以原音量播放。
4. 观看谱面。

### 预览 `json` 谱面

1. 预先使用“导出谱面”功能生成 `tpl` 模板文件。
2. 进入“预览谱面”功能，将对话框中的文件类型改为 `TPL`，选择 `tpl `文件，跳转至预览 `omgz` 谱面的第 3 步。
3. 观看谱面。

### 预览 `mcz` 谱面

1. 进入“预览谱面”功能，将对话框中的文件类型改为 `MCZ`，选择 `mcz `文件，跳转至预览 `omgz` 谱面的第 3 步。
2. 观看谱面。
