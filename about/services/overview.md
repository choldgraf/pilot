# Overview of hub services

2i2c builds and operates **distributions of JupyterHubs** that are tailored for particular use-cases.
These services share many of the same infrastructure components, but have customizations and optimizations that are more domain- or community-specific.

:::{note}
Our services are in an "alpha" state - we are still learning a lot about the best way that these hubs can serve communities in research and education.
The infrastructure and service may change over the coming months!
See [our strategy page](../strategy.md) for an overview of what we're hoping to do and where we're headed next.
:::

## What technology makes up each hub?

🚀 core infrastructure
: Underneath each 2i2c JupyterHub is a [JupyterHub](https://jupyter.org/hub). These provide interactive computing sessions for each of your users, and connect to the other infrastructure in the cloud. We use [`auth0`](https://auth0.com/) and [CILogon](https://www.cilogon.org/) for authenticating users, which can connect to a number of other authentication protocols (such as OAuth2).

💻 interfaces
: Each 2i2c JupyterHub has two main interactive interfaces: Jupyter interfaces (Notebook and Lab), and RStudio. Each of them is accessible from your session via `/tree`, `/lab`, and `/rstudio` endpoints in your URL.

🌄 environment
: Your 2i2c JupyterHub has an environment that has been created for your particular use-case. It exists as a Docker image that your JupyterHub loads when a user starts a new session. These images can either be built with the tool [repo2docker](https://repo2docker.readthedocs.io/), or pulled directly from a Docker registry. The environment also comes pre-loaded with some tools that are helpful for working with JupyterHub, such as [nbgitpuller](https://jupyterhub.github.io/nbgitpuller). See [](environment/custom) for more information.

🤖 hardware
: 2i2c JupyterHubs can run on most major cloud providers - the primary thing that is needed is a working Kubernetes deployment. By default, 2i2c runs its hubs on Google Cloud, but if communities wish to use a different provider, this can be accomplished as well. This also means that the hardware underlying the Kubernetes deployment is configurable.

📦 data
: The data that is used by your 2i2c JupyterHub is provided by you! 2i2c JupyterHubs can connect with a variety of public data sources. We recommend using standard data structures or specifications via libraries like [Intake](https://intake.readthedocs.io/en/latest/). Note that 2i2c does not host this data itself, but can build connections between 2i2c JupyterHubs and these data sources.

## Features of each hub

Here is a brief overview of the major features that are present in each.

```{csv-table}
:header-rows: 1
:widths: 20, 70, 5, 5
:file: ../../build_assets/feature-matrix.csv
```

<script>
    headers = document.querySelectorAll(".feature-header");
    headers.forEach((header) => {
        td = header.parentElement
        td.setAttribute("colspan", "100")
        td.classList.add("feature-header")
        tr = td.parentElement
        tr.querySelectorAll("td:not(.feature-header)").forEach((td) => {
            td.remove()
        })
    })
</script>
<style>
    td.feature-header {
        font-weight: 500;
        background-color: #f8f9fa;
    }
</style>

(note-on-urls)=
## Where are hubs accessed?

By default all 2i2c JupyterHub get their own URL with the following form:

```
<hub-name>.<community-name>.2i2c.cloud
```

Each 2i2c JupyterHub has **hub name** (denoted by `<hub-name>`) and a **community name** (denoted by `<community-name>`). Communities are collections of hubs around a particular community or collaboration. Each community infrastructure may be run by different teams. For more information, see [](people-behind-hubs).

It is also possible to provide your own URL that points to a 2i2c JupyterHub.

## Will 2i2c keep information about a hub's users?

2i2c will not collect user data for any purpose. 2i2c will have access to all of the information that is inside a hub (which it requires in order to debug problems and and assist with upgrades), however we will not retain any of this data or move it *outside* of the hub, and will not retain it once the hub is shut down (except in order to transfer data to you at your request).

## Data outside of the hub

If you wish to access data that exists outside of your 2i2c Hub, it is your responsibility to put this data in the cloud and manage the infrastructure around it. 2i2c does not control this data, it merely provides access to it via your hub infrastructure.

## Where are hubs configured and deployed?

All of the configuration and deployment scripts for the 2i2c JupyterHub can be found at [the `pilot-hubs/` repository](https://github.com/2i2c-org/pilot-hubs). This repository contains both the deployment code as well as documentation that explains how it works. It should be treated as "for advanced users only", and is provided for transparency and as a guide for the community to follow if they wish to manage their own infrastructure similar to 2i2c JupyterHub.

To learn about how the `pilot-hubs/` repository works, we recommend checking out the [`pilot-hubs` documentation](ph:index).

See the next sections for more information about each hub distribution.
