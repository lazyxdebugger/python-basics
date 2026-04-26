
login_attempt=[("192.90.10.1","FAILED"),("192.90.10.3","SUCCESS"),("192.90.10.1","FAILED"),("192.90.10.1","FAILED"),("192.90.10.3","FAILED"),("192.90.10.3","SUCCESS"),("192.90.10.1","FAILED")]

uniq_ips={ip for ip,_ in login_attempt}

print("possible brute force attackers are:")

for ip in uniq_ips:
    count=0
    for i,status in login_attempt:
        if i==ip and status=="FAILED":
            count+=1
    if count>=3:
        print(f"{ip}-->{count} failed attempts")


