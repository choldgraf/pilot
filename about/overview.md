(about-the-project)=
# Overview

2i2c JupyterHubs offer interactive computing environments designed to serve multiple users via a JupyterHub that runs in the cloud.
They are designed and deployed by the [International Interactive Computing Collaboration](https://2i2c.org) (or 2i2c). They are [a team with many years of experience](https://2i2c.org/about/) running interactive computing infrastructure for research and education.

## Who is a 2i2c JupyterHub for?

2i2c JupyterHubs are designed for communities in research and education who want the following things:

1. Access to the latest technology in Jupyter and interactive computing for collaborative and scalable data science running in the cloud.
2. To utilize open source, community-driven tools and standards.
3. To use infrastructure that they could take control of themselves, and that gives the user the [Right to Replicate](overview/right-to-replicate).
4. To use infrastructure that is designed by and for individuals in research and education.
5. To support infrastructure from a non-profit organization that is committed to communities in research, education, and open source.

(services/overview:what-we-provide)=
## What will 2i2c provide?

2i2c will operate and manage a 2i2c JupyterHub deployment for use by you and your community, accessible via a web URL. 2i2c will handle the design, configuration, development, and ongoing operation of the hub infrastructure.

The following sections describe several common activities that the 2i2c team will perform as a part of your managed JupyterHub.

### JupyterHub Setup

* Requirement definitions and technical scoping
* Architectural design
* Initial deployment on cloud infrastructure

### Ongoing development of hub infrastructure

* Develop customizations needed for the hub deployment
* Updates to the hub software environment
* Upgrades and optimizations to 2i2c Hub infrastructure

### Ongoing operation of hub infrastructure

* Debug infrastructure issues, with expedited turnaround time for responses
* Providing “escalation support” before / during / after the outages and downtime
* Provide support to hub admins to facilitate their use of the infrastructure

### Development of open source software that underlie the 2i2c Hubs

* Improvements to the Jupyter ecosystem of tools and standards for interactive computing.
* New features and bug fixes for the tools that are used in a 2i2c Hub

(overview/right-to-replicate)=
## Your Right to replicate

A core principle of 2i2c is to build and manage technology that is controlled by the community that uses it.
One way in which we adhere to this principle is by respecting the [Customer Right to Replicate](https://2i2c.org/right-to-replicate/). This states the following:

```{epigraph}
The Right to Replicate gives customers the right to replicate their infrastructure in its entirety elsewhere, with or without 2i2c.
```

We believe that following this principle will lead to a more equitable and more productive ecosystem for research and education in the cloud. It also helps avoid many of the potential downsides of relying on a cloud vendor for infrastructure. Read the [Right to Replicate](https://2i2c.org/right-to-replicate/) documentation for more information about what this means.

(people-behind-hubs)=
## What 2i2c provides

Each Hub is a collaboration between 2i2c team members, and representatives from the community that uses the hub.
They require a variety of expertise to design, deploy, maintain, and use.

Generally speaking, 2i2c provides **development** and **operation** of a 2i2c JupyterHub, as well as **support** for questions and issues that arise with the hub infrastructure.
It does this in collaboration with leaders from the community for a particular hub (usually, these leaders have "administrative" rights on a hub with more priveleges for user control etc).

:::{seealso}
- **Support options**: see [](../admin/howto/support.md).
:::

## Funding open source

Everything that 2i2c deploys is open source and community-driven projects.
We prioritize using multi-stakeholder projects that are well-supported by a diverse community of contributors.
The resources that we receive to run 2i2c JupyterHubs thus **also go towards making open-source improvements** in these communities so that others may benefit from them.
We see this as an opportunity to solve two problems with one stream of funding: support research and education, and [support open source communities](https://2i2c.org/values/) in the Jupyter ecosystem and beyond.

## Replicate a 2i2c Hub

2i2c JupyterHubs are designed to use entirely open-source tools that work in other contexts.
We are a non-profit organization that believes that using tools that are interoperable, open-source, and owned by the community will empower research and education and make it more equitable and inclusive.
For this reason we are committed to deploying open source infrastructure that you can take elsewhere and deploy on your own.

Check out [](../admin/howto/replicate.md) for information about replicating a 2i2c JupyterHub.
