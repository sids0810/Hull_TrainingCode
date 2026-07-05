from assets import LoanPool
from liabilities import Tranche
from engine import CapitalStructureGenerator
from engine import WaterfallEngine

if __name__ == "__main__":

    test_pool = LoanPool(100000000, 0.05, 360, 0.005, 1)

    test_pool.amortize_pool()

    structure = CapitalStructureGenerator(test_pool.initial_balance, 0.03)

    bond_stack = structure.generate_tranches()

    run_engine = WaterfallEngine(bond_stack)

    run_engine.run_waterfall(test_pool)

    for i in bond_stack:
        print(f"Name: {i.get_name()} | Current Balance: {i.current_balance}")
