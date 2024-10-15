import psutil

def usage():
    
    ram = psutil.virtual_memory()
    print("Din RAM användning är",ram.percent,"%")
    
    cpu = psutil.cpu_percent(interval=0.5)
    print("Din CPU användning är ",cpu,"%")
    
    disk = psutil.disk_usage('/')
    print("Din disk användning är ",disk.percent,"%")

