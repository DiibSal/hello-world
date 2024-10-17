import psutil

def usage():
    global ramPer, ramUse, ramTot, cpu, diskPer, diskUse, diskTot
    cpu = psutil.cpu_percent(interval=1)
    ramPer = psutil.virtual_memory().percent
    ramUse = psutil.virtual_memory().used/(1000**3)
    ramTot = psutil.virtual_memory().total/(1000**3)
    diskPer = psutil.disk_usage("/").percent
    diskUse = psutil.disk_usage("/").used/(1000**3)
    diskTot = psutil.disk_usage("/").total/(1000**3)
