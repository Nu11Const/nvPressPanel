# nvPressPanel
# Install
```
curl -fsSL https://get.nvpress.tk | bash
```
# Build
## 第一步
首先进入`frontend`文件夹，如果安装过了pnpm，可以跳过此步。
```
npm install -g pnpm
pnpm setup
```
## 第二步
还是在`frontend`目录，执行此命令
```
pnpm install
pnpm build
```
之后就会在`dist`目录下生成前端文件。
## 第三步
切换到`backend`目录，将前端文件夹下的`index.html`复制到后端`templates`目录
将其它文件复制到后端`backend`目录。
## 第四步
执行
```python3 App.py```
会自动打开Web服务器，Flask后端，和FTP服务器。
