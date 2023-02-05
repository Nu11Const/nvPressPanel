sudo service nvpress stop
sudo rm /www/nvpresspanel -rf
sudo wget -O panel.tar.gz https://get.nvpress.tk/panel.tar.gz
sudo tar -xvf  panel.tar.gz -C /www/nvpresspanel
echo 更新成功。。。