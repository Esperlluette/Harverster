import nmap

class Scanner():
    def __init__(self):
        self.nm = nmap.PortScanner()
    
    def network_scan_number_ip_mac_devices(self, ip_network:str):
        """ Return a dict with number of devices connectes and their ips 
            {
                "number devices":X,
                "ip":"mac",
                "ip":"mac",
                "ip":"mac",
                "ip":"mac",
                "ip":"mac",
            }
            
        to do : recover hostname, ip, mac address to asignate hostname to an ip and mac. 
        1 get list of ip
        2 get list of hostnames 
        3 get list of macs 
        4 combine them 
        5 return the dictionnary  

        Args:
            ip_network (str): _description_

        Returns:
            _dict: dictionnary with hostname, ip, mac
            OR : 
            Exception: e
        """
        _dict= {}
        _except = None
        _mac_list = []
        # _hostname_list = []
        print(_except)

        try: 
            print("scan")
            self.nm.scan(hosts=ip_network,arguments='-n -sP',timeout=15)
        except Exception as e:
            _except = e
        for element in self.nm.all_hosts():
            if 'mac' in self.nm[element]['addresses']:
                mac_address = self.nm[element]['addresses']['mac']
            else: 
                mac_address = 'None'    
            _mac_list.append(mac_address)
            _dict[element] = mac_address 
        for element in _dict:
            print(f"IP: {element}, MAC: {_dict[element]}")
        return _dict
            
    
    def machine_scan_open_ports_on_device(self, ip_addr:str):
        self.nm.scan(hosts=ip_addr, arguments="-p 1-65535 ")
        return self.nm[ip_addr]['tcp'].keys()

    def focus_on_machine_ip(self, ip_addr:str): 
        """Scan a host given is parameter and return all opens ports and service attached
        Args:
            ip_addr (str): Host ip address 
        
        Returns: 
            services (dict): dictionnary with           {
            "OPEN_PORT": {"service":"SERVICE_NAME",
                          "version":"VERSION"}
            "OPEN_PORT": {"service":"SERVICE_NAME",
                          "version":"VERSION"}
        }
        """

            #### NOT FINISH YET DO NOT USE ###

        # try:
        #     self.nm.scan(hosts=ip_addr)
        #     if  self.nm['nmap']['scaninfo']['error']>0: 
        #         return None
        #     for element in self.nm["scan_result"]["nmap"]:
        #         print(element)
        # except Exception as e:
        #    return e
          
    def focus_on_machine_mac(self, ip_addr:str):
        pass