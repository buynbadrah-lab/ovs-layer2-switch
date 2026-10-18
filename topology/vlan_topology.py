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
        ip='10.10.10.1/24'
    )

    h2 = net.addHost(
        'h2',
        ip='10.20.20.1/24'
    )

    s1 = net.addSwitch(
        's1',
        protocols='OpenFlow13'
    )

    net.addLink(h1, s1)
    net.addLink(h2, s1)

    net.start()

    s1.cmd(
        'ovs-vsctl set port s1-eth1 tag=10'
    )

    s1.cmd(
        'ovs-vsctl set port s1-eth2 tag=20'
    )

    print("VLAN 10 and VLAN 20 configured")

    CLI(net)

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
