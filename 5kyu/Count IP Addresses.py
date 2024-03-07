def ip_to_int(ip):
    bytes = [int(x) for x in ip.split('.')]
    return (bytes[0] << 24) + (bytes[1] << 16) + (bytes[2] << 8) + bytes[3]

def ips_between(start, end):
    start_int = ip_to_int(start)
    end_int = ip_to_int(end)
    return end_int - start_int