# Link Layer & LANs: Acronyms & key terms

> **NB**
> This sheet is new: If you notice any errors or omissions (or if you add any of the missing hyperlinks!), please do make contact via email/Piazza or send a [pull request](https://help.github.com/articles/about-pull-requests/).
---

## Key terms

### 6.1. Introduction to the Link Layer

| | |
|---|---|
| error detection | |
| error correction | |
| frame | |
| framing | |
| link | |
| link access | |
| network interface card | NIC aka. network interface controller, network adapter, LAN adapter, physical network interface |
| node | |
| reliable delivery | |

### 6.2. Error-Detection and -Correction Techniques

| | |
|---|---|
| bit string | |
| checksum | |
| code | |
| cyclic redundancy check | |
| error correction | |
| error detection | |
| exclusive or | XOR |
| forward error correction | FEC |
| generator polynomial | |
| Internet Checksum | |
| modulo-2 arithmetic | |
| redundancy | |
| parity bit | |
| parity check | |
| polynomial code | |
| undetected (bit) error | |

### 6.3. Multiple Access Links and Protocols

| | |
|---|---|
| active node | |
| buffer | |
| bus | networks |
| ALOHA | |
| [backoff time](https://en.wikipedia.org/wiki/Exponential_backoff) | also backoff window |
| binary exponential backoff | |
| [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth) | |
| [bit time](https://en.wikipedia.org/wiki/Bit_time) | 1/(NIC speed) |
| broadcast link | |
| cable access network | |
| cable modem termination service | CMTS |
| carrier sense multiple access | CSMA |
| carrier sense multiple access with collision detection | CSMA/CD |
| carrier sensing | |
| channel access | method \| problem \| protocol |
| channel partitioning | protocol |
| channel propagation delay | |
| code division multiple access | CDMA |
| collision | |
| collision detection | |
| duplex mode | |
| Data-Over-Cable Service Interface Specifications | DOCSIS |
| efficiency | of a multiple access protocol |
| empty slot | |
| frequency-division multiple access | FDMA |
| half-duplex mode | |
| [IEEE 802.5 Token Ring](https://en.wikipedia.org/wiki/Token_ring) | LAN protocol |
| local area network | LAN |
| polling | delay \| protocol |
| polls | |
| point-to-point link | |
| media\|medium access control | MAC |
| multiple access | method \| problem \| protocol |
| multiplexing | FDM \| CDM \| TDM |
| network adapter | |
| random access | protocol |
| [slot time](https://en.wikipedia.org/wiki/Slot_time) | |
| successful time slot | in slotted ALOHA |
| taking-turns | protocol |
| time-division multiplexing | TDM |
| time frame | (distinct from link Ethernet _frame_) |
| time slot | |
| token | |
| token-passing | protocol |
| | |

#### Summary of MAC protocols

| Protocol | Low load | High load | Coordination & Issues | Examples |
|---|---|---|---|---|
| channel ptx | inefficient | efficient, fair | decentralized | empty slots | (DCMA wireless) |
| random access | efficient | inefficient | decentralized | collision, CS\|CD, backoff | (slotted) ALOHA |
| polling | efficient | efficient, fair | centralized | polling delay, latency, single PoF (master) | Bluetooth
| token-passing | efficient | efficient, fair | "nearly" decentralized | token overhead, latency, single PoF (token) | Token Ring |

### 6.4. Switched Local Area Networks

#### 6.4.1. Link Layer Addressing and ARP

| | |
|---|---|
| Address Resolution Protocol | ARP |
| aging time | |
| ARP module | |
| ARP query packet | |
| ARP response packet | |
| ARP table | |
| [Asynchronous Transfer Mode](https://en.wikipedia.org/wiki/Asynchronous_Transfer_Mode) | ATM |
| broadcast address | `FF-FF-FF-FF-FF-FF` |
| broadcast storm | |
| [Fiber Distributed Data Interface](https://en.wikipedia.org/wiki/Fiber_Distributed_Data_Interface) | FDDI protocol |
| MAC address | aka. burned-in address (BIA), LAN address, (Ethernet) hardware address (EHA), physical address |
| network adapter | |
| network interface | |
| subnet | |
| time-to-live | TTL field |
| [Token Ring](https://en.wikipedia.org/wiki/Token_ring) | IEEE 802.5, protocol |

#### 6.4.2. Ethernet

|  |  |
|---|---|
| Ethernet | protocol |
| [`EtherType`](https://en.wikipedia.org/wiki/EtherType) | type field in [Ethernet frame](https://en.wikipedia.org/wiki/Ethernet_frame) |
| hub | |
| synchronization | |
| repeater | |

#### 6.4.2. Link-Layer Switches

|  |  |
|---|---|
| filtering | |
| forwarding | |
| hub | |
| plug-and-play | |
| self-learning | |
| spanning tree | restriction on Ethernet topology |
| switch | |
| switch poisoning | |
| switching table | |

#### 6.4.4. Virtual Local Area Networks (VLANs)

|  |  |
|---|---|
| MAC-based VLAN | |
| port-based VLAN | |
| traffic isolation | |
| trunking | |
| trunk port | |
| virtual local area network | VLAN |
| VLAN tag | |

#### Comparison switching in the network- and link layer

Adapted from Table 6.1 of Kurose & Ross (page 515):

|                   | Hubs |  Switches | Routers |
|-------------------|------|-----------|---------|
| Collision free, full duplex |  -   |   yes     |   yes   |
| Traffic isolation |  -   | (w/VLAN)  |   yes   |
| Plug-and-play     | yes  |    yes    |    -    |
| Optimal routing   |  -   |     -     |   yes   |

### 6.5. Link Virtualization & MPLS

| | |
|---|---|
| circuit switching | |
| label edge router (LER) | cf. transit router |
| label switching | |
| label switch router (LSR) | aka. label-switched router, transit router |
| Multi-Protocol Label Switching | MPLS |
| overlay network | |
| packet switching | |
| traffic engineering | |
| virtual circuit | aka. virtual connection, virtual channel |
| virtual private network | VPN |

From Shay, _Understanding Data Communications and Networks_ (3e), p. 695:

|  | Virtual Circuit (VC) | Datagram |
|--|--|--|
| congestion control | Routers able to reserve space for anticipated packet arrival | Unexpected packet arrival makes control difficult |
| adaptability | changing conditions may make long-lived VCs suboptimal | each packet routed according to current network state |
| routing overhead | each virtual circuit is routed just once | separate routing decision for each packet |
| ordering | packets arrive in order | packets arrive out of order |
| robustness | packet loss if node/link failure breaks VC connection | packets may be routed around failures |

### 6.6. Center Networking

| | |
|---|---|
| access router | |
| blade | |
| data center | |
| data center network design |
| blade | host in data center |
| border router | |
| fully-connected | topology |
| hierarchical | topology |
| load balancer | |
| load balancing | |
| rack | |
| tier-1 router | |
| tier-2 router | |
| top of rack switch | |

---

## Acronyms

|  | Description |
|--|-------------|
| ALOHA | [Additive Links On-line Hawaii Area](https://en.wikipedia.org/wiki/ALOHAnet) |
| ARP | [Address Resolution Protocol](https://en.wikipedia.org/wiki/Address_Resolution_Protocol) |
| ARQ | [Automatic Repeat Query/reQuest](https://en.wikipedia.org/wiki/Automatic_repeat_request) |
| CDN | [Content Delivery/Distribution Network](https://en.wikipedia.org/wiki/Content_delivery_network) |
| CMTS | [Cable Modem Termination System](https://en.wikipedia.org/wiki/Cable_modem_termination_system) |
| CRC | [Cyclic Redundancy Check](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) |
| CSMA | [Carrier Sense Multiple Access](https://en.wikipedia.org/wiki/Carrier-sense_multiple_access) |
| CSMA/CA | [CSMA with Collision Avoidance](https://en.wikipedia.org/wiki/Carrier-sense_multiple_access_with_collision_avoidance) |
| CSMA/CD | [CSMA with Collision Detection](https://en.wikipedia.org/wiki/Carrier-sense_multiple_access_with_collision_detection) |
| DOCSIS | [Data-Over-Cable Service Interface Specifications](https://en.wikipedia.org/wiki/DOCSIS) |
| ECC | [Error Correcting Code](https://en.wikipedia.org/wiki/Error_detection_and_correction) |
| EDC | [Error Detection and Correction](https://en.wikipedia.org/wiki/Error_detection_and_correction) (or Error Detection Code) |
| EOR | End Of Row (switch, cf. TOR) |
| FEC | [Forwarding Equivalence Class](https://en.wikipedia.org/wiki/Forwarding_equivalence_class) (in MPLS) |
| FDDI | [Fiber Distributed Data Interface](https://en.wikipedia.org/wiki/Fiber_Distributed_Data_Interface) |
| FDM | [Frequency-Division Multiplexing](https://en.wikipedia.org/wiki/Frequency-division_multiplexing) |
| FEC | [Forward Error Correction](https://en.wikipedia.org/wiki/Forward_error_correction) |
| HDLC | [High-level Data Link Control](https://en.wikipedia.org/wiki/High-Level_Data_Link_Control) |
| HFC | [Hybrid Fibre-Coaxial](https://en.wikipedia.org/wiki/Hybrid_fibre-coaxial) (network) |
| IPX | [Internetwork Packet Exchange](https://en.wikipedia.org/wiki/IPX/SPX) (Novell protocol) |
| L2F | [L2 Forwarding](https://en.wikipedia.org/wiki/Layer_2_Forwarding_Protocol) (protocol) |
| L2TP | [Layer 2 Tunneling Protocol](https://en.wikipedia.org/wiki/Layer_2_Tunneling_Protocol) |
| LACP | [Link Aggregation Control Protocol](https://en.wikipedia.org/wiki/Link_aggregation#Link_Aggregation_Control_Protocol) |
| LAN | [Local Area Network](https://en.wikipedia.org/wiki/Local_area_network) |
| LAP | [Link Access Procedure](https://en.wikipedia.org/wiki/Link_access_procedure) |
| LLC | [Logical Link Control](https://en.wikipedia.org/wiki/Logical_link_control) (sublayer) |
| LLDP | [Link Layer Discovery Protocol](https://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol) |
| LSP | [Label-Switched Path](https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching) |
| LSR | [Label-Switch/Switched/Switching Router](https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching#Label_switch_router) |
| MAC | [Medium (or Media) Access Control](https://en.wikipedia.org/wiki/Medium_access_control) (address, sublayer) |
| MDC | [Modular Data Center](https://en.wikipedia.org/wiki/Modular_data_center) |
| MDPC | [MultiDimensional Parity-Check](https://en.wikipedia.org/wiki/Multidimensional_parity-check_code) (code) |
| MPLS | [MultiProtocol Label Switching](https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching) |
| NDP | [Neighbor Discovery Protocol](https://en.wikipedia.org/wiki/Neighbor_Discovery_Protocol) |
| NIC | [Network Interface Controller](https://en.wikipedia.org/wiki/Network_interface_controller)/Card |
| PPP | [Point-to-Point Protocol](https://en.wikipedia.org/wiki/Point-to-Point_Protocol) |
| RDP | [Reliable Data Protocol](https://en.wikipedia.org/wiki/Reliable_Data_Protocol) |
| RF | [Radio Frequency](https://en.wikipedia.org/wiki/Radio_frequency) (wireless channel) |
| RDT | Reliable Data Transfer (protocol) |
| RSTP | [Rapid](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol#Rapid_Spanning_Tree_Protocol) [STP](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol) |
| RSVP | [Resource Reservation Protocol](https://en.wikipedia.org/wiki/Resource_Reservation_Protocol) |
| RSVP-TE | [Resource Reservation Protocol - Traffic Engineering](https://en.wikipedia.org/wiki/RSVP-TE) (extension of RSVP) |
| STP | [Spanning Tree Protocol](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol) |
| TDM | [Time-Division Multiplexing](https://en.wikipedia.org/wiki/Time-division_multiplexing) |
| TTL | [Time To Live](https://en.wikipedia.org/wiki/Time_to_live) |
| TOR | Top Of Rack (switch, cf. EOR) |
| VC | [Virtual Circuit](https://en.wikipedia.org/wiki/Virtual_circuit) |
| VLAN | [Virtual LAN](https://en.wikipedia.org/wiki/Virtual_LAN) |
| WEP | [Wired Equivalent Privacy](https://en.wikipedia.org/wiki/Wired_Equivalent_Privacy) |
| WME | [Wireless Multimedia Extensions](https://en.wikipedia.org/wiki/Wireless_Multimedia_Extensions) (aka. WMM) |
| WMM | [Wi-Fi Multimedia](https://en.wikipedia.org/wiki/Wi-Fi_Multimedia) (aka. WME) |
