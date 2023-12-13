### Outage : 
Inability to log in or access accounts due to a service disruption.

### Duration:
The outage occurred on October 5, 2023, from 9:00 AM to 10:00 AM (GMT).

### Impact:
Users experienced a complete inability to log in or access their accounts during the outage period. This issue affected 40% of the user base, leading to frustration and an influx of support requests.

### Root Cause:
The root cause of the outage was identified as a database connectivity issue caused by a misconfiguration during a routine maintenance activity.

### Timeline:

### Detection:
The issue was detected at 9:00 AM 

### Actions Taken:

Investigatiion into the reported login failures.
Initial assumption: High traffic or a potential external attack impacting the authentication service.

### Escalation:
The development team initially managed the incident, and it was later escalated to the system reliability team once database and network issues were ruled out.

### Resolution:

Intermittent failures arose due to an issue with the external identity provider. To restore service stability, a temporary switch to a backup identity provider was implemented. Additionally, a hotfix was applied to address the root cause within the external identity provider.
Identified the misconfiguration in the database connection pool settings during routine maintenance.
Rolled back the recent changes to the database configuration to restore normal connectivity.
Implemented additional monitoring alerts for critical database parameters to catch similar misconfigurations promptly.
Root Cause and Resolution:

### Root Cause:
A misconfiguration during routine maintenance led to incorrect database connection pool settings, causing a disruption in user authentication services.

### Resolution:

Rolled back the recent changes to the database configuration, restoring proper connectivity.
Conducted a thorough review of the maintenance process to prevent similar misconfigurations in the future.
Implemented additional checks in the deployment pipeline to catch database configuration changes before they impact the live environment.
Corrective and Preventative Measures:

### Improvements/Fixes:

Enhance the change management process to include thorough reviews of database configuration changes before deployment.
Establish a clear rollback plan for routine maintenance activities to minimize the impact of misconfigurations.
Conduct regular training sessions for the operations and maintenance teams on best practices for database configuration changes.

### Tasks to Address the Issue:

Implement a patch for the authentication service to enable automatic failover support to secondary identity providers. Enhance incident response protocols for a more efficient involvement of the system reliability team. Document the incident and resolution process for future reference and training purposes.


