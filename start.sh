if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Snehal-k10/MOVIE-HOUSE-TEST-CODE.git /MOVIE-HOUSE-TEST-CODE 
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MOVIE-HOUSE-TEST-CODE 
fi
cd /MOVIE-HOUSE-TEST-CODE 
pip3 install -U -r requirements.txt
echo "Starting Bot....💌"
python3 bot.py
