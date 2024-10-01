import psutil

def usage():
    
    ram = psutil.virtual_memory()
    print("Din RAM användning är",ram.percent,"%")
    
    cpu = psutil.cpu_percent(interval=1, percpu=False)
    print("Din CPU användning är ",cpu,"%")
    
    disk = psutil.disk_usage('/')
    #Q: Visar endast värde 43?
    print("Din disk användning är ",disk.percent,"%")

