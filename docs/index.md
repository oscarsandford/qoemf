---
layout: default
title: "qoemf"
---

# Project Proposal

This project surveys a set of well-defined, domain-agnostic quality of service parameters and defines each parameter's importance in the context of different networking domains. Such domains include online multiplayer gaming, peer-to-peer file transfer services, video streaming, and financial applications. 

Note: 
This paper has had a redirection in purpose and approach since the original intention.  Due to the difficulty of designing and implementing the target topology with Nodejs/Nginx in Mininet, indecision on protocol levels to measure, and time restrictions, our original plan to load test a QoS measurement framework became unfeasible. We also found that our requirements for the framework were becoming narrower and narrower, and that results would not be very meaningful. After further research, a new objective was decided by the team. Below you will find our new proposed project with adjusted objectives and time-frame. Please note that despite our new direction, we are still working within the QoS field, focusing now on qualitative analysis and evaluation, instead of emulation and measurement. As such, the research we completed before is still applicable to the new proposal. We have added to our related works list, and have not removed any of the sources we originally listed. More sources will be added to the citation list.  

**New Objective**

To survey a set of well-defined, domain-agnostic quality of service parameters and define each parameter's importance in the context of different networking domains. Such domains 
include online multiplayer gaming, peer-to-peer file transfer services, video streaming, and financial applications.

**Overview**

This study will focus on quality of service, as it is easier to evaluate due to its quantitative nature. QoS requirements stem from domain and system requirements, rather than only the requirements of an user-end, which can be difficult to measure. In the interest of isolating the analysis of a network to its technical requirements and how well organizations correctly prioritize the maintenance of their system in order to best fit a generalized view of the customers' needs, we will only consider quality of service (QoS) in this study.  

**Related Works**

Countless studies in computer networking have addressed quality of service when it comes to the development and analysis of new algorithms, measurements on the efficacy of existing solutions, as well as domain-specific requirements for specific systems. 
However, various domains have differing standards on quality of service for their applications. It is difficult to correctly understand what it means for an application to have a "good" quality of service, especially under the requirements of the application domain itself, without giving weights, or prioritization, to certain parameters. We aim to provide an evaluation of each general QoS parameter (as outlined by [1]) based on analysis of domain requirements for each domain. This work is necessary because QoS has been analyzed in certain domains, but there does not yet seem to be a survey on how common QoS measurement parameters are prioritized in each domain. As a result of this survey, readers will come to understand the most meaningful QoS measurements for each domain.

**Timeline**

- Jan 31st - Feb 13th: Create project outline, gather resources, outline program and create git repository. 
- Feb 14th - Feb 27th: Build testing environment and further research on related papers.
- Feb 28th - Mar 13th: Redirection of project. Gathered more sources and updated our project paper.
- Mar 14th - Mar 27th: Third Bi-weekly update. Gather new research materials, analyze papers and their target domain(s), evaluate QoS parameters outline - in related work with respect to their use/priority in target domain 
- Mar 28th - Apr 4th: Final Presentation on findings and preliminary evaluations Continue to work on the final report.
- Apr 5th - Apr 11th: Finalize report and turn it in


* * *

# Log Book

THe progression of our project is documented here. We started with an initial idea to do simulation and QoS measurement in Mininet, and then evolved our idea into the new proposal (as seen above).


### First Bi-weekly Project Update (2/21/2022)

As  of now, most of the  effort has gone to research. Each member has taken time to review papers that relate to our project. Along with this, we’ve reviewed documentation for Mininet and set up a testing environment with Mininet in VM (VirtualMachine). The code creates a simple network and tests when it goes live. A Github repository has been made containing the code and all we’ve written for the report so far.

There are a few tasks that we are currently working on. One major task we are undertaking is researching and deciding on the metrics we’ll be using to run our tests. We are comparing metrics used in different papers to observe what can give us an accurate result. Another major task is working on the technical side of the project. Simply getting the code up and running for QoS tests that we’ll measure with our metrics.

### Second Bi-weekly Project Update (3/7/2022)

Firstly, there has been a slight shift in direction of the project. The over-all objective is to give a qualitative evaluation on using Mininet to evaluate various QoS parameters fora Node.js server, given metrics used by other papers that explore QoS in emulated networks.

Further research has been done in the realm of Quality of Service testing, specifically what metrics were used for the testing. The team referenced several different papers in order to ultimately decide which metrics to use. https://link.springer.com/chapter/10.1007%2F978-981-16-5120-5_2 The principle paper that was reviewed. From this the metrics considered included Throughput, Delay, Packet Loss and Jitter. Though it was noticed that RTT was not considered in the paper. Further, the https://link.springer.com/article/10.1007/s11042-021-11467-x paper enforces throughput as a necessary metric, and that response time (or RTT) must be considered. https://ieeexplore.ieee.org/document/9251144/authors#authors also reinforces the use of delays tests and jitter as QoS measurements.   

The final metrics that have been decided on are: 

