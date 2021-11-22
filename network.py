#importação da biblioteca P4-Utils

from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

#Definições gerais da rede
net.setLogLevel('info')
net.enableCli()

#Definição da rede
#Switches
net.addP4Switch('s1')
net.addP4Switch('s2')
net.addP4Switch('s3')
net.addP4Switch('s4')
net.addP4Switch('s5')

 #Hosts
net.addHost('h1')
net.addHost('h2')

#Conexões entre os dispositivos da rede.
net.addLink("", "")


#Opção gerais dos nós
net.enableCpuPortAll()     #
net.disablePcapDumpAll()   #
net.disableLogAll()        #
net.enableCli()            #
net.startNetwork()         #
