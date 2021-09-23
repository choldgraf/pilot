# Roles for the service

There are a few major roles that we define for the Managed JupyterHub Service.
These are outlined below.

```{figure} https://drive.google.com/uc?export=download&id=1sT3pSgMePpsnQKUNih0gLUsJWqG2os1D
A short overview of the major roles that participate in the Managed JupyterHub Service
```

(roles:community-representative)=
## Community Representative

The job of a Community Representative is to ensure that the interests of the {term}`Hub Community` are represented in the infrastructure, and that the hub serves their needs.
There must be **one or two community representatives for a given community**.
This role is usually filled by someone that is a member of the hub's community of practice.

### Responsibilities

- The main point of contact between the hub engineer and the {term}`Hub Community`.
- Collect feedback and questions from users on a hub.
- Surface questions and requests to Hub Engineers via support tickets.
- Oversee the [Hub Administrators](roles:hub-administrator)


(roles:hub-administrator)=
## Hub Administrator

The job of hub administrators is to support users and to perform common administrative operations on a hub that do not require intervention from a [Hub Engineer](roles:hub-engineer).
[Community Representatives](roles:community-representative) are the first Hub Administrators, and they may add new Hub Administrators via the JupyterHub interface.
They are able to add users, start/stop servers, and generally have more control over operations on the hub.

:::{seealso}
See the [Hub Administrator's guide](/admin/index) for helpful information for Hub Administrators.
:::

:::{warning}
Only give this role to people you trust, as they can perform disruptive actions for other users.
:::

### Responsibilities

- Provide support to users of a hub for common problems that don't require a Hub Engineer to resolve.
- Add new users to a hub, including administrative users.
- Surface major issues or requests to the Community Representative(s).

(roles:hub-engineer)=
## Hub Engineer

The job of a Hub Engineer is to develop and operate deployment infrastructure for a hub, and to perform major upgrades or improvements to resolve issues that cannot be solved by a [Hub Administrator](roles:hub-administrator).
Hub engineers regularly work on the JupyterHub infrastructure and provide open source development for the technology that powers each hub.
People in these roles are generally affiliated with 2i2c.

### Responsibilities

- Respond to support requests from the Community Representative(s)
- Perform major upgrades on hub infrastructure
- Debug and resolve major issues with a hub that require intervention from a Hub Engineer
- Perform open source development on technologies that are in use by the hubs
