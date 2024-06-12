import psutil

def get_system_stats():
    # CPU statistics
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()
    
    # Memory statistics
    memory = psutil.virtual_memory()
    memory_total = memory.total
    memory_used = memory.used
    memory_free = memory.free
    
    # Disk statistics
    disk = psutil.disk_usage('/')
    disk_total = disk.total
    disk_used = disk.used
    disk_free = disk.free
    
    # Network statistics
    network = psutil.net_io_counters()
    bytes_sent = network.bytes_sent
    bytes_received = network.bytes_recv
    
    # Print statistics
    print("CPU Usage: {}%".format(cpu_percent))
    print("CPU Count: {}".format(cpu_count))
    print("CPU Frequency: {} MHz".format(cpu_freq.current if cpu_freq is not None else "N/A"))
    print("Memory Total: {:.2f} GB".format(memory_total / (1024 ** 3)))
    print("Memory Used: {:.2f} GB".format(memory_used / (1024 ** 3)))
    print("Memory Free: {:.2f} GB".format(memory_free / (1024 ** 3)))
    print("Disk Total: {:.2f} GB".format(disk_total / (1024 ** 3)))
    print("Disk Used: {:.2f} GB".format(disk_used / (1024 ** 3)))
    print("Disk Free: {:.2f} GB".format(disk_free / (1024 ** 3)))
    print("Bytes Sent: {:.2f} MB".format(bytes_sent / (1024 ** 2)))
    print("Bytes Received: {:.2f} MB".format(bytes_received / (1024 ** 2)))

# Call the function to get and print system stats
get_system_stats()
