# Link Layer and LANs: Review exercises

> **NB**
> This sheet is new: If you notice any errors or omissions, please do make contact via email/Piazza or send a [pull request](https://help.github.com/articles/about-pull-requests/).

## 6.1. Introduction to the Link Layer

- Describe the sublayers of the **link layer**. Which is "on top"?

1. What do we call the **protocol data unit** (packet) of the link layer?

2. What services are provided by the link layer?

3. Where is the link layer implemented?

4. Do link layer reliable delivery services make those in the transport layer redundant? Explain. **NB:** Ethernet, the dominant L2 protocol, does _not_ offer reliable delivery (only EDC).

5. If _all_ links were to provide reliable delivery service, would the TCP reliable delivery service be redundant? Explain.

6. Why not leave reliability to the transport layer completely?

---

## 6.2. Error-Detection and -Correction Techniques

1. Describe how a **error detection** scheme is employed to provide a reliable delivery service.

2. (Extra for Experts:) Compare/contrast the meanings of **source coding**, **channel coding**, and **cryptographic coding**; explain the relevance of each in communication networks, and the layer(s) in which it might be implemented.

### 6.2.1. Parity checks

1. Describe how the **parity bit** is chosen for an **even** (or **odd**) parity check.

2. How is the parity bit used to **detect** errors?

3. Is the choice between these alternatives significant? Explain.

4. Explain how/why **parity bit** scheme is only able to detect 50% of **burst errors**?

5. Explain how a **two-dimensional parity bit** scheme is able to both detect and **correct** a single error.

6. Explain how a two dimensional parity check is able to detect (but not correct) any combination of two errors.

7. (Extra for Experts:) Show that the parity bit in the "bottom-right corner" of the augmented array acts a parity bit for both of the final row and final column.

### 6.2.1. Checksumming methods

1. Describe the **Internet Checksum**.

2. In which internet protocols is is applied? To which fields?

3. Checksums are not used in the link layer, where cyclic redundancy checks are used: Why not apply one "best" method in all layers?

4. What kind(s) of error would a checksum not detect? Do you expect a checksum to be more reliable than a parity check?

### 6.2.3. Cyclic redundancy checks

1. Give examples of protocols in which CRC are used?

2. Define **modulo-2** addition and -subtraction. Are bits carried/borrowed if multi-bit patterns are added/subtracted?

3. Explain why modulo-2 arithmetic operates like an clock face (with numerals at 12 o'clock and 6 o'clock).

4. When calculating the EDC bits, the data bit-string is shifted by "r" bits (in the notation of Kurose & Ross): Explain why the shift is necessary, and why r is the degree of the generator polynomial.

5. Comment on the performance of a well-designed r-bit CRC code in the face of burst errors.

6. Suppose that the transmitted polynomial T is received as T' := T + E, where E is an error.
   - Show that rem(T', G) = rem(E, G)?
   - Which errors would be undetected by the CRC scheme with generator G?

7. (Extra for Experts:) Describe, in terms of bit patterns, the errors that a CRC can/not detect.

8. (Extra for Experts:) Can a **parity check** be expressed as a CRC? Explain.

9. (Extra for Experts:) Can CRC codes perform error **correction**? Comment briefly.

---

## 6.3. Multiple Access Links and Protocols

1. Recall examples of shared physical media.

2. What is a **collision**?

3. What is the purpose of a **multiple access protocol**?

4. Outline three or four desirable properties of an "ideal" multiple access protocol (with rate R bits/second, say).

5. Identify or describe three main categories of multiple access protocols.

6. Kurose & Ross discuss multiple access protocols in the context of the link layer as opposed to the network layer: Why?

7. Contrast the meanings of **efficiency** and **fairness** in the context of channel access.

### 6.3.1. Channel-Partitioning Protocols

1. Identify and describe three classes of **channel partitioning** protocols.

2. Explain the appeal and the drawback(s) of **TDMA** and of **FDMA**.

#### 6.3.2. Random Access protocols

1. Describe, in general terms, how **random access** protocols work.

2. Describe the **slotted ALOHA** protocol.

3. Explain the appeal of slotted ALOHA relative to channel partitioning.

4. In the context of ALOHA, explain the meaning of **successful slot**?

5. Each of the N nodes in a slotted ALOHA network transmits independently with probability p.
   - Determine the probability that a specified node k transmits successfully in a given time slot.
   - What, then, is the probability of successful transmission (by any node) in that time slot?
   - (Extra for Experts:) Find the values of p that extremizes the expression for efficiency.
   - (Extra for Experts:) At this optimal p, determine the efficiency of a heavily-loaded system in the limit "N goes to infinity"?

6. Repeat the preceding efficiency calculations for "pure" ALOHA.

7. Explain the trade-off that arises between **slotted ALOHA** and "pure" **ALOHA**.

8. Are collisions more- or less likely in pure- or unslotted ALOHA? Explain briefly.

9. In the context of multiple access protocol, outline analogies between protocols of human conversation and:
   - **carrier sensing**
   - **collision detection**

10. With the aid of a diagram, explain how collisions are inevitable even if carrier sensing is employed.

11. How does **collision detection** improve the performance of a multiple access protocol.

12. How soon after a collision is detected is a node in a CSMA/CD network able to re-transmit?

13. Explain how a re-transmission delay is chosen by a **binary exponential backoff** algorithm, and why this process is sensible.

14. How is the backoff time defined in the **Ethernet** protocol.

15. Identify or describe the factor(s) influencing the efficiency of a DSMA/CD deployment?

16. Why must a node wait for a _random_ length of time (as opposed to a fixed length interval) after a collision is detected. (How about a fixed period that depends on the node index?)

17. Identify or describe physical factors dictating the efficiency of a CSMA/CD network.

18. Describe the physical mechanism by which an adapter is able to detect collisions.

### 6.3.3. Taking-Turns Protocols: Polling and token-passing

1. Contrast potential sources of inefficiency of protocols based on "taking-turns" with those based on **random access**.

2. Explain the workings of a protocol based on **polling**.

3. Outline the positive and negative characteristic(s) of **polling** protocols.

4. Explain the workings of a protocol based on **token-passing**.

5. What challenge(s) does token passing raise for the protocol designer?

6. Identify an existing protocol based on **polling**; on **token-passing**.

### 6.3.4. DOCSIS: The Link-Layer Protocol for Cable Internet Access

> This section is not examinable.

1. The multiple access problem does not arise on the downstream channel of a cable access network: Why?

2. Explain how each of the following elements are incorporated into the DOCSIS protocol:
   - Channel partitioning
   - Random access
   - Centrally-allocated slots

---

## 6.4. Switched Local Area Networks

### 6.4.1 Link-Layer Addressing and ARP

1. Recall the "addresses" employed at each layer of the Internet protocol stack.

2. Provide at least two commonly-used synonyms for "link-layer addresses".

3. Explain how the MAC address space is managed to maintain uniqueness of addresses across devices.

4. Contrast **IPv4 addresses** and **MAC addresses**.

5. How many MAC addresses are (typically) associated with a host? With a router?

6. Contrast the meaning of **adapter** and **interface**.

7. What happens when a frame's destination MAC address doesn't match that of a receiving interface? What if the frame has the MAC **broadcast address**?

8. What is the role of the **Address Resolution Protocol** (ARP).

9. Compare and contrast the Address Resolution Protocol (ARP) and the **Domain Name System** (DNS).

10. Identify or describe the (most important) columns of an **ARP table**.

11. What is the role of the **TTL** field in **ARP tables**? How does this compare with its role in **IP packets**? With its role in DNS?

12. Which Ethernet nodes contain an **ARP table**?

13. What is an **ARP module**?

14. What fields are carried by an **ARP packet**?

15. How would you distinguish a frame carrying an **ARP query packet** from one carrying an **ARP response packet**?

16. What happens when a host receives an **ARP query packet**?

17. What is a typical (initial) value for **TTL field** in an ARP table entry?

18. "_ARP is plug-and-play_": Explain briefly.

19. "_ARP straddles the boundary between the link and network layers_": Discuss briefly.

20. How can a sending host tell whether a destination interface lives on the same **subnet**?

21. Describe how does an IP packet reach a destination off the subnet of the sender?

### 6.4.2. Ethernet

1. Outline some of the factors that may have contributed to the success of **Ethernet** as the dominant wired LAN technology.

2. Contrast early **hub** devices with modern **switch** devices. In what sense is a switch "smarter" than a hub?

3. Explain the role of the **preamble** field in an Ethernet frame.

4. What happens when an Ethernet frame fails the CRC check at the receiving interface?

5. Ethernet communication might be described as "unreliable" and "connectionless": Explain each of these terms.

6. If Ethernet does not provide a reliable service, how are LAN users assured of reliable communication?

7. Identify or describe the **MAC protocol** employed in Ethernet networks.

8. Identify or describe each of the fields in the Ethernet frame structure.

9. Which protocol layer(s) does Ethernet cover? Explain.

10. What do different members of the Ethernet family have in common and how do they differ?

11. Explain the identifier in, for example, the 100BASE-T Ethernet standard.

### 6.4.2. Link-Layer Switches

1. Outline key differences between  **switches** and **buses** in Ethernet networks.

2. Compare and contrast the configuration and features of (network layer) **routers** and (link layer) **switches**.

3. Compare and contrast (level-2) **switches** and (level-3) **routers**.

4. Explain how the **switch table** in an Ethernet **switch** is configured.

### 6.4.4. Virtual Local Area Networks (VLANs)

1. Explain the notion of traffic isolation.

2. Explain how **virtual LANs** (VLANs) provides for:
   - Traffic isolation
   - Efficient utilization of switching hardware
   - Flexible user management e.g. physical transfers between organization units

3. How are packets transferred _between_ VLANs?

4. Explain the notion of VLAN **trunking** and **trunk port**. How is trunking implemented?

5. What would be required to connect users of a given VLAN that that are located in different physical locations in the absence of trunking? (i.e. What savings does trunking offer?)

6. Contrast **port-based** VLANs with **MAC-based** VLANs.

7. Explain the role of the (optional) **VLAN tag** (IEEE 802.1Q tag) in the Ethernet frame.

---

### 6.5. Link Virtualization & MPLS

- How might **MPLS** forwarding decisions differ from those of **IP**?
- Explain the difference between **circuit switching**, **packet switching**, and **label switching** (as in MPLS); identify a network that employs each case.
- Outline a few scenarios in which **MPLS** may be employed in the context of traffic engineering.

1. Use an example to explain the meaning of **overlay network**.

2. What is a [**virtual circuit**](https://en.wikipedia.org/wiki/Virtual_circuit)? How does it relate to **circuit switching** and **packet switching**?

3. Explain the original motivation for the development of the **Multiprotocol Label Switching** (MPLS) protocol.

4. In what sense is MPLS (_Multiprotocol_ Label Switching) "multiprotocol".

5. (Extra for Experts:) With which protocol layer is MPLS associated? Discuss.

6. Compare and contrast MPLS with software defined networking (SDN) technology.

7. Explain how **label switching** improves _forwarding efficiency_.

8. Explain how **label switching** increases _routing flexibility_ and _robustness_.

9. "_Current interest in MPLS is relates to **traffic management/engineering** (as opposed to switching speed)_". Discuss briefly.

---

## 6.6. Center Networking

1. What are the roles of a **load balancer** within a data centre?

2. Outline a similarity between data centre load balancing and **Network Address Translation** (NAT).

3. Explain why data centre load balancing might be described as "application-layer routing".

4. Describe the **topology** of a modern data centre. What are the benefits of this design?

5. (Extra for Experts:) Briefly describe one recent trend in data centre networking technology.

---

## 6.7. Retrospective: A day in the life of a Web Page Request

> This material draws from all other modules.​
