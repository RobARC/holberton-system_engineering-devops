# 0x0A Configuration management

## Background Context

When I was working for SlideShare, I worked on an auto-remediation tool called Skynet that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the servers hostname or any other metadata we had (server type, server environment). At some point, a bug was present in my code that sent nil to the filter method.

There were 2 pieces of bad news:

<ol>
<li>When MCollective receives nil as an argument for its filter method, it takes this to mean all servers</li>
<li>The action I sent was to terminate the selected servers</li>
</ol>
I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShares entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.

##Resources
<b>Read or watch:</b>

#### [Intro to Configuration Management](https://intranet.hbtn.io/rltoken/r-NmkYO8bxIKp2qEx2ZjKQ)
#### [Puppet resource type: file (check Resource types for all manifest types in the left menu)](https://intranet.hbtn.io/rltoken/fuhnsI9_1_F4GrHwGT3GxA)
#### [Puppets Declarative Language: Modeling Instead of Scripting](https://intranet.hbtn.io/rltoken/Fqmb5rnChQgYAypvKoTxAQ)
#### [Puppet lint](https://intranet.hbtn.io/rltoken/oezu0m_hJ8nEVA6a9o17Tw)
#### [Puppet emacs mode](https://intranet.hbtn.io/rltoken/N70cVw8mG3707He-OxjP1w)
