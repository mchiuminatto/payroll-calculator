sudo chmod ugo+wr ./data/; # make sure have right permissions
sudo chmod ugo+wr ./data/*; # make sure have right permissions
export PYTHONPATH=$PWD;
python3 ./payroll_calculator/main.py ./data/work_record.txt ./data/payroll.csv;