- Throughput (total transmitted data in bits)/(total time taken in seconds)
- Delay (time required to transmit the data from sender to receiver)
- Packet loss (the number of packets not delivered to their destination)
- Jitter (the variance in latency)
- RTT (Round-Trip Time)

Our next tasks will include finalizing the emulation code that will be used for testing. Some further research may take place. The purpose for the research is to compare proper implementation of an emulation of a network and testing it using a framework. It is the hope that by increasing our knowledge of similar emulations it will inform our approach in our project. 

**Individual Contributions:**

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
- Wrote the project updates and updated the project website
- Contributed to research for related works in the project
- Revised experiment environment with Mininet VM

### Revised Project Proposal Posted (3/13/2022)

See the proposal at the top of the page. At this point, our completed and upcoming tasks on the timeline where as follows:

Passed:
- Jan 31st - Feb 13th: Create project outline, gather resources, outline program and create git repository. 
- Feb 14th - Feb 27th: Build testing environment and further research on related papers.
- Feb 28th - Mar 13th: Redirection of project. Gathered more sources and updated our project paper.

Upcoming:
- Mar 14th - Mar 27th: Third Bi-weekly update. Gather new research materials, analyze papers and their target domain(s), evaluate QoS parameters outline - in related work with respect to their use/priority in target domain 
- Mar 28th - Apr 4th: Final Presentation on findings and preliminary evaluations Continue to work on the final report.
- Apr 5th - Apr 11th: Finalize report and turn it in


### Third Bi-weekly Project Update (3/23/2022)

Project Update:
Since the last project update, we have changed the objective and purpose of the project. We have a new project proposal that can be reviewed at the beginning of the project website. Below you can find the new project objective, overview, the work we have completed for the new objective and the next steps to finalize the project. 

New Objective: 
To survey a set of well-defined, domain-agnostic quality of service parameters and define each parameter's importance in the context of different networking domains. Such domains include online multiplayer gaming, peer-to-peer file transfer services, video streaming, and financial applications. Our objective includes analyzing 20-25 different papers and additional sources for insight. 

Overview: 
This study will focus on quality of service, as it is easier to evaluate due to its quantitative nature. QoS requirements stem from domain and system requirements, rather than only the requirements of an user-end, which can be difficult to measure. In the interest of isolating the analysis of a network to its technical requirements and how well organizations correctly prioritize the maintenance of their system in order to best fit a generalized view of the customers' needs, we will only consider quality of service (QoS) in this study.

Work Completed:
We composed the taxonomy of quality of service parameters including quantitative security, performance and importance metrics; and non-measurable policies that influence in the metrics. 
We derived this hierarchy based on the specifications found in [1] with additional notes:

Metrics cover the following attributes:
- Security (robustness against malicious action)
	- Confidentiality (information is received by intended party)
	- Integrity (information remains accurate)
- Performance
	- Timeliness (e.g. delay)
	- Precision (i.e. consistency, e.g. jitter)
	- Accuracy (i.e. lack of errors, e.g. packet loss)
	- Combinations (i.e. of the above, e.g. throughput: precision over time)
- Relative Importance (i.e. cost of given service to user)

Policies involve the following:
- Levels of Service (i.e. commitment to a task, e.g. guaranteed or best-effort)
	- Availability
- Management (i.e. accept lower quality of service instead of no service at all)

The metrics cover the quantifiable aspects of a system’s components. The policies dictate the behavior of these components. The domains that we are reviewing currently 
include online multiplayer gaming, peer-to-peer file transfer services, video streaming, and financial applications. We are currently halfway through analyzing papers that 
propose solutions to pressing QoS problems, revealing the importance of certain QoS parameters in these domains.  
We aggregated and cross-validated the quality of service measurements used in related works, such as domain-agnostic network simulations, with the taxonomy above. 

Next steps: 
Create domain requirement diagrams that compare the importance of each parameter with respect to the domain requirements.
Capture other sources for additional insight (such as company engineering blogs).

**Individual Contributions:**

Juan Flores
- Wrote the project updates and updated the project website
- Performed analysis on papers from the compiled library
- Revised project report updates
- Responded to comments, feedback and questions on discussion board

Oscar Sandford
- Outlined networking domains of interest
- Researched and analyzed different papers for analysis
- Written and editorial contributions to project proposal document
- Responded to comments, feedback and questions on discussion board
- Revised updates and new project proposal
- Composed introduction, related work, and approach sections

Ben Wunderlich
- Researched and analyzed different papers for analysis
- Revised updates and new project proposal


[1] B. Sabata, S. Chatterjee, M. Davis, J.J. Sydir, and T.F. Lawrence, “Taxonomy for qos specifications,” in Proceedings Third International Workshop on ObjectOriented 
Real-Time Dependable Systems, 1997, pp. 100–107.



# Final Presentation

<iframe src="https://drive.google.com/file/d/1AxZUVzWk-ZuPe1CXitZ_XOE1LmRy0fPg/preview" width="640" height="480" allow="autoplay"></iframe>



# Report 

<iframe src="csc466_report.pdf" width="100%" height="500px"></iframe>
