#importação da biblioteca P4-Utils

from p4utils.mininetlib.network_API import NetworkAPI

#Definições gerais da rede
net = NetworkAPI()

#Definição da rede
net.addP4Switch('s1')
net.addP4Switch('s2')
net.addP4Switch('s3')
net.addP4Switch('s4')
net.addP4Switch('s5')

net.addHost('h2')

net.addLink("", "")
