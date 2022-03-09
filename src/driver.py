#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections, pmonitor
from mininet.log import setLogLevel
from time import sleep

class SingleSwitchTopo(Topo):
	def build(self, n=2):
		switch = self.addSwitch("s1")
		for h in range(n):
			# Each host gets 50%/n of system CPU
			host = self.addHost( "h%s" % (h + 1), cpu=.5/n )
			# 10 Mbps, 5ms delay, 2% loss, 1000 packet queue
			self.addLink(host, switch, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True)

def startup_test(net):
	print("Host connections")
	dumpNodeConnections(net.hosts)
	print("Test network connectivity with pingAll")
	net.pingAll()

def iperf_test(net, a: str, b: str):
	print(f"Testing bandwidth between {a} and {b}.")
	ha, hb = net.get(a, b)
	net.iperf((ha, hb))

def host_process_test(net, h: str):
	print(f"Host {h} starting process")
	host = net.get(h)
	host.cmd("while true; do date; sleep 1; done > dates.out &")
	sleep(10)
	print("Process complete")
	host.cmd("kill %while")
	print("Output:")
	with open("dates.out", "r") as fl:
		for i, line, in enumerate(fl.readlines()):
			print(f"{i+1}: {line}")
		fl.close()

def host_node_test(net, h: str):
	server = net.get(h)
	server.setIP("127.0.0.1")
	client = net.get("h2")
	print(f"> Destroying existing node processes on {h}.")
	server.cmd("killall -9 node")

	print("> host running: node index.js "+server.IP()+"")
	res1 = server.cmd("node index.js "+server.IP()+"")	
	sleep(1)
	print(res1)

	print("> client running: curl http://"+server.IP()+":8080")
	res2 = client.cmd("curl -v http://"+server.IP()+":8080")
	print(res2)
	sleep(1)

	print(f"> Killing node processes on {h}.")
	server.cmd("killall -9 node")
	print("> Done.")


if __name__ == "__main__":
	setLogLevel("info")
	topo = SingleSwitchTopo(n=4)
	net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
	net.start()

	# Run tests
	#startup_test(net)
	#iperf_test(net, "h1", "h3")
	#host_process_test(net, "h1")    
	host_node_test(net, "h1")    

	net.stop()
