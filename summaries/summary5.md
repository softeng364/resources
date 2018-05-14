# Network control plane: Acronyms & key terms

> **NB**
> This sheet is new: If you notice any errors or omissions (or if you add any of the missing hyperlinks!), please do make contact via email/Piazza or send a [pull request](https://help.github.com/articles/about-pull-requests/).

## Key terms

### 5.1. Introduction

| | |
|-|-|
| [control plane](https://en.wikipedia.org/wiki/Control_plane) | |
| [data plane](en.wikipedia.org/wiki/Data_plane) | aka. forwarding plane, user plane |
| [management plane](https://en.wikipedia.org/wiki/Management_plane) | |

### 5.2. Routing Algorithms

| | |
|-|-|
| [all-pairs shortest path problem](https://en.wikipedia.org/wiki/Shortest_path_problem#All-pairs_shortest_paths) | |
| admininstrative weights | link costs |
| bandwidth | in bits/second |
| cycle | aka. circuit |
| Bellman-Ford algorithm | |
| Dijkstra's algorithm | |
| distance vector protocol | aka. IGP type 2 |
| [dynamic routing](https://en.wikipedia.org/wiki/Dynamic_routing) | aka. adaptive routing |
| [forwarding table](https://en.wikipedia.org/wiki/Forwarding_information_base) | aka. forwarding information base (FIB) |
| graph | |
| least-cost path | |
| link | aka. arc/branch/edge (cf. chord, twig) |
| [link aggregation](https://en.wikipedia.org/wiki/Link_aggregation) | for throughput and redundancy |
| link-state protocol | aka. IGP type 1 |
| link utilization | |
| [minimax path](https://en.wikipedia.org/wiki/Widest_path_problem) | |
| node | aka. vertex |
| path bandwitch | aka. path capacity |
| [route poisoning](https://en.wikipedia.org/wiki/Route_poisoning) | |
| [routing loop](https://en.wikipedia.org/wiki/Routing_loop_problem) | aka. forwarding loop |
| [routing table](https://en.wikipedia.org/wiki/Routing_table) | aka. routing information base (FIB) |
| shortest path | |
| [shortest-path tree](https://en.wikipedia.org/wiki/Shortest-path_tree) | |
| [single-source shortest path problem](https://en.wikipedia.org/wiki/Shortest_path_problem#Single-source_shortest_paths) | |
| [static routing](https://en.wikipedia.org/wiki/Static_routing) | |
| topology | |
| [traffic engineering](https://en.wikipedia.org/wiki/Internet_traffic_engineering) | |
| [tree](https://en.wikipedia.org/wiki/Tree_(graph_theory)) | |
| [widest path](https://en.wikipedia.org/wiki/Widest_path_problem) | |

### 5.3. Intra-AS Routing in the Internet: OSPF

| | |
|-|-|
| area | |
| area number | |
| area border router | ABR |
| autonomous system | AS |
| autonomous system boundary router | ASBR |
| autonomous system number | ASN |
| backbone router | BR |
| internal router | AR |
| hierarchy | |
| [interior gateway protocol](https://en.wikipedia.org/wiki/Interior_gateway_protocol) | |
| IS-IS | |
| multicast | |
| OSPF | |
| OSPF area | |

### 5.4. Routing Among the ISPs: BGP

| | |
|-|-|
| [access network](https://en.wikipedia.org/wiki/Access_network) | |
| anycast  | cf. unicast, broadcast, multicast, geocast |
| `AS_PATH` | attribute |
| [autonomous system](https://en.wikipedia.org/wiki/Autonomous_system_(Internet)) | AS |
| autonomous system number | ASN |
| [backbone network](https://en.wikipedia.org/wiki/Backbone_network) | aka. core network |
| BGP route | |
| [Domain name registrar](https://en.wikipedia.org/wiki/Domain_name_registrar) | |
| [exterior gateway protocol](https://en.wikipedia.org/wiki/Exterior_gateway_protocol) | |
| [hot potato routing](https://en.wikipedia.org/wiki/Hot-potato_and_cold-potato_routing) | aka. nearest-exit routing |
| internet presence | |
| IP-anycast | |
| `LOCAL_PREF` | attribute |
| `NEXT_HOP` | attribute |
| provider network | |
| path vector protocol | |
| [peering](https://en.wikipedia.org/wiki/Peering) |
| [routing policy](https://en.wikipedia.org/wiki/Routing_protocol) | |

### 5.5. The SDN Control Plane

|  |  |
|--|--|
| flow table | |
| label-based forwarding | see MPLS in Chapter 6 |
| input port | aka. ingress port |
| [middlebox](https://en.wikipedia.org/wiki/Middlebox) | see [IETF RFC 3234](https://tools.ietf.org/html/rfc3234) |
| monolithic | |
| [multipath routing](https://en.wikipedia.org/wiki/Multipath_routing) | |
| network controller | |
| northbound interface | aka. application-controller plane interface |
| [ONOS](https://en.wikipedia.org/wiki/ONOS) | The Linux Foundation since 2015 |
| Open Daylight | ODL, The Linux Foundation (also) |
| OpenFlow | |
| output port | aka. egress port |
| southbound interface | aka. data-controller plane interface |
| unbundling | |

### 5.6. ICMP: The Internet Control Message Protocol

| | |
|-|-|
| echo request | |
| echo response | |
| ICMP code | |
| ICMP field | |
| latency | |
| `ping` | network utility |
| round-trip time | RTT |
| router advertisement | |
| router discovery | |
| source quench | |
| `traceroute` | network utility |
| time-to-live | TTL aka. hop limit |
| unreachable | network/host/protocol/port |
| unknown | network/host |

### 5.7. Network Management & SNMP

| | |
|-|-|
| managing server | an application |
| managed device | hardware or software
| managed objects | on/within managed device |
| managment Information Base | (MIB) features, configuration parameters, counters, state/errors |
| managment agent | running on each managed device |
| management protocol | for communication between managing server and -devices |
| features | |
| configuration | |
| counters | and statistics |

---

## Acronyms

|         | Description                        |
|---------|------------------------------------|
| A-CPI | Application-Controller Plane Interface (aka. [NBI](https://en.wikipedia.org/wiki/Northbound_interface)) |
| ABR | Area Border Router |
| AD | [Administrative Distance](https://en.wikipedia.org/wiki/Administrative_distance) |
| AS | [Autonomous System](https://en.wikipedia.org/wiki/Autonomous_system_(Internet)) |
| ASBR | Autonomous System Boundary Router |
| ASIC | [Application-Specific Integrated Circuit](https://en.wikipedia.org/wiki/Application-specific_integrated_circuit) |
| ASN | [Autonomous System](https://en.wikipedia.org/wiki/Autonomous_system_(Internet)) Number |
| BGP | [Border Gateway Protocol](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) |
| BR | Backbone Router |
| D-CPI | Data-Controller Plane Interface (aka. [SBI](en.wikipedia.org/wiki/Southbound_interface)) |
| DF | "Don't Fragment" (ICMP flag) |
| DV | [Distance-Vector](https://en.wikipedia.org/wiki/Distance-vector_routing_protocol) (routing protocol) |
| DVMRP | [Distance-Vector Multicast Routing Protocol](https://en.wikipedia.org/wiki/Distance_Vector_Multicast_Routing_Protocol) |
| EGP | [Exterior Gateway Protocol](https://en.wikipedia.org/wiki/Exterior_gateway_protocol) (preceded BGP) |
| EIGRP | [Enhanced IGRP](https://en.wikipedia.org/wiki/Enhanced_Interior_Gateway_Routing_Protocol)  |
| FIB | [Forwarding Information Base](https://en.wikipedia.org/wiki/Forwarding_information_base) (aka. Forwarding Table, MAC Table) |
| ICANN | [Internet Corporation for Assigned Names and Numbers](https://en.wikipedia.org/wiki/ICANN) |
| ICMP | [Internet Control Message Protocol](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) |
| IDRP | Interdomain Routing Protocol |
| IGP | [Interior Gateway Protocol](https://en.wikipedia.org/wiki/Interior_gateway_protocol) |
| IGRP | [Interior Gateway Routing Protocol](https://en.wikipedia.org/wiki/Interior_Gateway_Routing_Protocol) (an IGP from Cisco) |
| IGMP | [Internet Group Management Protocol](https://en.wikipedia.org/wiki/Internet_Group_Management_Protocol) |
| IR | Internal Router |
| IS-IS | [Intermediate System to Intermediate System](https://en.wikipedia.org/wiki/IS-IS) (routing protocol) |
| LS | [Link-State](https://en.wikipedia.org/wiki/Link-state_routing_protocol) (routing protocol) |
| LSA | [Link-State Advertisement](https://en.wikipedia.org/wiki/Link-state_advertisement) |
| LSP | [Link State Packet](https://en.wikipedia.org/wiki/Link_state_packet) |
| MIB | [Management Information Base](https://en.wikipedia.org/wiki/Management_information_base) |
| MOSPF | [Multicast](https://en.wikipedia.org/wiki/Multicast) [OSPF](https://en.wikipedia.org/wiki/Open_Shortest_Path_First) |
| NBI | [Northbound Interface](https://en.wikipedia.org/wiki/Northbound_interface) |
| NFV | [Network Function Virtualization](https://en.wikipedia.org/wiki/Network_function_virtualization) |
| NLRI | Network Layer Reachability Information |
| ODL | [OpenDaylight](https://en.wikipedia.org/wiki/OpenDaylight_Project) ([SDN](https://en.wikipedia.org/wiki/Software-defined_networking) controller) |
| OLSR | [Optimized Link State Routing](https://en.wikipedia.org/wiki/Optimized_Link_State_Routing_Protocol) (protocol) |
| ONOS | [Open Network Operating System](https://en.wikipedia.org/wiki/ONOS) ([SDN](https://en.wikipedia.org/wiki/Software-defined_networking) controller) |
| OSPF | [Open Shortest Path First](https://en.wikipedia.org/wiki/Open_Shortest_Path_First) |
| OVSDB | [Open vSwitch Database](https://en.wikipedia.org/wiki/Open_vSwitch) (management protocol) |
| PBF | [Policy-Based Forwarding]() |
| PBR | [Policy-Based Routing](https://en.wikipedia.org/wiki/Policy-based_routing) |
| PIM | [Protocol-Independent Multicast](https://en.wikipedia.org/wiki/Protocol_Independent_Multicast) (routing protocol) |
| RA | Router Agent |
| RA | Router Advertisement |
| REST | [REpresentational State Transfer](https://en.wikipedia.org/wiki/Representational_state_transfer) |
| RIP | [Routing Information Protocol](https://en.wikipedia.org/wiki/Routing_Information_Protocol) |
| RPF | [Reverse Path Forwarding](https://en.wikipedia.org/wiki/Reverse_path_forwarding) |
| SAL | Service Abstraction Layer |
| SBI | [Southbound Interface](en.wikipedia.org/wiki/Southbound_interface) |
| SDN | [Software Defined Networking](https://en.wikipedia.org/wiki/Software-defined_networking) |
| SMI | [Structure of Management Information](https://en.wikipedia.org/wiki/Structure_of_Management_Information) (in SNMP) |
| SNMP | [Simple Network Management Protocol](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol) |
| SOAP | [Simple Object Access Protocol](https://en.wikipedia.org/wiki/SOAP) |
| SSM | [Source-Specific Multicast](https://en.wikipedia.org/wiki/Source-specific_multicast) (routing protocol) |
| STP | [Spanning Tree Protocol](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol) |
| TTL | [Time To Live](https://en.wikipedia.org/wiki/Time_to_live) (aka. hop limit) |
| VMM | Virtual Machine Monitor (aka. [hypervisor](https://en.wikipedia.org/wiki/Hypervisor)) |
| VRF | [Virtual Routing and Forwarding](https://en.wikipedia.org/wiki/Virtual_routing_and_forwarding) |
| WSDL | [Web Services Description Language](https://en.wikipedia.org/wiki/Web_Services_Description_Language) |

---
