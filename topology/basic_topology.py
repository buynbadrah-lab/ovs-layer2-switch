from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel


def topology():

    net = Mininet(
        switch=OVSSwitch,
        controller=None
    )

    h1 = net.addHost(
        'h1',
        ip='10.0.0.1/24'
    )

    h2 = net.addHost(
        'h2',
        ip='10.0.0.2/24'
    )

    s1 = net.addSwitch(
        's1',
        protocols='OpenFlow13'
    )

    net.addLink(h1, s1)
    net.addLink(h2, s1)

    net.start()

    print("Basic OVS Layer 2 topology started")

    CLI(net)

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
