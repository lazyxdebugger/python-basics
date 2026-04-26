login_logs=[("ADMIN","192.10.90.5","FAILED"),("USER","192.10.90.6","SUCCESS"),("ADMIN","192.10.90.5","FAILED"),("GUEST","192.10.90.7","FAILED"),("ADMIN","192.10.90.5","FAILED"),("USER","192.10.90.6","SUCCESS"),("ADMIN","192.10.90.5","FAILED"),("GUEST","192.10.90.7","FAILED")]

uniq_ips={ip for _,ip,_ in login_logs}

failed_count=0
sus_ips=set()

for ip in uniq_ips:
    for username,i,status in login_logs:
        if ip==i and status=="FAILED":
            failed_count+=1
            sus_ips.add(i)
            
print("total failed logins:",failed_count)
print("sus ips:",sus_ips)
        
