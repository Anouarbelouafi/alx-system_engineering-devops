# 0. My first postmortem

>> Issue Summary:

* Duration of the Outage: The outage started at 2:00 PM GMT on January 12, 2024, and ended at 4:30 PM GMT on the same day.
* Impact: During this period, our restaurant’s online ordering system was down. Approximately 60% of our users were affected.
* Root Cause: The root cause was a server overload due to an unexpected surge in traffic.

>> Timeline:

* 2:00 PM: The issue was detected when our monitoring system alerted us about the server overload.
* 2:10 PM: Our engineering team started investigating the issue. Initial assumptions were that it could be a DDoS attack.
* 2:30 PM: The team ruled out the DDoS attack theory and started investigating other potential causes.
* 3:00 PM: The incident was escalated to our senior engineers.
* 4:00 PM: The team identified the root cause as a server overload due to an unexpected surge in traffic.
* 4:30 PM: The incident was resolved by distributing the load to other servers.

>> Root Cause and Resolution

* Root Cause: Our server was not equipped to handle the sudden surge in traffic, which caused the server to overload.
* Resolution: We resolved the issue by distributing the load to other servers. We also added more resources to the affected server to handle future traffic surges.

>> Corrective and Preventative Measures

* Improvements: We need to improve our server capacity planning and load balancing. We also need to enhance our monitoring system to detect such issues earlier.

>> Tasks:

* Upgrade our servers to handle higher traffic.
* Implement a better load balancing solution.
* Enhance our monitoring system to alert us about potential server overloads.

## 1. Make people want to read your postmortem

>> And here’s a hypothetical diagram to illustrate the situation:

User Traffic
    |
    |  /-------------------\
    |  |    Load Balancer  |
    |  \-------------------/
    |            |
    |  /-------------------\        /-------------------\
    |  |     Server 1      |        |     Server 2      |
    |  | Party in progress |        | Ready for a party |
    |  \-------------------/        \-------------------/
