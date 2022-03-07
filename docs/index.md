---
layout: default
title: "qoemf"
---

# Project Proposal

We propose designing and demonstrating a framework for measuring QoS (quality of service) for clients connecting to a server over a virtual 
network using [mininet](http://mininet.org/). Alterations on the server-side (e.g. flow control policy, packet drop rates) will be used to simulate 
load or unstable connection. On the client-side, we can recreate DoS and other attacks on the server in a controlled and natural way in order to 
see how the server responds. Our primary objective will be to understand how these various factors influence the quality of experience for clients 
connecting to the network. 

More details forthcoming.


* * *

# Log Book

Over time, we will document our progress on the project here.


### First Bi-weekly Project Update (2/21/2022)

As  of now, most of the  effort has gone to research. Each member has taken time to review papers that relate to our project. Along with this, we’ve reviewed documentation for Mininet and set up a testing environment with Mininet in VM (VirtualMachine). The code creates a simple network and tests when it goes live. A Github repository has been made containing the code and all we’ve written for the report so far.

There are a few tasks that we are currently working on. One major task we are undertaking is researching and deciding on the metrics we’ll be using to run our tests. We are comparing metrics used in different papers to observe what can give us an accurate result. Another major task is working on the technical side of the project. Simply getting the code up and running for QoS tests that we’ll measure with our metrics.

### First Bi-weekly Project Update (3/7/2022)

Firstly, there has been a slight shift in direction of the project. The over-all objective is to give a qualitative evaluation on using Mininet to evaluate various QoS parameters for a Node.js server, given metrics used by other papers that explore QoS in emulated networks.

Further research has been done in the realm of Quality of Service testing, specifically what metrics were used for the testing. The team referenced several different papers in 
order to ultimately decide which metrics to use. https://link.springer.com/chapter/10.1007%2F978-981-16-5120-5_2 The principle paper that was reviewed. From this the metrics 
considered included Throughput, Delay, Packet Loss and Jitter. Though it was noticed that RTT was not considered in the paper. Further, the https://link.springer.com/article/10.1007
/s11042-021-11467-x paper enforces throughput as a necessary metric, and that response time (or RTT) must be considered. https://ieeexplore.ieee.org/document/9251144/authors#authors 
also reinforces the use of delays tests and jitter as QoS measurements.   

The final metrics that have been decided on are: 

- Throughput (total transmitted data in bits)/(total time taken in seconds)
- Delay (time required to transmit the data from sender to receiver)
- Packet loss (the number of packets not delivered to their destination)
- Jitter (the variance in latency)
- RTT (Round-Trip Time)

Our next tasks will include finalizing the emulation code that will be used for testing. Some further research may take place. The purpose for the research is to compare proper 
implementation of an emulation of a network and testing it using a framework. It is the hope that by increasing our knowledge of similar emulations it will inform our approach in our 
project. 

Individual Contributions:

Juan Flores
- Wrote the project updates and updated the project website
- Contributed to research for related works in the project
- Revised project report updates 

Oscar Sandford
- Set up project structure on GitHub: report template in LaTeX, project website
- Written and editorial contributions to project proposal document
- Researched and responded to related works in the report
- Set up experiment environment with Mininet VM, recorded setup replication instructions
- Created driver code for Node.js server-clients topology using the Mininet Python API
- Created a sample Node.js application to test with

Ben Wunderlich
- Wrote the project updates and updated the porject website
- Contributed to research for related works in the project
- Revised experiment environment with Mininet VM

### Update Coming Soon - (TBD)

Duis vitae urna ut felis luctus gravida. Sed aliquam, nisl vel aliquet euismod, erat magna bibendum justo, ac tincidunt elit purus ut sapien. Donec euismod odio magna, quis hendrerit dui hendrerit eget. Proin dapibus mi vel ligula lacinia, a euismod tellus tincidunt. Suspendisse vitae volutpat ligula. Duis placerat vestibulum mi auctor varius. Nullam eget bibendum purus, sed consectetur augue. Pellentesque ut ex vel lorem vestibulum maximus. Maecenas bibendum libero augue, tempor feugiat tellus tristique sit amet.


# Midterm Presentation

Embed a video here?

# Final Presentation

Embed a video here?


# Report 

Embed PDF here. Just a test.
<iframe src="../report/report.pdf" width="100%" height="500px"></iframe>
