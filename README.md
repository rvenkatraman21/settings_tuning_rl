# Settings Management using Reinforcement Learning methods
## Background and Problem Statement

Our fulfillment operations are executed through a series of decision making systems – setting ETAs, assigning couriers, deciding offer values, and coordinating demand supply in the market. Each of these systems makes tradeoffs between estimated cost, speed, service quality and has a huge impact on them. The levers used in these systems rely on tuning “settings” to balance out key KPIs.

Tuning a setting in a single service takes a significant amount of time and resources (through experiments spanning many weeks for a single setting and through offline studies of our research teams), and may still be suboptimal since most settings are static over time and space. To further add to the complexity, all the systems are interconnected and the settings are not managed in a coordinated way. This solution aims to solve this gap by optimizing different settings in the Fulfillment system through an automated Reinforcement Learning mechanism. Eventually, these decisions can be coordinated across different services in Fulfillment.
The north star of this effort is to create a system that intelligently coordinates settings (or interventions) across all fulfillment services.

Examples of different levers available to coordinate the fulfillment process:
- [Strategic] Courier Supply: Scheduling, Missions
- [Tactical] Demand: ETA expectations, Offer Minimums, Market Pauses
- [Tactica] Transmission to restaurant
- [Tactical] Dispatching: Delivery Bundling, Driver Wait In Restaurant, Offer Delays
- [Tactical] Driver Pay: Offer escalations, Pay minimums


### Who does it impact?
Externally, this impacts all sides of the marketplace – diners, drivers and restaurants.
Internally, it impacts Operations and Product teams that are responsible for Fulfillment metrics and use the levers available in different services to control the metrics.


## Idea Description
The proposed solution will be a naive Proof of Concept of a generic Reinforcement Learning framework. It will be constructed and tested through simulated data that may loosely mimic the behavior of our existing systems. Specifically, we will explore simulated scenarios where we assume a relationship between a setting (let’s say a setting in Dispatch that controls the tradeoff between Driver Engaged Time and ETA Error), the current market state (OPC, order backlog etc.) and key metrics (say Fulfillment Cost and Late %), with noise added to the impacted metric to simulate reality. This relationship will be constructed using observations from past tests. We will simulate two scenarios:
Current status: The setting is a static value.
Reinforcement Learning (RL) method: The optimal settings are learned through a reward function provided to the RL model. Note that the simulated RL model will not know the established relationship between the setting, current state and the metrics. The RL model only sees the current state, action and resulting outcome for learning the relationship.
We hope to demonstrate the RL method can learn this unknown relationship and arrive at settings that result in KPIs that are as good or an improvement on the current state, without having to manually tune the setting, as we do currently. We may also learn how long the learning process might take before such a system can be used in Production, and how it is impacted by the noise (uncertainty) levels.
Next, we will explore the simulated data mirroring two adjacent services (ETA and Dispatch) instead of just one service in isolation, and control settings in both of them in parallel.

Here's a [deck](https://docs.google.com/presentation/d/1ei_pWtxqPsthQe9DSc-FIjff3KtGVw1Di8V_H6Yj-Jg/edit#slide=id.gf64b6b6521_0_124) with simulated results

## Out of Scope/ What it will not do?
This exercise will just be a Proof of Concept to demonstrate the learning capability of the RL model and its dynamic nature during uncertainty. We will NOT:
Optimize settings on the real Fulfillment Simulation System (GHOST). In the interest of time, we will be demonstrating the learning behavior by simulating the interaction between settings, market state and downstream KPIs using an assumed relationship.
Use any Production Dispatch or DE code. As suggested in (1), we will be demonstrating the learning behavior by simulating the interaction between settings, market state and downstream KPIs using an assumed relationship.
Consider behavior across all Fulfillment services. For the current proof of concept, we will consider 1-2 settings in Dispatch and Delivery Estimation only.

