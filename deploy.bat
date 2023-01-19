@echo off
cd frontend
npm i -g pnpm
pnpm install
pnpm build
copy dist/assets dist/js favicon.ico -r ../backend/static
copy dist/index.html ../backend/static
cd ../backend
pip3 -r install requirements.txt
echo "Open 127.0.0.1:8080 to use it!"
python3 App.py