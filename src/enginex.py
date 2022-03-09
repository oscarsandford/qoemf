from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.net import Mininet
import time

class DumbbellTopo(Topo):
    def build(self, bw=8, delay="10ms", loss=0):
        switch1 = self.addSwitch('switch1')
        switch2 = self.addSwitch('switch2')
        appClient = self.addHost('aClient')
        appServer = self.addHost('aServer')
        crossClient = self.addHost('cClient')
        crossServer = self.addHost('cServer')
        self.addLink(appClient, switch1)
        self.addLink(crossClient, switch1)
        self.addLink(appServer, switch2)
        self.addLink(crossServer, switch2)
        self.addLink(switch1, switch2, bw=bw, delay=delay, loss=loss, max_queue_size=14)

def simulate():
    dumbbell = DumbbellTopo()
    network = Mininet(topo=dumbbell, host=CPULimitedHost, link=TCLink, autoPinCpus=True)
    network.start()

    appClient = network.get('aClient')
    appServer = network.get('aServer')

    wd = str(appServer.cmd("pwd"))[:-2]

    appServer.cmd("echo 'b a n a n a s' > available-fruits.html")
    appServer.cmd("echo 'events { } http { server { listen " + appServer.IP() + "; root " + wd + "; } }' > nginx-conf.conf") # Create server config file
    appServer.cmd("sudo nginx -c " + wd + "/nginx-conf.conf &") # Tell nginx to use configuration from the file we just created

    time.sleep(1) # Server might need some time to start

    fruits = appClient.cmd("curl -v http://" + appServer.IP() + "/available-fruits.html")
    print(fruits)

    appServer.cmd("sudo nginx -s stop")
    network.stop()

if __name__ == '__main__':
    simulate()
