# Proxy-Speed-Test-Ftp-chacker
# For Proxy test run python3 speed.py 
It Will create a file named proxs.txt . put ip:port into the file
then agin run python3 speed.py .
# For Ftp check the process is same just change the url in the code 
# then Run python3 ftp.py

# 2 nd Updated way
# use : pip install -U cf-speedtest
# then : nano proxy 
# then : while read ip;do cf_speedtest --proxy http://"$ip";done < proxy | tee result
# Watch 2nd Way video added in the file
