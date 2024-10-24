import psutil

class Larm:
    

    def __init__(self, typ, grad):
        self.typ = typ
        self.grad = grad
       
    def alarm(self):
        if self.typ == "CPU":
            aktuellt_varde = psutil.cpu_percent(interval=0.1)
        elif self.typ == "RAM":
            aktuellt_varde = psutil.virtual_memory().percent
        elif self.typ == "Disk":
            aktuellt_varde = psutil.disk_usage('/').percent
        else:
            return
    
        if aktuellt_varde >= self.grad:
            print(f"LARM: {self.typ} över {self.grad}%: Aktuell användning: {aktuellt_varde}%")
    
    def __str__(self):
        return f"Larm för {self.typ} är sätt på: {self.grad}%"