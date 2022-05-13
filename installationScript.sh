sudo apt-get -y update
sudo apt-get -y install gcc
sudo apt-get -y install make
sudo apt-get -y install libbz2-dev
sudo apt-get -y install zlib1g-dev
sudo apt-get -y install libncurses5-dev
sudo apt-get -y install libncursesw5-dev
sudo apt-get -y install liblzma-dev

mkdir ~/downloads
cd ~/downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh /S /D=%UserProfile%\Miniconda3
source ~/.profile