## About the connector
FortiCASB-SSPM (SaaS Security Posture Management) is a cloud-based solution that provides visibility into security risks, user activities, identities, and data exposure across connected SaaS applications via API integration.
<p>This document provides information about the FortiCASB-SSPM Connector, which facilitates automated interactions, with a FortiCASB-SSPM server using FortiSOAR&trade; playbooks. Add the FortiCASB-SSPM Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with FortiCASB-SSPM.</p>

### Version information

Connector Version: 1.0.0


Authored By: Julian Petersohn (Fortinet Cloud CSE)

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-forticasb-sspm`

## Prerequisites to configuring the connector
- You must have the URL of FortiCASB-SSPM server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the FortiCASB-SSPM server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>FortiCASB-SSPM</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Integration Key<br></td><td><br>
<tr><td>URL<br></td><td><br>
<tr><td>User ID<br></td><td><br>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Risks<br></td><td>Pull SSPM findings/misconfigurations (risks)<br></td><td> <br/><br></td></tr>
<tr><td>Get Identities<br></td><td>Get Suridata identities<br></td><td> <br/><br></td></tr>
<tr><td>Get User Activities<br></td><td>Get User activities.<br></td><td> <br/><br></td></tr>
<tr><td>Get Files<br></td><td>Get details and information related to files.<br></td><td> <br/><br></td></tr>
<tr><td>Get Audit Log<br></td><td>Get FortiCASB-SSPM Audit Log<br></td><td> <br/><br></td></tr>
</tbody></table>

### operation: Get Risks
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Limit<br></td><td>Limit the amount of returned results<br>
</td></tr><tr><td>Sort<br></td><td>Sort order of creation date<br>
</td></tr><tr><td>Minimum Score<br></td><td>Filter results from minimum score<br>
</td></tr><tr><td>Maximum Score<br></td><td>Filter results to maximum score<br>
</td></tr><tr><td>Sort Field<br></td><td>Field to sort by<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Identities
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Limit<br></td><td>Limit the number of results in the response<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get User Activities
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Limit<br></td><td>Limit the number of results in the response<br>
</td></tr><tr><td>Activity Types<br></td><td>Filter specific activities types<br>
</td></tr><tr><td>Application Names<br></td><td>Filter specific applications names<br>
</td></tr><tr><td>User E-Mails<br></td><td>Filter specific emails that triggered the activity<br>
</td></tr><tr><td>Time Sort Field<br></td><td>Determine if time sort and filter apply to activity time or event creation time<br>
</td></tr><tr><td>Start Date/Time<br></td><td>Filter results from date according to field_time<br>
</td></tr><tr><td>End Date/Time<br></td><td>Filter results to date according to field_time<br>
</td></tr><tr><td>Order<br></td><td>Sort results according to field_time<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Files
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Limit<br></td><td>Limit the number of results in the response<br>
</td></tr><tr><td>Sort<br></td><td>Sort order of creation date<br>
</td></tr><tr><td>Create Date/Time From<br></td><td>Filter results from start date of file creation<br>
</td></tr><tr><td>Create Date/Time To<br></td><td>Filter results till end date of file creation<br>
</td></tr><tr><td>Update Date/Time From<br></td><td>Filter results from start date of file modification<br>
</td></tr><tr><td>Update Date/Time To<br></td><td>Filter results till end date of file modification<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Audit Log
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Limit<br></td><td>Limit the number of results in the response<br>
</td></tr><tr><td>Sort<br></td><td>Sort order of creation date<br>
</td></tr><tr><td>Start Date<br></td><td>Filter results from start date<br>
</td></tr><tr><td>End Date<br></td><td>Filter results till end date<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

## Included playbooks
The `Sample - forticasb-sspm - 1.0.0` playbook collection comes bundled with the FortiCASB-SSPM connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the FortiCASB-SSPM connector.

- Get Audit Log
- Get Files
- Get Identities
- Get Risks
- Get User Activities

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
