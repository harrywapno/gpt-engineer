pip install -r requirements.txt

find /path/to/folder -type f -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" | xargs -P 4 -I {} python main.py {}
