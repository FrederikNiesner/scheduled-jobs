#!/bin/sh
cd Google\ Drive/Code/Repositories/scheduled-jobs/internetSpeed
git pull
python3 internetSpeed.py
git add .
git commit -m "scheduled speedtest `date`"
git push