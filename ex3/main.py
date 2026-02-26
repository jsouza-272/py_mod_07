from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine


def rrr(x: dict):
    x['home'] = 3030303


if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")
    factory = FantasyCardFactory()
    print("Factory: FantasyCardFactory")
    strategy = AggressiveStrategy()
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    print("\nSimulating aggressive turn...")
    print("Hand:", engine.player.get('hand'))

    print("\nTurn execution:")
    print("Strategy:", engine.strategy.get_strategy_name())
    print("Actions:", engine.simulate_turn())

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")
