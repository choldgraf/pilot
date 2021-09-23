# Pricing

The fee for the 2i2c Hub Service is paid monthly. This covers the services provided as described above.
The cost of the hub service is highly dependent on the use-case, complexity of the environment, and cloud resources that are needed.
In the alpha phase, 2i2c’s goal is to offer hubs at a bespoke price that is sustainable for both us and the communities we serve.

:::{admonition} If you’d like a quote
If you'd like a quote for estimated cloud costs and the management fee for your hub service, please fill out [this Google form to understand your use-case](https://docs.google.com/forms/d/e/1FAIpQLSepevnAiyN7ECZqTvTd5W7H6AePv7t5APnqTZ3r2D8gp1Nepw/viewform?usp=sf_link).
:::

There are two major components to the price of 2i2c's Managed JupyterHubs service: DevOps fees, and Cloud Costs.
We give an overview of major considerations for each below.

## DevOps costs

2i2c provides "DevOps as a Service" for the communities that it serves.
This means that we design, operate, develop, and support the cloud infrastructure that powers each JupyterHub.
For a more in-depth description of what this entails, see [](services/overview:what-we-provide).

As the 2i2c Managed JupyterHubs service is in an `alpha` stage, we are still researching and understanding what the price of these DevOps services will be.
We'll fill in more details in this section as we understand them better, but in the meantime here are a few guidelines that we'll use for our pricing:

2i2c DevOps fees should be:

- Competitive with other "Data Science environment as a service" offerings.
- An amount that is sustainable for the communities we serve, with mechanisms to accommodate institutions with fewer resources.
- An amount that allows 2i2c to both sustain itself and thrive, and covers our time developing and supporting open source projects as part of the service.

## Cloud costs

### How much will my cloud costs be?

This is difficult to estimate ahead of time, because it is **heavily** dependent on the primary use-case and size of your community, and because cloud vendors change the cost of their machines often (though they don't change by much).

We recommend checking out [the Zero to JupyterHub cost projection documentation](z2jh:cost), which has a lot of useful background information to understand this.

For one example to help you estimate, see the section below.

#### An example with Google Cloud Platform

To get a rough estimate of your cloud costs, here is a rough guide that is based on **Memory (RAM)**. It is a reasonable rule of thumb as long as you don't any particularly complex needs like extremely large datasets or scalable computing/GPUs.

:::{admonition} Other cloud vendors may differ
This example focuses on Google Cloud Platform.
There are similar machine types (and generally similar prices) across all of the vendors. You can perform a similar calculation with [AWS](https://calculator.s3.amazonaws.com/index.html) or [Azure](https://azure.microsoft.com/en-us/pricing/calculator/) by following the same steps using a machine that has a similar amount of RAM and CPU as a `e2-highmem4`)
:::

1. **Read [the Zero to JupyterHub cost projection documentation](z2jh:cost)**. This is a nice high-level overview of the factors that drive the cost of JupyterHub deployments on commercial cloud.
2. **Estimate memory available to each user**. The amount of RAM needed for each user is often the biggest driver of cloud cost. Decide the "maximum" amount of RAM that a user will generally need, and multiply that by 1.5x.
3. **Determine how many average simultaneous users you'd like a hub to support**. This isn't necessarily the total size of your community, but how many people you think will be using the hub *at the same time*.
4. **Look up the monthly price of an `e2-highmem4` machine**. This is a basic machine that is suitable for many use-cases. [Go to the Google Cloud pricing page](https://cloud.google.com/compute/vm-instance-pricing) and go to the `E2 high-memory machine types` section. In that section, look for the `e2-highmem-4` monthly price.

Now calculate a rough estimate of your monthly cloud cost with the following formula:

```
(n_avg_simultaneous_users * memory_per_user) / 16GB * monthly_price
```

So for example, if you have a community of **100 total users** but expect an average of only 20 of them to be active at the same time, and each user requires **4GB** of RAM, then with a monthly `e2-highmem4` price of $97.83 (as of {sub-ref}`today`), then your monthly cost will be around:

```
(20 * 4) / 16 * 97.83 = $489.15 / month or $5,869.80 / year
```

Or, around **$4.80 per user per month** in cloud costs. If you required **2GB RAM** instead of **4GB RAM**, cloud costs would likely drop to around **$2.40 per user per month**.

:::{warning}
This is just a rough estimate! As mentioned above, the actual costs will vary from this, but this amount should be correct within an order of magnitude.
:::

### Who pays for cloud costs?

You should pay *only* for the cloud costs you actually incur, and you should have control over the financial resources available to run your infrastructure.
2i2c has two approaches to handle cloud billing:

**You manage billing, we manage infrastructure.** If you’d like to manage your own cloud billing, or have credits to use, simply give us permissions to run infrastructure that uses this account. 2i2c is then not involved in managing your cloud bill at all. We can provide guidance for setting up alerts / checkpoints on the billing if you wish.

**We manage both billing and infrastructure.** If you wish that 2i2c also manage cloud billing for the Hub infrastructure, 2i2c will manage a billing account for you (and give you administrative access to it). We will send you an additional “Cloud Billing” invoice. This will be used to purchase credits that are used to run your hub’s infrastructure.

```{figure} https://drive.google.com/uc?export=download&id=1PU2qBZH_nzIGI1-16vBMsdWE6gPqqz-P

An overview of our cloud pricing options and how 2i2c fits in with each.
```
