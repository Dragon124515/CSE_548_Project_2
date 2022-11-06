from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI


class MyTopo( Topo ):

    def build( self ):


        # Add hosts and switches
        Host1 = self.addHost( 'h1', ip="192.168.2.10" )
        Host2 = self.addHost( 'h2', ip="192.168.2.20" )
        Host3 = self.addHost( 'h3', ip="192.168.2.30" )
        Host4 = self.addHost( 'h4', ip="192.168.2.40" )
        Switch = self.addSwitch( 's1' )

        # Add links
        self.addLink( Host1, Switch )
        self.addLink( Host2, Switch )
        self.addLink( Host3, Switch )
        self.addLink( Host4, Switch )

#connects to the Pox network on port 6655
Controller = RemoteController( 'c1', port=6655 )

topo = MyTopo()
net = Mininet(topo=topo, switch=OVSSwitch, controller=Controller,autoSetMacs=True)
#starts the mininet
net.start()
#starts up the interactive command line interface for the mininet
CLI(net)
#stops the net when the command line interface is closed
net.stop()
