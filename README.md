## This is a test repository and contains sample scripts

1. random1.py is a python script and it prints 1 to 10 numbers randomly.
   numpy and random functions are used.
   In order to use the script, you need to have numpy library installed and then execute the script with python2.7
   
   Instructions to install pip and numpy on RHEL or Centos or Mac OS
   a. # curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   b. # sudo python get-pip.py
   c. # pip install numpy
   d. # python random1.py

2. An SSL offloading server with the following specs:
   - 4 times Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz
   - 64GB of ram
   - 2 tb HDD disk space
   - 2 x 10Gbit/s nics

   In this scenario I will be more interested in monitoring the following in the same priority as the order.
   i. CPU: I will monitor the CPU of the server as the SSL offloading involves a lot of computation hence it is a CPU intensive Job.
  ii. Network: As the number os requests proxied are 25000 which is a significant number I would monitor the network as well.
 iii. Memory: Though the memory of the server is high(64G) it depends on the SSL implementation how much memory does it need, if the SSL is using a significant amount of memory then we might be interested in monitoring the memory as well.

I will be monitoring all these parameters using nagios and setup alerts so that I can take preventive measures after the warnings alerts are recieved.

