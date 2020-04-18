"""
**Submitted to ANAC 2020 SCML**
*Authors* type-your-team-member-names-with-their-emails here


This code is free to use or update given that proper attribution is given to 
the authors and the ANAC 2020 SCML. 

This module implements a factory manager for the SCM 2020 league of ANAC 2019 
competition. This version will use subcomponents. Please refer to the 
[game description](http://www.yasserm.com/scml/scml2020.pdf) for all the 
callbacks and subcomponents available.

Your agent can learn about the state of the world and itself by accessing 
properties in the AWI it has. For example:

- The number of simulation steps (days): self.awi.n_steps  
- The current step (day): self.awi.current_steps
- The factory state: self.awi.state
- Availability for producton: self.awi.available_for_production


Your agent can act in the world by calling methods in the AWI it has. 
For example:

- *self.awi.request_negotiation(...)*  # requests a negotiation with one partner
- *self.awi.request_negotiations(...)* # requests a set of negotiations

 
You can access the full list of these capabilities on the documentation.

- For properties/methods available only to SCM agents, check the list 
  [here](http://www.yasserm.com/scml/scml2020docs/api/scml.scml2020.AWI.html)

"""

# required for development
from scml.scml2020.agents import DoNothingAgent

# required for running the test tournament
import time
from tabulate import tabulate
from scml.scml2020.utils import anac2020_std, anac2020_collusion
from scml.scml2020.agents import DecentralizingAgent, BuyCheapSellExpensiveAgent
from negmas.helpers import humanize_time

# required for typing
from typing import List, Optional, Dict, Any
import numpy as np
from negmas import (
    Issue, AgentMechanismInterface, Contract, Negotiator,
    MechanismState, Breach,
)
from scml.scml2020.world import Failure
from scml.scml2020 import SCML2020Agent
from scml.scml2020 import PredictionBasedTradingStrategy
from scml.scml2020 import MovingRangeNegotiationManager, StepNegotiationManager
from scml.scml2020 import DemandDrivenProductionStrategy, SupplyDrivenProductionStrategy

from .trading import MyPredictionBasedTradingStrategy

class _NegotiationCallbacks:
    def acceptable_unit_price(self, step, sell) -> int:
        production_cost = np.max(self.awi.profile.costs[:, self.awi.my_input_product])
        if sell:
            return production_cost + self.input_cost[step]
        return self.output_price[step] - production_cost

    def target_quantity(self, step, sell) -> int:
        if sell:
            needed, secured = self.outputs_needed, self.outputs_secured
        else:
            needed, secured = self.inputs_needed, self.inputs_secured

        return needed[step] - secured[step]

    def target_quantities(self, steps, sell) -> np.ndarray:
        """Implemented for speed but not really required"""

        if sell:
            needed, secured = self.outputs_needed, self.outputs_secured
        else:
            needed, secured = self.inputs_needed, self.inputs_secured

        return needed[steps[0] : steps[1]] - secured[steps[0] : steps[1]]

class BaRgent(
    _NegotiationCallbacks,
    SupplyDrivenProductionStrategy,
    StepNegotiationManager,
    PredictionBasedTradingStrategy,
    SCML2020Agent
):
    """
    This is the only class you *need* to implement. You can create the agent
    by combining the following strategies:
    
    1. A trading strategy that decides the quantities to sell and buy
    2. A negotiation manager that decides which negotiations to engage in and 
       uses some controller(s) to control the behavior of all negotiators
    3. A production strategy that decides what to produce

    """
    pass



if __name__ == '__main__':    
    competitors = [BaRgent, DecentralizingAgent, BuyCheapSellExpensiveAgent]
    run(competitors, n_steps=16)
