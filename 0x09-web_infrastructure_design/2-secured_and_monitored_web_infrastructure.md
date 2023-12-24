# Issues with the given infrastructure

+ Terminating SSL at the load balancer level: Terminating SSL at the load balancer level can be an issue because traffic between the load balancer and the app servers would be unencrypted, leaving the app servers vulnerable to packet sniffing or ARP poisoning.
+ Having only one MySQL server capable of accepting writes: Having only one MySQL server capable of accepting writes can be an issue because it can cause a single point of failure. If the server fails, the website will be unavailable.
+ Having servers with all the same components (database, web server, and application server): Having servers with all the same components can be a problem because their consumption will not grow the same way between each of them. Hence, there is a need to have more database servers to handle the load.
