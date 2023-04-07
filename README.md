
# Payroll System 



## Run from docker 


sudo docker build --tag payroll .
sudo docker run -it --mount src=$(pwd)/data,target=/data,type=bind payroll