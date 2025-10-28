#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

class SpineLeafTopo( Topo ):

    def build( self ):
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        spines = [s1, s2] # Lista para las conexiones

        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )
        s6 = self.addSwitch( 's6' )
        leaves = [s3, s4, s5, s6] # Lista para las conexiones
        
        # Añadimos los 4 hosts
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )

        # Conectar Hosts a Switches
        # h1 <-> s3
        self.addLink( h1, s3 )
        # h2 <-> s4
        self.addLink( h2, s4 )
        # h3 <-> s5
        self.addLink( h3, s5 )
        # h4 <-> s6
        self.addLink( h4, s6 )

        # Conectar Switches Spine a Switches Leaf
        for spine in spines:
            for leaf in leaves:
                self.addLink( spine, leaf )
topos = { 'spineleaf': ( lambda: SpineLeafTopo() ) }

def run():
    "Crea la red y la ejecuta"
    topo = SpineLeafTopo()
    net = Mininet( topo=topo,
                   link=TCLink,
                   host=CPULimitedHost )
    net.start()
    print("Topología Spine-Leaf iniciada.")
    CLI( net ) # Inicia la interfaz de línea de comandos de Mininet
    net.stop() # Detiene la red al salir del CLI

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
