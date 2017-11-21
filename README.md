# createCiscoIseGuests
Python Module for creating guest wireless accounts on Cisco ISE

# Objective: #
Use python module to create Guest Accounts on Cisco ISE.  This script can also be used to test ISE has been correctly configured.


# Solution #
- Use python module to test API connectivity with ISE 2.3.
- Python module takes ISE PAN IP address, ERS and Sponsor username/password inputs and automatically identifies corresponding SponsorID and Spronsor Portal IDs.
- With the Cisco API, you can create, read, update, delete, and search for guest users.
- Requires External RESTful Services (ERS) API to be enabled on ISE (https://www.cisco.com/c/en/us/td/docs/security/ise/2-1/api_ref_guide/api_ref_book/ise_api_ref_ers1.html)


ISE ERS Configuration Example: https://communities.cisco.com/docs/DOC-66297
Cisco ISE Guest API Guide: https://www.cisco.com/c/en/us/td/docs/security/ise/2-1/api_ref_guide/api_ref_book/ise_api_ref_guest.html


# On Cisco ISE...#
### Connect to ISE PAN ###
![](/images/ise-pan.png)


>- Note: you can also use the “Cisco ISE 2.3 Mobility Sandbox v1” on dcloud http://dcloud.cisco.com if you don't have access to an ISE server to play with.  
Cisco Dcloud
![](/images/dcloud.png)


### Enable ERS API within ISE ###
- Navigate to **Administration** > **System** > **Settings** and select ERS Settings from the left panel.
- Enable the ERS APIs by selecting Enable ERS for Read/Write and Save
![](/images/ise-enable-ers.png)

>Note: The ERS APIs are disabled by default for security so you must enable it.
>**ERS is also disabled after ISE upgrades, so have to re-enable it.**


### Create ERS API Admin User ###
![](/images/ise-ers-admin.png)
>- You must create separate users (not admin) with the ERS Admin (Read/Write) or ERS Operator (Read-Only) roles to use the ERS APIs.

- Navigate to Administration > System > Admin Access
- Choose Administrators > Admin Users from the left pane
- Choose +Add > Create an Admin User to create a new ers-admin account (and optional ers-operator account).
- This account will be used to collect ERS API information.


### Create a user account that has rights to create guest accounts ###
![](/images/ise-api-user.png)
- Navigate to **Administration** > **Identity Management** > **Identities**, then choose Users from the left pane
- Choose +Add > Create a User to create a new apisponsor account.
- Note: By default, users in the ALL_ACCOUNTS user identity group are members of the sponsor group and can manage all guest user accounts.


#### Allow Guest Accounts to be created through the API ###
![](/images/ise-enable-api.png)
- Navigate to **Work Centers** > **Guest Access** > **Portals & Components**, then from the left menu, select “Sponsor Groups” and ALL_ACCOUNTS
- Check the “Access Cisco ISE guest accounts using the programmatic interface (Guest REST API)”.



## Run Python module to Create a Guest User ##

- update the settings.py file with ISE PAN IP address and credentials
- Python module learns SponsorId and Sponsor Portal ID
- Python module uses requests POST to create the user account (URL listed below)
- Note use of user and Sponsor Portal ID from previous step
- Please see API documentation in the External RESTful Services (ERS) Online SDK referenced previously. Select “Guest User” for required and optional fields.

![](/images/ise-guest-fields.png)


# Validate on ISE #
![](/images/ise-guest-validation.png)
- Go to **Work Centers** > **Guest Access** > **Reports**
- Select Reports, Guest Access Reports and then Sponsor Login and Audit from the left menu.
