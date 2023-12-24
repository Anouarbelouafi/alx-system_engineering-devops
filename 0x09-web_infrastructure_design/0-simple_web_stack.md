# The issues with the given infrastructure are

- SPOF (Single Point of Failure): The infrastructure has no redundancy that can help in avoiding SPOFs. Any single failure in any part of the system will cause the entire system to stop working.

- Downtime when maintenance needed: Deploying new code requires restarting the web server, which results in downtime. The infrastructure has only one server and one database, which is used to make the deployment and maintenance, hence no way users will access the website during that period.

- Cannot scale if too much incoming traffic: The infrastructure cannot scale if there is too much incoming traffic because there is no second server in the system to share loads, and the system will be overloaded.
